import argparse
import time

# bool string Type to bool Type
def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def get_config():

    # instantiate
    parser = argparse.ArgumentParser()


    # Add params

    # params for training
    parser.add_argument("--num_agents", type=int, default=2)  # the number of agent OK
    parser.add_argument("--seed", type=int, default=75, help="Random seed for numpy/torch")  # set random seed
    parser.add_argument("--episode_limit", type=int, default=100000)  # Total episode
    parser.add_argument("--episode_length", type=int, default=600)  # Max step (replay buffer parameters)
    parser.add_argument("--gpu", type=int, default=3)  # GPU id


    #params for planner
    parser.add_argument("--num_symOption",type=int,default=6)  # the number of symbolic options


    # -------------------------------------- mappo
    parser.add_argument("--env_name", type=str, default='GoTogether', help="specify the name of environment")
    parser.add_argument("--experiment_name", type=str,
                        default='HS-MARL')
    parser.add_argument("--user_name", type=str, default='xcmu',
                        help="[for wandb usage], to specify user's name for simply collecting training data.")
    parser.add_argument("--algorithm_name", type=str,
                        default='mappo', choices=["rmappo", "mappo"])


    parser.add_argument("--cuda", action='store_false', default=True,
                        help="by default True, will use GPU to train; or else will use CPU;")  # use GPU or CPU  OK
    parser.add_argument("--cuda_deterministic",
                        action='store_false', default=True,
                        help="by default, make sure random seed effective. if set, bypass such function.")  # OK
    parser.add_argument("--n_training_threads", type=int,
                        default=1, help="Number of torch threads for training")  # the number of threads of torch for training OK
    parser.add_argument("--n_rollout_threads", type=int, default=1,
                        help="Number of parallel envs for training rollouts")  # the number of threads for env.  OK
    parser.add_argument("--n_eval_rollout_threads", type=int, default=1,
                        help="Number of parallel envs for evaluating rollouts")  # 测试：实例化1个环境
    parser.add_argument("--n_render_rollout_threads", type=int, default=1,
                        help="Number of parallel envs for rendering rollouts")  # 渲染：实例化1个环境


    # 可视化操作？
    parser.add_argument("--use_wandb", action='store_false', default=True,
                        help="[for wandb usage], by default True, will log date to wandb server. or else will use tensorboard to log data.")
    
    # env parameters
    parser.add_argument("--use_obs_instead_of_state", action='store_true',
                        default=False,
                        help="Whether to use global state or concatenated obs")  # using the concatenant observation instead of env. state

    # network parameters
    parser.add_argument("--share_policy", action='store_false',
                        default=True, help='Whether agent share the same policy')  # Is using the shared policy
    parser.add_argument("--use_centralized_V", action='store_false',
                        default=True, help="Whether to use centralized V function")  # Is using the centralized function?
    parser.add_argument("--stacked_frames", type=int, default=1,
                        help="Dimension of hidden layers for actor/critic networks")  # hidden layer
    parser.add_argument("--use_stacked_frames", action='store_true',
                        default=False, help="Whether to use stacked_frames")  # 是否使用hidden layer
    parser.add_argument("--hidden_size", type=int, default=64,
                        help="Dimension of hidden layers for actor/critic networks")  # hidden size
    parser.add_argument("--layer_N", type=int, default=1,
                        help="Number of layers for actor/critic networks")  # layer数目
    parser.add_argument("--use_ReLU", action='store_false',
                        default=True, help="Whether to use ReLU")  # 是否relu

    # 一些trick
    parser.add_argument("--use_popart", action='store_true', default=False,
                        help="by default False, use PopArt to normalize rewards.")  # Is using PopArt to normalize rewards OK
    parser.add_argument("--use_valuenorm", action='store_false', default=True,
                        help="by default True, use running mean and std to normalize rewards.")  # Is using running mean and std to normalize rewards  OK
    parser.add_argument("--use_feature_normalization", action='store_false',
                        default=True, help="Whether to apply layernorm to the inputs")  # 是否layer normalization
    parser.add_argument("--use_orthogonal", action='store_false', default=True,
                        help="Whether to use Orthogonal initialization for weights and 0 initialization for biases")  # 使用Orthogonal initialization初始化
    parser.add_argument("--gain", type=float, default=0.01,
                        help="The gain # of last action layer")

    # recurrent parameters
    parser.add_argument("--use_naive_recurrent_policy", action='store_true',
                        default=False, help='Whether to use a naive recurrent policy')  # Is using naive recurrent policy? OK
    parser.add_argument("--use_recurrent_policy", action='store_false',
                        default=False, help='use a recurrent policy')  # Is using recurrent policy?    OK
    parser.add_argument("--recurrent_N", type=int, default=1, help="The number of recurrent layers.")  # 循环网络的层数
    parser.add_argument("--data_chunk_length", type=int, default=10,
                        help="Time length of chunks used to train a recurrent_policy")  # the data trunk used to train policy network  OK

    # optimizer parameters
    parser.add_argument("--lr", type=float, default=5e-4,
                        help='learning rate (default: 5e-4)')  # learning rate OK
    parser.add_argument("--critic_lr", type=float, default=5e-4,
                        help='critic learning rate (default: 5e-4)')  # critic's learning rate OK
    parser.add_argument("--opti_eps", type=float, default=1e-5,
                        help='RMSprop optimizer epsilon (default: 1e-5)')  # optimization epsilon OK
    parser.add_argument("--weight_decay", type=float, default=0)  # weight decay OK

    # ppo parameters
    parser.add_argument("--ppo_epoch", type=int, default=15,
                        help='number of ppo epochs (default: 15)')  # epochs  OK
    parser.add_argument("--use_clipped_value_loss",
                        action='store_false', default=True,
                        help="by default, clip loss value. If set, do not clip loss value.")  # Is using the clipped value loss OK
    parser.add_argument("--clip_param", type=float, default=0.2,
                        help='ppo clip parameter (default: 0.2)')  # clip parameters OK
    parser.add_argument("--num_mini_batch", type=int, default=1,
                        help='number of batches for ppo (default: 1)')  # mini-batch   OK
    parser.add_argument("--entropy_coef", type=float, default=0.01,
                        help='entropy term coefficient (default: 0.01)')  # the coefficient of entropy OK
    parser.add_argument("--value_loss_coef", type=float,
                        default=1, help='value loss coefficient (default: 0.5)')  # the coefficient of value loss OK
    parser.add_argument("--use_max_grad_norm",
                        action='store_false', default=True,
                        help="by default, use max norm of gradients. If set, do not use.")  # Is using the max norm of gradients OK
    parser.add_argument("--max_grad_norm", type=float, default=10.0,
                        help='max norm of gradients (default: 0.5)')  # max norm of gradients (default: 0.5)  OK
    parser.add_argument("--use_gae", action='store_false',
                        default=True, help='use generalized advantage estimation')  # 是否使用gae trick
    parser.add_argument("--gamma", type=float, default=0.99,
                        help='discount factor for rewards (default: 0.99)')  # 奖励衰减系数
    parser.add_argument("--gae_lambda", type=float, default=0.95,
                        help='gae lambda parameter (default: 0.95)')  # gae trick中的lambda参数
    parser.add_argument("--use_proper_time_limits", action='store_true',
                        default=False, help='compute returns taking into account time limits')  # 在考虑到时间限制的情况下计算回报
    parser.add_argument("--use_huber_loss", action='store_false', default=True,
                        help="by default, use huber loss. If set, do not use huber loss.")  # Is using the Huber loss OK
    parser.add_argument("--use_value_active_masks",
                        action='store_false', default=True,
                        help="by default True, whether to mask useless data in value loss.")  # whether to mask useless data in value loss.  OK
    parser.add_argument("--use_policy_active_masks",
                        action='store_false', default=True,
                        help="by default True, whether to mask useless data in policy loss.")  # whether to mask useless data in policy loss   OK
    parser.add_argument("--huber_delta", type=float, default=10.0, help=" coefficience of huber loss.")  #  coefficience of huber loss  OK

    # run parameters
    parser.add_argument("--use_linear_lr_decay", action='store_true',
                        default=False, help='use a linear schedule on the learning rate')  # Is using linear decay of the learning rate?
    # save parameters
    parser.add_argument("--save_interval", type=int, default=1,
                        help="time duration between contiunous twice models saving.")  # 连续两次模型保存之间的时间长度

    # log parameters
    parser.add_argument("--log_interval", type=int, default=5,
                        help="time duration between contiunous twice log printing.")  # 连续两次log输出之间的时间长度

    # eval parameters
    parser.add_argument("--use_eval", action='store_true', default=False,
                        help="by default, do not start evaluation. If set`, start evaluation alongside with training.")  # 默认情况下，不启动评估。如果设置`，则与训练同时开始评估。
    parser.add_argument("--eval_interval", type=int, default=25,
                        help="time duration between contiunous twice evaluation progress.")  # 每25个epoch下进行一次评估
    parser.add_argument("--eval_episodes", type=int, default=32,
                        help="number of episodes of a single evaluation.")  # 一次评估中的episode长度

    # render parameters
    parser.add_argument("--save_gifs", action='store_true', default=False,
                        help="by default, do not save render video. If set, save video.")  # 不保存渲染视频
    parser.add_argument("--use_render", action='store_true', default=False,
                        help="by default, do not render the env during training. If set, start render. Note: something, the environment has internal render process which is not controlled by this hyperparam.")  # 是否开启渲染
    parser.add_argument("--render_episodes", type=int, default=5,
                        help="the number of episodes to render a given env")  # 渲染一个给定的环境所需的剧集数量
    parser.add_argument("--ifi", type=float, default=0.1,
                        help="the play interval of each rendered image in saved video.")  # 保存视频中每个渲染图像的播放时间间隔

    # pretrained parameters
    parser.add_argument("--model_dir", type=str, default=None,
                        help="by default None. set the path to pretrained model.")  # 模型的路径，可去预训练model


    args = parser.parse_args()

    return args