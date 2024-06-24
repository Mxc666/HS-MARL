import numpy as np
import gym
from gym import spaces
from envs.env import Env


class MultiDiscrete(gym.Space):
    """
    - The multi-discrete action space consists of a series of discrete action spaces with different parameters
    - It can be adapted to both a Discrete action space or a continuous (Box) action space
    - It is useful to represent game controllers or keyboards where each key can be represented as a discrete action space
    - It is parametrized by passing an array of arrays containing [min, max] for each discrete action space
       where the discrete action space can take any integers from `min` to `max` (both inclusive)
    Note: A value of 0 always need to represent the NOOP action.
    e.g. Nintendo Game Controller
    - Can be conceptualized as 3 discrete action spaces:
        1) Arrow Keys: Discrete 5  - NOOP[0], UP[1], RIGHT[2], DOWN[3], LEFT[4]  - params: min: 0, max: 4
        2) Button A:   Discrete 2  - NOOP[0], Pressed[1] - params: min: 0, max: 1
        3) Button B:   Discrete 2  - NOOP[0], Pressed[1] - params: min: 0, max: 1
    - Can be initialized as
        MultiDiscrete([ [0,4], [0,1], [0,1] ])
    """

    def __init__(self, array_of_param_array):
        super().__init__()
        self.low = np.array([x[0] for x in array_of_param_array])
        self.high = np.array([x[1] for x in array_of_param_array])
        self.num_discrete_space = self.low.shape[0]
        self.n = np.sum(self.high) + 2

    def sample(self):
        """ Returns a array with one sample from each discrete action space """
        # For each row: round(random .* (max - min) + min, 0)
        random_array = np.random.rand(self.num_discrete_space)
        return [int(x) for x in np.floor(np.multiply((self.high - self.low + 1.), random_array) + self.low)]

    def contains(self, x):
        return len(x) == self.num_discrete_space and (np.array(x) >= self.low).all() and (
                np.array(x) <= self.high).all()

    @property
    def shape(self):
        return self.num_discrete_space

    def __repr__(self):
        return "MultiDiscrete" + str(self.num_discrete_space)

    def __eq__(self, other):
        return np.array_equal(self.low, other.low) and np.array_equal(self.high, other.high)


# train (子进程的环境)
class SubprocVecEnv(object):
    def __init__(self, all_args):  # 构造action space，observation space，以及shared observation space
        """
        envs: list of gym environments to run in subprocesses
        """
        # Env这个需要根据自己环境去改，Env实际上就是建立环境时所需的那几个基本元素（观测维度，动作维度，step，reset）
        self.env_list = [Env(i) for i in range(all_args.n_rollout_threads)]  # 训练时开五个子进程
        self.num_envs = all_args.n_rollout_threads  # 五个子进程，各有一个环境

        self.num_agent = self.env_list[0].agent_num  # agent个数
        self.signal_obs_dim = self.env_list[0].obs_dim  # 观测维度 14
        self.signal_action_dim = self.env_list[0].action_dim  # 动作维度 5

        self.u_range = 1.0  # control range for continuous control，连续空间的动作范围
        self.movable = True  # 如果一个agent有多个动作空间，则用这个配合使用

        # environment parameters
        # self.discrete_action_space = True
        self.discrete_action_space = True  # 是否离散动作空间

        # if true, action is a number 0...N, otherwise action is a one-hot N-dimensional vector
        self.discrete_action_input = False  # 离散的动作输入或者对动作进行one-hot编码
        # if true, even the action is continuous, action will be performed discretely
        self.force_discrete_action = False  # 是否将动作空间强制离散化

        # configure spaces 最终使用的变量
        self.action_space = []  # 动作空间，每个维度对应一个agent
        self.observation_space = []  # 观测空间，每个维度对应一个agent
        self.share_observation_space = []  # 共享观测空间，把所有的agent的观测拼接
        share_obs_dim = 0  # 初始化共享观测的维度
        for agent in range(self.num_agent):  # 遍历每一个agent
            total_action_space = []  # 每个智能体开始时都会重新初始化。用于存储每个智能体的多个动作空间，应该考虑的是一个智能体的多个动作

            # physical action space
            if self.discrete_action_space:  # 离散动作空间
                u_action_space = spaces.Discrete(self.signal_action_dim)  # 生成离散的动作 Discrete(5)
                # print(u_action_space.n), 5
            else:  # 连续动作空间
                u_action_space = spaces.Box(low=-self.u_range, high=+self.u_range, shape=(2,),
                                            dtype=np.float32)  # [-1,1]
            if self.movable:  # 可移动才会进入total_action里面
                total_action_space.append(u_action_space)  # 用于下面的if判断

            # total action space
            if len(total_action_space) > 1:  # 当前智能体如果是多个动作空间，则会进入这里，然后把它们整合
                # all action spaces are discrete, so simplify to MultiDiscrete action space
                if all([isinstance(act_space, spaces.Discrete) for act_space in
                        total_action_space]):  # 如果当前agent的多个动作空间都是离散的，则会把他们整合为混合离散空间
                    act_space = MultiDiscrete([[0, act_space.n - 1] for act_space in total_action_space])

                else:
                    act_space = spaces.Tuple(total_action_space)  # 如果不全是离散空间，则把这些动作空间用元组存储
                self.action_space.append(act_space)  # 存储处理后的作为动作空间
            else:  # 当前智能体如果是一个动作空间，则会进入这里
                self.action_space.append(total_action_space[0])

            # observation space
            share_obs_dim += self.signal_obs_dim  # 共享观测需要把所有agent的观测维度加起来
            # 观测空间的构造，值是连续的，维度是14维
            self.observation_space.append(spaces.Box(low=-np.inf, high=+np.inf, shape=(self.signal_obs_dim,),
                                                     dtype=np.float32))  # [-inf,inf]
            # print(self.observation_space) [Box(-inf, inf, (14,), float32), Box(-inf, inf, (14,), float32)]

        self.share_observation_space = [spaces.Box(low=-np.inf, high=+np.inf, shape=(share_obs_dim,),
                                                   dtype=np.float32) for _ in range(self.num_agent)]
        # print(self.share_observation_space) [Box(-inf, inf, (28,), float32), Box(-inf, inf, (28,), float32)]

    # 返回5个线程各自的结果
    def step(self, actions):
        """
        输入actions纬度假设：
        # actions shape = (5, 2, 5)
        # 5个线程的环境，里面有2个智能体，每个智能体的动作是一个one_hot的5维编码
        """
        # for env, action in zip(self.env_list, actions):
        #     print(env, action) 形如：<envs.env.Env object at 0x000001FFE8344850> [[0. 0. 0. 0. 1.]
        #      [0. 0. 0. 0. 1.]]
        results = [env.step(action) for env, action in zip(self.env_list, actions)]  # 执行动作, 每个子线程下和对应的action做zip

        # print(np.array(results).shape)

        # print(*results) 两个智能体
        # 形如：[[array([0.29017378, 0.82546682, 0.75042642, 0.11363518, 0.01565707,
        # 0.68397345, 0.40832007, 0.97293181, 0.98817457, 0.48801269,
        # 0.48546021, 0.31783374, 0.95191906, 0.84361277]), array([0.38771313, 0.65537966, 0.66054361, 0.59661837, 0.06229965,
        # 0.02799428, 0.20041577, 0.74098257, 0.6847851 , 0.06338255,
        # 0.86746395, 0.88598935, 0.21314289, 0.90137743])], [[0.6734774447413128], [0.3518900029366867]], [False, False], [{}, {}]]

        obs, rews, dones, infos = zip(*results)

        # print(np.array(rews).shape)  (5, 2, 1)
        # print(rews)
        # 形如：
        # ([[0.3758931584360722], [0.07956037304288421]], [[0.7744469020952874], [0.8731443161698165]], [[0.9051444833720836], [0.8742706718428822]], [[0.16134255363546757], [0.9979875585524395]], [[0.49388488912679696], [0.2662860798709977]])

        # print(np.stack(rews)) 应该是对应5个线程
        # [[[0.96234351]
        #   [0.87774482]]

        #  [[0.25459432]
        #   [0.46015987]]

        #  [[0.39997915]
        #   [0.01441116]]

        #  [[0.34151431]
        #   [0.8745412 ]]

        #  [[0.21294098]
        #   [0.55071665]]]
        return np.stack(obs), np.stack(rews), np.stack(dones), infos

    # 返回5个线程各自的结果
    def reset(self):
        obs = [env.reset() for env in self.env_list]
        # print(np.array(obs).shape) (5, 2, 14)
        # print(np.stack(obs).shape) (5, 2, 14)
        return np.stack(obs)

    def close(self):
        pass

    def render(self, mode="rgb_array"):
        pass
