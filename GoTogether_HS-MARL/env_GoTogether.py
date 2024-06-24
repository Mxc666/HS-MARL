import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import random
from gym import spaces
# import cv2

class EnvGoTogether(object):
    def __init__(self, size):
        self.map_size = size
        self.occupancy = np.zeros((self.map_size, self.map_size))  # 背景板
        for i in range(self.map_size):  # 生成黑色边框
            self.occupancy[0][i] = 1
            self.occupancy[self.map_size - 1][i] = 1
            self.occupancy[i][0] = 1
            self.occupancy[i][self.map_size - 1] = 1
        self.agt1_pos = [self.map_size - 3, 1]  # 红色agent的位置
        self.agt2_pos = [self.map_size - 2, 2]  # 蓝色agent的位置
        self.goal_pos = [1, self.map_size - 2]  # 绿色goal的位置

        self.thriple_ypos = int((self.map_size - 1)/3)
        self.thriple_xpos = int(self.map_size - self.thriple_ypos)
        self.thriple_pos = [self.thriple_xpos, self.thriple_ypos]

        self.num_agent = 2  # define the number of agent
        self.action_dim = 4  # define the action dimension of agent
        self.numState = [[1, 0, 0, 0]] * self.num_agent  # All Free

        self.isTerminal = False
        self.isGlobal = False

        self.NearGoal_list = []
        for i in range(3 * 1):
            for j in range(3 * 1):
                self.NearGoal_list.append([self.goal_pos[0] - 1 + i, self.goal_pos[1] - 1 + j])
        self.NearGoal_list.remove(self.goal_pos)

    def reset(self):
        self.occupancy = np.zeros((self.map_size, self.map_size))  # 重置背景板
        for i in range(self.map_size):   # 周围黑框
            self.occupancy[0][i] = 1
            self.occupancy[self.map_size - 1][i] = 1
            self.occupancy[i][0] = 1
            self.occupancy[i][self.map_size - 1] = 1
        self.agt1_pos = [self.map_size - 3, 1]   # 红色agent位置
        self.agt2_pos = [self.map_size - 2, 2]   # 蓝色agent位置
        self.goal_pos = [1, self.map_size - 2]   # 绿色goal位置

        self.numState = [[1, 0, 0, 0]] * self.num_agent  # All Free
        self.isTerminal = False
        self.isGlobal = False

    def get_state(self):
        state = np.zeros((1, 4))
        state[0, 0] = self.agt1_pos[0] / self.map_size
        state[0, 1] = self.agt1_pos[1] / self.map_size
        state[0, 2] = self.agt2_pos[0] / self.map_size
        state[0, 3] = self.agt2_pos[1] / self.map_size
        return state

    def step(self, action_list):
        reward = 0
        bad_n = 0
        # agent1 move
        if action_list[0] == 0:  # move up
            if self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1]] != 1:  # if can move
                self.agt1_pos[0] = self.agt1_pos[0] - 1
        elif action_list[0] == 1:  # move down
            if self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1]] != 1:  # if can move
                self.agt1_pos[0] = self.agt1_pos[0] + 1
        elif action_list[0] == 2:  # move left
            if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] - 1] != 1:  # if can move
                self.agt1_pos[1] = self.agt1_pos[1] - 1
        elif action_list[0] == 3:  # move right
            if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] + 1] != 1:  # if can move
                self.agt1_pos[1] = self.agt1_pos[1] + 1
        
        ####################################################################################
        # agent2 move
        if action_list[1] == 0:  # move up
            if self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1]] != 1:  # if can move
                self.agt2_pos[0] = self.agt2_pos[0] - 1
        elif action_list[1] == 1:  # move down
            if self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1]] != 1:  # if can move
                self.agt2_pos[0] = self.agt2_pos[0] + 1
        elif action_list[1] == 2:  # move left
            if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] - 1] != 1:  # if can move
                self.agt2_pos[1] = self.agt2_pos[1] - 1
        elif action_list[1] == 3:  # move right
            if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] + 1] != 1:  # if can move
                self.agt2_pos[1] = self.agt2_pos[1] + 1

        # 两个agent都要走到goal的位置
        if self.agt1_pos == self.goal_pos and self.agt2_pos == self.goal_pos:
            reward = reward + 100
            self.isGlobal = True

        # x^2 + y^2 下于等于1，或者大于9都被认为是太近
        if self.sqr_dist(self.agt1_pos, self.agt2_pos)<=1 or self.sqr_dist(self.agt1_pos, self.agt2_pos)>9:
            reward = reward - 0.1
            bad_n += 0.1
        
        done = False
        if reward > 0:  # 只有当两个agent together，同时不要太近也不太远的情况下，到达goal，才被认为是terminate
            done = True
            self.isTerminal = True

        # update numState
        # r1Goal, r2Goal
        if self.agt1_pos == self.goal_pos and self.agt2_pos == self.goal_pos:
            self.numState = [[0, 0, 0, 1]] * self.num_agent

        # r1NearGoal, r2NearGoal
        elif self.agt1_pos in self.NearGoal_list and self.agt2_pos in self.NearGoal_list:
            self.numState = [[0, 0, 1, 0], [0, 0, 1, 0]]

        # r1other, r2NearGoal
        elif self.agt1_pos not in self.NearGoal_list and self.agt2_pos in self.NearGoal_list:
            self.numState = [[0, 1, 0, 0], [0, 0, 1, 0]]

        # r1NearGoal, r2other
        elif self.agt1_pos in self.NearGoal_list and self.agt2_pos not in self.NearGoal_list:
            self.numState = [[0, 0, 1, 0], [0, 1, 0, 0]]

        return [[[reward]]*self.num_agent, [done]*self.num_agent, [{}]*self.num_agent, [bad_n]]

    # x^2 + y^2
    def sqr_dist(self, pos1, pos2):
        return (pos1[0]-pos2[0])*(pos1[0]-pos2[0])+(pos1[1]-pos2[1])*(pos1[1]-pos2[1])

    # 全图的RGB作为agent的观测
    def get_global_obs(self):
        obs = np.zeros((self.map_size, self.map_size, 3))
        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.occupancy[i][j] == 0:
                    obs[i, j, 0] = 1.0
                    obs[i, j, 1] = 1.0
                    obs[i, j, 2] = 1.0  # 白色RGB

        obs[self.agt1_pos[0], self.agt1_pos[1], 0] = 1.0
        obs[self.agt1_pos[0], self.agt1_pos[1], 1] = 0.0
        obs[self.agt1_pos[0], self.agt1_pos[1], 2] = 0.0  # 红色 agent RGB

        obs[self.agt2_pos[0], self.agt2_pos[1], 0] = 0.0
        obs[self.agt2_pos[0], self.agt2_pos[1], 1] = 0.0
        obs[self.agt2_pos[0], self.agt2_pos[1], 2] = 1.0  # 蓝色 agent RGB

        obs[self.goal_pos[0], self.goal_pos[1], 0] = 0.0
        obs[self.goal_pos[0], self.goal_pos[1], 1] = 1.0
        obs[self.goal_pos[0], self.goal_pos[1], 2] = 0.0  # 绿色 agent RGB
        return obs

    def get_agt1_obs(self):
        obs = self.get_global_obs()
        return obs
    
    def get_agt2_obs(self):
        obs = self.get_global_obs()
        return obs

    def get_obs(self):
        return [self.get_agt1_obs(), self.get_agt2_obs()]

    # Match to the env. shape of mappo
    def get_flatten_obs(self):
        return [list(self.get_agt1_obs().flatten()), list(self.get_agt2_obs().flatten())]

    # mappo need the centralized observation
    def get_shared_flatten_obs(self):
        return [list(self.get_agt1_obs().flatten())+list(self.get_agt2_obs().flatten())] * self.num_agent

    # mappo need the action space shape
    def get_action_space(self):
        return [spaces.Discrete(self.action_dim), spaces.Discrete(self.action_dim)]

    # get the observation dimension
    def get_obs_dim(self):
        return len(self.get_flatten_obs()[0])

    # get Item state, representation by number
    def getNumState(self):
        return self.numState

    def plot_scene(self):
        plt.figure(figsize=(5, 5))
        plt.imshow(self.get_global_obs())
        plt.xticks([])
        plt.yticks([])
        plt.show()

    def render(self):
        obs = self.get_global_obs()
        enlarge = 30
        new_obs = np.ones((self.map_size*enlarge, self.map_size*enlarge, 3))
        for i in range(self.map_size):
            for j in range(self.map_size):

                if obs[i][j][0] == 0.0 and obs[i][j][1] == 0.0 and obs[i][j][2] == 0.0:
                    cv2.rectangle(new_obs, (j * enlarge, i * enlarge), (j * enlarge + enlarge, i * enlarge + enlarge), (0, 0, 0), -1)
                if obs[i][j][0] == 1.0 and obs[i][j][1] == 0.0 and obs[i][j][2] == 0.0:
                    cv2.rectangle(new_obs, (j * enlarge, i * enlarge), (j * enlarge + enlarge, i * enlarge + enlarge), (0, 0, 255), -1)
                if obs[i][j][0] == 0.0 and obs[i][j][1] == 1.0 and obs[i][j][2] == 0.0:
                    cv2.rectangle(new_obs, (j * enlarge, i * enlarge), (j * enlarge + enlarge, i * enlarge + enlarge), (0, 255, 0), -1)
                if obs[i][j][0] == 0.0 and obs[i][j][1] == 0.0 and obs[i][j][2] == 1.0:
                    cv2.rectangle(new_obs, (j * enlarge, i * enlarge), (j * enlarge + enlarge, i * enlarge + enlarge), (255, 0, 0), -1)
        cv2.imshow('image', new_obs)
        cv2.waitKey(100)
