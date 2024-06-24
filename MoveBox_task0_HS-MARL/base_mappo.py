import numpy as np
import torch
from utils.shared_buffer import SharedReplayBuffer
from algorithms.algorithm.r_mappo import RMAPPO as TrainAlgo  # Trainer class for MAPPO to update policies
from algorithms.algorithm.rMAPPOPolicy import RMAPPOPolicy as Policy  # MAPPO Policy - value and action



def _t2n(x):
    """Convert torch tensor to a numpy array."""
    return x.detach().cpu().numpy()


class Base_mappo(object):
    """
    Base class for training recurrent policies.
    :param config: (dict) Config dictionary containing parameters for training.
    """

    def __init__(self, config):
        self.all_args = config['all_args']
        self.envs = config['envs']
        self.device = config['device']
        self.num_agents = self.all_args.num_agents

        # parameters
        self.env_name = self.all_args.env_name
        self.algorithm_name = self.all_args.algorithm_name
        self.use_obs_instead_of_state = self.all_args.use_obs_instead_of_state
        self.episode_length = self.all_args.episode_length
        self.n_rollout_threads = self.all_args.n_rollout_threads
        self.n_eval_rollout_threads = self.all_args.n_eval_rollout_threads
        self.n_render_rollout_threads = self.all_args.n_render_rollout_threads
        self.use_linear_lr_decay = self.all_args.use_linear_lr_decay
        self.hidden_size = self.all_args.hidden_size
        self.use_wandb = self.all_args.use_wandb
        self.use_render = self.all_args.use_render
        self.recurrent_N = self.all_args.recurrent_N

        # generate mappo policy (policy network), need to judge whether use centralized V
        self.use_centralized_V = self.all_args.use_centralized_V
        share_observation_space = self.envs.share_observation_space[0] if self.use_centralized_V \
            else self.envs.observation_space[0]
        self.policy = Policy(self.all_args,
                             self.envs.observation_space[0],
                             share_observation_space,
                             self.envs.action_space[0],
                             device=self.device)

        # Trainer class for mappo to update policies.
        self.trainer = TrainAlgo(self.all_args, self.policy, device=self.device)
        # replay buffer for mappo
        self.buffer = SharedReplayBuffer(self.all_args,
                                         self.num_agents,
                                         self.envs.observation_space[0],
                                         share_observation_space,
                                         self.envs.action_space[0])



    def warmup(self):
        """Collect warmup pre-training data."""
        raise NotImplementedError

    def collect(self, step):
        """Collect rollouts for training."""
        raise NotImplementedError

    def insert(self, data):
        """
        Insert data into buffer.
        :param data: (Tuple) data to insert into training buffer.
        """
        raise NotImplementedError

    @torch.no_grad()
    def compute(self):
        """Calculate returns for the collected data."""
        self.trainer.prep_rollout()
        next_values = self.trainer.policy.get_values(np.concatenate(self.buffer.share_obs[-1]),
                                                     np.concatenate(self.buffer.rnn_states_critic[-1]),
                                                     np.concatenate(self.buffer.masks[-1]))
        next_values = np.array(np.split(_t2n(next_values), self.n_rollout_threads))
        self.buffer.compute_returns(next_values, self.trainer.value_normalizer)

    def train(self):
        """Train policies with data in buffer. """
        self.trainer.prep_training()
        train_infos = self.trainer.train(self.buffer)
        self.buffer.after_update()
        return train_infos