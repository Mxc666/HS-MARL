import numpy as np
import gym
from env_MoveBox import EnvMoveBox  # env Class


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


# train
class SubprocVecEnv(object):
    def __init__(self, all_args):
        """
        envs: list of gym environments to run in subprocesses
        """

        self.env_list = [EnvMoveBox(i) for i in range(all_args.n_rollout_threads)]
        self.num_envs = all_args.n_rollout_threads

        self.num_agent = self.env_list[0].num_agent
        self.signal_obs_dim = self.env_list[0].get_obs_dim()

        # configure spaces
        self.action_space = list(self.env_list[0].get_action_space())
        self.observation_space = list(self.env_list[0].get_flatten_obs())

        # shared observation space
        self.share_observation_space = self.env_list[0].get_shared_flatten_obs()


    def step(self, actions):

        results = [env.step(action.flatten()) for env, action in zip(self.env_list, actions)]
        rews, dones, infos = zip(*results)

        return np.stack(rews), np.stack(dones), infos

    def reset(self):
        for env in self.env_list:
            env.reset()

    def reset_obs(self):
        obs_list = []
        for env in self.env_list:
            env.reset()
            obs_list.append(env.get_flatten_obs())

        return np.stack(obs_list)

    def isTerminal(self):
        return [env.isTerminal for env in self.env_list]

    def isGlobal(self):
        return [env.isGlobal for env in self.env_list]

    def getNumState(self):
        return [env.getNumState() for env in self.env_list]

    def get_obs(self):
        return [env.get_flatten_obs() for env in self.env_list]