import wandb
import socket
from pathlib import Path
import os
import torch
import numpy as np
import pandas as pd
from argParser_Seed_1 import get_config   # arg. setting
from env_wrapped import SubprocVecEnv  # env Class
from rewrite_mappo import mappo  # MAPPO: option's policy
from meta_controller import SymbolicModel  # meta-controller: generate plan



# Setting parameters
args = get_config()


# choose algorithm and check Error
if args.algorithm_name == "rmappo":  # network is rnn
    assert (args.use_recurrent_policy or args.use_naive_recurrent_policy), ("check recurrent policy!")
elif args.algorithm_name == "mappo":
    assert (args.use_recurrent_policy == False and args.use_naive_recurrent_policy == False), ("check recurrent policy!")
else:
    raise NotImplementedError


# use GPU or CPU
if args.cuda and torch.cuda.is_available():  # GPU
    print("\nchoose to use gpu...\n")
    device = torch.device("cuda:"+str(args.gpu))
    torch.set_num_threads(args.n_training_threads)  # the number of threads of torch for training, default: 1
    if args.cuda_deterministic:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
else:  # CPU
    print("\nchoose to use cpu...\n")
    device = torch.device("cpu")
    torch.set_num_threads(args.n_training_threads)


def log_train(train_infos, total_num_steps):
        """
        Log training info.
        :param train_infos: (dict) information about training update.
        :param total_num_steps: (int) total number of training env steps.
        """
        for k, v in train_infos.items():
            wandb.log({k: v}, step=total_num_steps)



# Interpretative
SymOption_dict = {'0': 'AllFree -> r1Free(NotLocal) r2AtLever', '1': 'AllFree -> r1PassMid r2AtLever(MeanWhile)', '2': 'AllFree -> r1AtLever r2Free(NotLocal)', \
                  '3': 'AllFree -> r1AtLever r2PassMid(MeanWhile)', '4': 'r1Free r2AtLever -> r1PassMid r2AtLever', '5': 'r1PassMid r2AtLever(MeanWhile) -> r1PassMid r2AtLever', \
                  '6': 'r1AtLever r2Free -> r1AtLever r2PassMid', '7': 'r1AtLever r2PassMid(MeanWhile) -> r1AtLever r2PassMid', '8': 'r1PassMid r2AtLever -> r1UpPart r2AnyPos(NotLocal)', \
                  '9': 'r1AtLever r2PassMid -> r1AnyPos(NotLocal) r2UpPart', '10': 'r1UpPart r2AnyPos(NotLocal) -> r1GetTreasure r2AnyPos(NotLocal)', '11': 'r1AnyPos r2UpPart -> r1AnyPos(NotLocal) r2GetTreasure', \
                  }
Action_SET = [[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]],  # m0: r1 Free r2 AtLever
             [[1, 0, 1, 0, 0], [0, 1, 0, 0, 0]],  # m1: r1 PassMid r2 AtLever
             [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0]],  # m2: r1 AtLever r2 Free
             [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0]]]  # m3: r1 AtLever r2 PassMid
TREE = {0: 4, 1: 5, 2: 6, 3: 7,\
        4: 8, 5: 8, 6: 9, 7: 9,\
        8: 10, 9: 11}  # successor nodes
              

# success
success_kindSeed = {}

# iterate seeds
cur_seed = args.seed
print('seed: ', cur_seed)

# wandb
# run dir
run_dir = Path(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0] + "/results") / args.env_name / args.experiment_name
if not run_dir.exists():
    os.makedirs(str(run_dir))
if args.use_wandb:
    run = wandb.init(config=args,
                     project=args.env_name,
                     entity=args.user_name,
                     notes=socket.gethostname(),
                     name=str(args.experiment_name) + "_seed_" + str(cur_seed),
                     group=args.experiment_name,
                     dir=str(run_dir),
                     job_type="training",
                     reinit=True)


torch.manual_seed(cur_seed)  # set seed for cpu
torch.cuda.manual_seed_all(cur_seed)  # set seed for GPU
np.random.seed(cur_seed)



# Define: instantiate env., agent, Meta-controller
envs = SubprocVecEnv(args)  # subproccess env., per env. is two agents move the box
config = {
        "all_args": args,  # parameters
        "envs": envs,  # environment
        "device": device,  # GPU/CPU
    }   # config, into mappo algorithm
All_option = args.num_symOption   # the number of symbolic options
agent_list = [mappo(config) for i in range(All_option)]  # define per option's policy
# Meta-controller, contains planner and Meta-controller
# input: state pairs, reward, Option set, sr;
# output: updated Option set, Action models
meta_controller = SymbolicModel(args)


# begin to Train the SOMAPPO
cumulative_average_reward = 0  # calcute the cumulative average reward
success_tracker = 0
cumulative_average_reward_log = {}
cur_plan_so_list = []
reward_num = 0 # using to compute the average rewards, episodes numbers
Steps = 0  # record the total step
maxStepsPerEpisode = args.episode_length   # Max step
episodes = int(args.episode_limit) // args.n_rollout_threads  # Max episodes: total episode/ threads

# reset env., buffer
[agent_list[i].warmup() for i in range(All_option)]   # reset env. and define replay buffer

act_reward = {'0': 0, '1': 0, '2': 0, '3': 0}  # initiate action models' reward (m0, m1, m2, m3)

# --------------------- generate numstate pairs (transition: action model)
meta_controller.generateNumStatePairs()
for episodeCount in range(episodes):  # record the episode, episodeCount is the current episode num
    print('\n====================================================')
    print('current seed: ', cur_seed, ', current episode: ', episodeCount)
        
    envs.reset()  # restart env. and not return observation
    episodeSteps = 0  # current episode's step, means episode_length

    # --------------------- planner, generate plan
    meta_controller.generateReward(act_reward, str(cur_seed)) # gain the tree's reward
    meta_controller.generatePlan(str(cur_seed))  # gain the plan

    plan_index = 0
    plan_externalReward = 0 # cumulative external reward of the plan
    plan_targetState = 0

    turn_tag = False
    another_option_num = 0
    # given the plan, execute the action model and choose option
    while (not envs.isTerminal()[0]) and episodeSteps <= maxStepsPerEpisode:

        chosen_shared_option = meta_controller.choose_SymOption(plan_index)  # given plan, choose option by index. Noted that: shared_option
        plan_index += 1  # increase the index counter

        # action turn
        if turn_tag == True:
            chosen_shared_option = TREE[another_option_num]
            another_option_num = chosen_shared_option


        if chosen_shared_option == 5 or chosen_shared_option == 7:
            continue

        option_externalReward = 0    # initial the external reward for per option (symbolic option)
        option_intrinsicReward = 0
        episodeSteps = 0  # initial its step, for per chosen option
        # attain the s1 for the current option, under the single thread
        S1Numstate = envs.getNumState()[0]  #  [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        # print('S1Numstate', S1Numstate)

        if agent_list[chosen_shared_option].use_linear_lr_decay:
            agent_list[chosen_shared_option].trainer.policy.lr_decay(episodeCount, args.episode_limit)

        # execute symbolic option
        print('chosen_shared_option', chosen_shared_option, ', means: ', SymOption_dict[str(chosen_shared_option)])

        # gain the final symbolic state(s2), given option
        S2numstate = meta_controller.getS2numstate(chosen_shared_option)

        DynaNumstate = envs.getNumState()[0]  # dynamic RL state, under the single thread

        Data_sets = []
        # interact with env. and train the symbolic option's policy, under the chosen option
        while (not envs.isTerminal()[0]) and (DynaNumstate != S2numstate) and (episodeSteps <= maxStepsPerEpisode):
            mappo_obs1 = np.array(envs.get_obs())
            # given option, using its policy to choose action
            values, actions, action_log_probs, rnn_states, \
                            rnn_states_critic, _ = agent_list[chosen_shared_option].collect(episodeSteps)

            # change the env., gain the external reward, under the single thread
            mappo_rewards, mappo_dones, mappo_infos, mappo_bad_n = envs.step(actions)
            mappo_obs2 = np.array(envs.get_obs())
            data = mappo_obs2, mappo_rewards, mappo_dones, mappo_infos, values, actions, \
                                                action_log_probs, rnn_states, rnn_states_critic
            data = list(data)

            # Noted that: this index 0 represent the thread index
            done = mappo_dones[0]
            DynaNumstate = envs.getNumState()[0]  # dynamic RL state
            reward = data[1][0]
            option_externalReward += reward[0][0]  # the chosen option's external reward
            # gain the intrinsic reward, use it to train the chosen option
            # reach the final state S2 (5), local optimal (-10)
            cur_bad_n = mappo_bad_n[0][0]
            intrinsicRewards = agent_list[chosen_shared_option].criticize(mappo_rewards[0][0][0], DynaNumstate == S2numstate, done, cur_bad_n)
            data[1] = [intrinsicRewards]  # 0+5/ 10-10/ 100+5

            # gain the trajectory, to train the agent policy
            # compute return and update network
            # using the data of replay buffer to train the chosen option
            agent_list[chosen_shared_option].insert(data)  # insert data into buffer, for the current option's policy
            agent_list[chosen_shared_option].compute()
            train_infos = agent_list[chosen_shared_option].train()

            reward = data[1][0]
            option_intrinsicReward += reward[0][0]
            episodeSteps += 1  # interaction number + 1

            Data_sets.append(data)
            if (chosen_shared_option <= 3) and (DynaNumstate != S2numstate) and (DynaNumstate in Action_SET):

                another_option_num = int(Action_SET.index(DynaNumstate))
                act_reward[str(another_option_num)] = option_intrinsicReward + 5
                turn_tag = True

                print('episod = ', episodeCount, 'Step = ', episodeSteps, ', not reach goal when ', SymOption_dict[str(chosen_shared_option)],\
                                            ', but reach goal when ', SymOption_dict[str(another_option_num)])
                cur_plan_so_list.append('episod = ' + str(episodeCount) + ', Step = ' + str(episodeSteps) + ', not reach goal when ' +
                    SymOption_dict[str(chosen_shared_option)] + ', but reach goal when ' + SymOption_dict[str(another_option_num)])

                if agent_list[another_option_num].use_linear_lr_decay:
                    agent_list[another_option_num].trainer.policy.lr_decay(episodeCount, args.episode_limit)

                intrinsicRewards = [[Data_sets[-1][1][0][0][0] + 5]]*args.num_agents
                Data_sets[-1][1] = [intrinsicRewards]
                for data in Data_sets:
                    agent_list[another_option_num].insert(data)  # insert data into buffer, for the current option's policy
                    agent_list[another_option_num].compute()
                    train_infos = agent_list[another_option_num].train()

                break

        # update current action models' reward
        if chosen_shared_option <= 3  and (DynaNumstate == S2numstate):
            act_reward[str(int(chosen_shared_option))] += option_intrinsicReward

        # update Sucess ratio S_r
        if DynaNumstate == S2numstate:  # reach the s2
            print('episod = ', episodeCount, 'Step = ', episodeSteps, ', reach goal when ', SymOption_dict[str(chosen_shared_option)])
            cur_plan_so_list.append('episod = ' + str(episodeCount) + ', Step = ' + str(episodeSteps) + ', reach goal when ' + SymOption_dict[str(chosen_shared_option)])
        else:
            print('episod = ', episodeCount, 'Step = ', episodeSteps, ', failed when ', SymOption_dict[str(chosen_shared_option)])
            cur_plan_so_list.append('episod = ' + str(episodeCount) + ', Step = ' + str(episodeSteps) + ', failed when ' + SymOption_dict[str(chosen_shared_option)])

        Steps += episodeSteps  # add the sub step (chosen option's) into the total step

        # record the current episode's reward
        plan_externalReward += option_externalReward
        if envs.isGlobal()[0]:
            plan_targetState += 1

    # record the average rewards
    reward_num += 1
    cumulative_average_reward = (cumulative_average_reward * (Steps-1) + plan_externalReward) /Steps
    success_tracker = (success_tracker * (Steps-1) + plan_targetState) /Steps
    cumulative_average_reward_log['average_episode_rewards'] = cumulative_average_reward
    cumulative_average_reward_log['success_tracker'] = success_tracker
    if args.use_wandb:
        log_train(cumulative_average_reward_log, Steps)


if args.use_wandb:
    run.finish()


so_pd = pd.DataFrame({'symbolic option':cur_plan_so_list})
so_pd.to_csv('./out/symbolic_option_' + str(cur_seed) + '.csv', index=False, sep=',')
