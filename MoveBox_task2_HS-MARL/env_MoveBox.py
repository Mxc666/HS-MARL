import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from gym import spaces
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import cv2


NUM_AGENT = 2


class EnvMoveBox(object):
    def __init__(self, i, key_path='key.png'):
        self.raw_occupancy = np.zeros((15, 15))
        for i in range(15):
            self.raw_occupancy[0, i] = 1
            self.raw_occupancy[i, 0] = 1
            self.raw_occupancy[14, i] = 1
            self.raw_occupancy[i, 14] = 1
            self.raw_occupancy[1, i] = 1
            self.raw_occupancy[5, i] = 1
            self.raw_occupancy[6, i] = 1
        self.raw_occupancy[1, 6] = 0
        self.raw_occupancy[1, 7] = 0
        self.raw_occupancy[1, 8] = 0
        self.raw_occupancy[5, 1] = 0
        self.raw_occupancy[5, 2] = 0
        self.raw_occupancy[5, 3] = 0
        self.raw_occupancy[5, 4] = 0
        self.raw_occupancy[6, 1] = 0
        self.raw_occupancy[6, 2] = 0
        self.raw_occupancy[6, 3] = 0
        self.raw_occupancy[6, 4] = 0
        self.raw_occupancy[6, 6] = 0
        self.raw_occupancy[6, 7] = 0
        self.raw_occupancy[6, 8] = 0
        self.raw_occupancy[11, 6] = 1
        self.raw_occupancy[11, 7] = 1
        self.raw_occupancy[11, 8] = 1
        self.raw_occupancy[12, 6] = 1
        self.raw_occupancy[12, 7] = 1
        self.raw_occupancy[12, 8] = 1
        self.raw_occupancy[13, 6] = 1
        self.raw_occupancy[13, 7] = 1
        self.raw_occupancy[13, 8] = 1

        self.occupancy = self.raw_occupancy.copy()

        self.agt1_pos = [13, 1]
        self.occupancy[self.agt1_pos[0], self.agt1_pos[1]] = 1
        self.agt2_pos = [13, 13]
        self.occupancy[self.agt2_pos[0], self.agt2_pos[1]] = 1

        self.box_pos = [10, 7]
        self.occupancy[self.box_pos[0], self.box_pos[1]] = 1

        self.is_1_catch_box = False
        self.is_2_catch_box = False

        # key 的初始化位置
        self.key_pos = [8, 3]
        self.key_image = plt.imread(key_path)
        self.isKey = True

        self.num_agent = 2  # define the number of agent
        self.action_dim = 4  # define the action dimension of agent
        self.numState = [[1, 0, 0, 0, 0, 0, 0]] * self.num_agent  # All Free

        self.isTerminal = False
        self.isGlobal = False

    def reset(self):
        
        for i in [5, 6]:
            for j in [10, 11, 12, 13]:
                self.raw_occupancy[i, j] = 1

        self.occupancy = self.raw_occupancy.copy()

        self.agt1_pos = [13, 1]
        self.occupancy[self.agt1_pos[0], self.agt1_pos[1]] = 1
        self.agt2_pos = [13, 13]
        self.occupancy[self.agt2_pos[0], self.agt2_pos[1]] = 1

        self.box_pos = [10, 7]
        self.occupancy[self.box_pos[0], self.box_pos[1]] = 1

        self.is_1_catch_box = False
        self.is_2_catch_box = False

        self.isKey = True

        self.numState = [[1, 0, 0, 0, 0, 0, 0]] * self.num_agent  # All Free
        self.isTerminal = False
        self.isGlobal = False

    def step(self, action_list):
        if self.is_1_catch_box == False:
            if action_list[0] == 0: # up
                if self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1]] != 1:  # if can move
                    self.agt1_pos[0] = self.agt1_pos[0] - 1
                    self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1]] = 0
                    self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            if action_list[0] == 1:   # down
                if self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1]] != 1:  # if can move
                    self.agt1_pos[0] = self.agt1_pos[0] + 1
                    self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1]] = 0
                    self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            if action_list[0] == 2:   # left
                if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] - 1] != 1:  # if can move
                    self.agt1_pos[1] = self.agt1_pos[1] - 1
                    self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] + 1] = 0
                    self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            if action_list[0] == 3:  # right
                if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] + 1] != 1:  # if can move
                    self.agt1_pos[1] = self.agt1_pos[1] + 1
                    self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] - 1] = 0
                    self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1

        if self.is_2_catch_box == False:
            if action_list[1] == 0: # up
                if self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1]] != 1:  # if can move
                    self.agt2_pos[0] = self.agt2_pos[0] - 1
                    self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1]] = 0
                    self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            if action_list[1] == 1:   # down
                if self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1]] != 1:  # if can move
                    self.agt2_pos[0] = self.agt2_pos[0] + 1
                    self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1]] = 0
                    self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            if action_list[1] == 2:   # left
                if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] - 1] != 1:  # if can move
                    self.agt2_pos[1] = self.agt2_pos[1] - 1
                    self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] + 1] = 0
                    self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            if action_list[1] == 3:  # right
                if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] + 1] != 1:  # if can move
                    self.agt2_pos[1] = self.agt2_pos[1] + 1
                    self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] - 1] = 0
                    self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1

        if self.is_1_catch_box and self.is_2_catch_box:  # LeftGlued & RightGlued
            if action_list[0] == 0 and action_list[1] == 0: # up
                if self.occupancy[self.box_pos[0] - 1,self.box_pos[1]] == 0 and self.occupancy[self.box_pos[0] - 1,self.box_pos[1] - 1] == 0 and self.occupancy[self.box_pos[0] - 1,self.box_pos[1] + 1] == 0:
                    self.box_pos[0] = self.box_pos[0] - 1
                    self.agt1_pos[0] = self.agt1_pos[0] - 1
                    self.agt2_pos[0] = self.agt2_pos[0] - 1
                    self.occupancy[self.box_pos[0] + 1, self.box_pos[1]] = 0
                    self.occupancy[self.agt1_pos[0] + 1, self.agt1_pos[1]] = 0
                    self.occupancy[self.agt2_pos[0] + 1, self.agt2_pos[1]] = 0
                    self.occupancy[self.box_pos[0], self.box_pos[1]] = 1
                    self.occupancy[self.agt1_pos[0], self.agt1_pos[1]] = 1
                    self.occupancy[self.agt2_pos[0], self.agt2_pos[1]] = 1
            if action_list[0] == 1 and action_list[1] == 1:  # down
                if self.occupancy[self.box_pos[0] + 1,self.box_pos[1]] == 0 and self.occupancy[self.box_pos[0] + 1,self.box_pos[1] - 1] == 0 and self.occupancy[self.box_pos[0] + 1,self.box_pos[1] + 1] == 0:
                    self.box_pos[0] = self.box_pos[0] + 1
                    self.agt1_pos[0] = self.agt1_pos[0] + 1
                    self.agt2_pos[0] = self.agt2_pos[0] + 1
                    self.occupancy[self.box_pos[0] - 1, self.box_pos[1]] = 0
                    self.occupancy[self.agt1_pos[0] - 1, self.agt1_pos[1]] = 0
                    self.occupancy[self.agt2_pos[0] - 1, self.agt2_pos[1]] = 0
                    self.occupancy[self.box_pos[0], self.box_pos[1]] = 1
                    self.occupancy[self.agt1_pos[0], self.agt1_pos[1]] = 1
                    self.occupancy[self.agt2_pos[0], self.agt2_pos[1]] = 1
            if action_list[0] == 2 and action_list[1] == 2:  # left
                if self.occupancy[self.box_pos[0], self.box_pos[1] - 2] == 0:
                    self.box_pos[1] = self.box_pos[1] - 1
                    self.agt1_pos[1] = self.agt1_pos[1] - 1
                    self.agt2_pos[1] = self.agt2_pos[1] - 1
                    self.occupancy[self.box_pos[0], self.box_pos[1] - 1] = 1
                    self.occupancy[self.box_pos[0], self.box_pos[1] + 2] = 0
            if action_list[0] == 3 and action_list[1] == 3:  # right
                if self.occupancy[self.box_pos[0], self.box_pos[1] + 2] == 0:
                    self.box_pos[1] = self.box_pos[1] + 1
                    self.agt1_pos[1] = self.agt1_pos[1] + 1
                    self.agt2_pos[1] = self.agt2_pos[1] + 1
                    self.occupancy[self.box_pos[0], self.box_pos[1] + 1] = 1
                    self.occupancy[self.box_pos[0], self.box_pos[1] - 2] = 0

        if self.agt1_pos[0] == self.box_pos[0] and abs(self.agt1_pos[1] - self.box_pos[1]) == 1:
            self.is_1_catch_box = True

        if self.agt2_pos[0] == self.box_pos[0] and abs(self.agt2_pos[1] - self.box_pos[1]) == 1:
            self.is_2_catch_box = True
        
        reward = 0    
        if (self.is_1_catch_box == True) and (self.is_2_catch_box == True) and (self.box_pos[0] == self.key_pos[0]) and (abs(self.box_pos[1] - self.key_pos[1]) <= 1) and (self.isKey):
            self.isKey = False
            reward += 5

            for i in [5, 6]:
                for j in [10, 11, 12, 13]:
                    self.raw_occupancy[i, j] = 0
          
        done = False
        # reward = 0
        if self.box_pos == [6, 7]:
            reward += 10
            done = True
            self.isTerminal = True

        if self.box_pos == [1, 7]:
            reward += 100
            done = True
            self.isTerminal = True
            self.isGlobal = True


        # update numState
        if self.is_1_catch_box == True and self.is_2_catch_box == True and self.box_pos == [10, 7]:  # not at middle and not delivered
            self.numState = [[0, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0]]  # Agent1 Holding, Agent2 Holding

        elif self.is_1_catch_box == True and self.is_2_catch_box == True and self.box_pos[0] >= 5 and self.box_pos[0] <= 6 and self.box_pos[1] <= 4:
            if not self.isKey:
                self.numState = [[0, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0]]
            elif self.isKey:
                self.numState = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0]]
        
        elif self.is_1_catch_box == True and self.is_2_catch_box == True and self.box_pos[0] >= 5 and self.box_pos[0] <= 6 and self.box_pos[1] >= 10 and self.box_pos[1] <= 13:
            if not self.isKey:
                self.numState = [[0, 1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0]]

        elif self.is_1_catch_box == True and self.is_2_catch_box == False and self.box_pos == [10, 7]:
            self.numState = [[0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]  # Agent1 Glued, Agent2 Free

        elif self.is_1_catch_box == False and self.is_2_catch_box == True and self.box_pos == [10, 7]:
            self.numState = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]  # Aent1 Free, Agent2 Glued

        elif self.box_pos == [1, 7]:    # global optiomal
            self.numState = [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]]  # Agent1 Delivered, Agent2 Delivered
        
        return [[[reward]]*self.num_agent, [done]*self.num_agent, [{}]*self.num_agent]

    def get_global_obs(self):
        obs = np.ones((15, 15, 3))
        for i in range(15):
            for j in range(15):
                if self.raw_occupancy[i, j] == 1:
                    obs[i, j, 0] = 0.0
                    obs[i, j, 1] = 0.0
                    obs[i, j, 2] = 0.0
        obs[self.agt1_pos[0], self.agt1_pos[1], 0] = 1
        obs[self.agt1_pos[0], self.agt1_pos[1], 1] = 0
        obs[self.agt1_pos[0], self.agt1_pos[1], 2] = 0

        obs[self.agt2_pos[0], self.agt2_pos[1], 0] = 0
        obs[self.agt2_pos[0], self.agt2_pos[1], 1] = 0
        obs[self.agt2_pos[0], self.agt2_pos[1], 2] = 1

        obs[self.box_pos[0], self.box_pos[1], 0] = 0
        obs[self.box_pos[0], self.box_pos[1], 1] = 1
        obs[self.box_pos[0], self.box_pos[1], 2] = 0
        return obs

    def get_key(self):
        im = OffsetImage(self.key_image, zoom=0.04)
        ab = AnnotationBbox(im, (11, 8), xycoords='data', frameon=False)
        return ab

    def get_agt1_obs(self):
        obs = np.zeros((3, 3, 3))
        for i in range(3):
            for j in range(3):
                if self.raw_occupancy[self.agt1_pos[0] - 1 + i][self.agt1_pos[1] - 1 + j] == 0:
                    obs[i, j, 0] = 1.0
                    obs[i, j, 1] = 1.0
                    obs[i, j, 2] = 1.0
                d_x = self.agt2_pos[0] - self.agt1_pos[0]
                d_y = self.agt2_pos[1] - self.agt1_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1 + d_x, 1 + d_y, 0] = 0.0
                    obs[1 + d_x, 1 + d_y, 1] = 0.0
                    obs[1 + d_x, 1 + d_y, 2] = 1.0
                d_x = self.box_pos[0] - self.agt1_pos[0]
                d_y = self.box_pos[1] - self.agt1_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1 + d_x, 1 + d_y, 0] = 0.0
                    obs[1 + d_x, 1 + d_y, 1] = 1.0
                    obs[1 + d_x, 1 + d_y, 2] = 0.0
        obs[1, 1, 0] = 1.0
        obs[1, 1, 1] = 0.0
        obs[1, 1, 2] = 0.0
        return obs

    def get_agt2_obs(self):
        obs = np.zeros((3, 3, 3))
        for i in range(3):
            for j in range(3):
                if self.raw_occupancy[self.agt2_pos[0] - 1 + i][self.agt2_pos[1] - 1 + j] == 0:
                    obs[i, j, 0] = 1.0
                    obs[i, j, 1] = 1.0
                    obs[i, j, 2] = 1.0
                d_x = self.agt1_pos[0] - self.agt2_pos[0]
                d_y = self.agt1_pos[1] - self.agt2_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1 + d_x, 1 + d_y, 0] = 1.0
                    obs[1 + d_x, 1 + d_y, 1] = 0.0
                    obs[1 + d_x, 1 + d_y, 2] = 0.0
                d_x = self.box_pos[0] - self.agt2_pos[0]
                d_y = self.box_pos[1] - self.agt2_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1 + d_x, 1 + d_y, 0] = 0.0
                    obs[1 + d_x, 1 + d_y, 1] = 1.0
                    obs[1 + d_x, 1 + d_y, 2] = 0.0
        obs[1, 1, 0] = 0.0
        obs[1, 1, 1] = 0.0
        obs[1, 1, 2] = 1.0
        return obs

    def get_state(self):
        state = np.zeros((1, 6))
        state[0, 0] = self.agt1_pos[0] / 15
        state[0, 1] = self.agt1_pos[1] / 15
        state[0, 2] = self.agt2_pos[0] / 15
        state[0, 3] = self.agt2_pos[1] / 15
        state[0, 4] = self.box_pos[0] / 15
        state[0, 5] = self.box_pos[1] / 15
        return state

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
        fig = plt.figure(figsize=(5, 5))
        gs = GridSpec(2, 2, figure=fig)
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[1, 1])
        ax4 = fig.add_subplot(gs[0, 1])
        ax1.imshow(self.get_global_obs())
        plt.xticks([])
        plt.yticks([])
        ax2.imshow(self.get_agt1_obs())
        plt.xticks([])
        plt.yticks([])
        ax3.imshow(self.get_agt2_obs())
        plt.xticks([])
        plt.yticks([])
        ax4.imshow(self.occupancy)
        plt.xticks([])
        plt.yticks([])

        if self.isKey:
            ax1.add_artist(self.get_key())

        plt.show()

    def render(self):
        obs = np.ones((15 * 20, 15 * 20, 3))
        for i in range(15):
            for j in range(15):
                if self.raw_occupancy[i, j] == 1:
                    cv2.rectangle(obs, (j*20, i*20), (j*20+20, i*20+20), (0, 0, 0), -1)
        cv2.rectangle(obs, (self.agt1_pos[1] * 20, self.agt1_pos[0] * 20), (self.agt1_pos[1] * 20 + 20, self.agt1_pos[0] * 20 + 20), (0, 0, 255), -1)
        cv2.rectangle(obs, (self.agt2_pos[1] * 20, self.agt2_pos[0] * 20), (self.agt2_pos[1] * 20 + 20, self.agt2_pos[0] * 20 + 20), (255, 0, 0), -1)
        cv2.rectangle(obs, (self.box_pos[1] * 20, self.box_pos[0] * 20),
                      (self.box_pos[1] * 20 + 20, self.box_pos[0] * 20 + 20), (0, 255, 0), -1)
        cv2.imshow('image', obs)
        cv2.waitKey(100)