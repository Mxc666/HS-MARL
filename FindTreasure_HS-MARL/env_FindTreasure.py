import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from gym import spaces
# import cv2

class EnvFindTreasure(object):
    def __init__(self, map_size):
        self.map_size = map_size
        if map_size<7:
            self.map_size = 7

        self.half_pos = int((self.map_size - 1)/2)

        self.occupancy = np.zeros((self.map_size, self.map_size))
        for i in range(self.map_size):
            self.occupancy[0, i] = 1
            self.occupancy[i, 0] = 1
            self.occupancy[i, self.map_size - 1] = 1
            self.occupancy[self.map_size - 1, i] = 1
            self.occupancy[self.half_pos, i] = 1
        
        self.lever_pos = [self.map_size - 2, self.map_size - 2]

        self.agt1_pos = [self.half_pos+1, 1]
        self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1

        self.agt2_pos = [self.map_size-2, 1]
        self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1

        self.treasure_pos = [1, self.map_size - 2]
        # self.treasure_pos = [self.half_pos - 1, self.half_pos]

        # sub pos = [self.map_size - 2, self.map_size - 2]
        self.sub_pos = [self.map_size - 3, self.map_size - 2]


        self.num_agent = 2  # define the number of agent
        self.action_dim = 5  # define the action dimension of agent
        self.numState = [[1, 0, 0, 0, 0]] * self.num_agent  # All Free

        self.isTerminal = False
        self.isGlobal = False

    def reset(self):

        self.occupancy = np.zeros((self.map_size, self.map_size))
        for i in range(self.map_size):
            self.occupancy[0, i] = 1
            self.occupancy[i, 0] = 1
            self.occupancy[i, self.map_size - 1] = 1
            self.occupancy[self.map_size - 1, i] = 1
            self.occupancy[self.half_pos, i] = 1

        self.lever_pos = [self.map_size - 2, self.map_size - 2]

        self.agt1_pos = [self.half_pos + 1, 1]
        self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1

        self.agt2_pos = [self.map_size - 2, 1]
        self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1

        self.treasure_pos = [1, self.map_size - 2]
        # self.treasure_pos = [self.half_pos - 1, self.half_pos]

        # sub pos = [self.map_size - 2, self.map_size - 2]
        self.sub_pos = [self.map_size - 3, self.map_size - 2]

        self.numState = [[1, 0, 0, 0, 0]] * self.num_agent  # All Free
        self.isTerminal = False
        self.isGlobal = False

    def step(self, action_list):
        reward = 0
        bad_n = 0
        # agent1 move
        if action_list[0] == 0:  # move up
            if self.occupancy[self.agt1_pos[0]-1][self.agt1_pos[1]] != 1:  # if can move
                self.agt1_pos[0] = self.agt1_pos[0] - 1
                self.occupancy[self.agt1_pos[0]+1][self.agt1_pos[1]] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        elif action_list[0] == 1:  # move down
            if self.occupancy[self.agt1_pos[0]+1][self.agt1_pos[1]] != 1:  # if can move
                self.agt1_pos[0] = self.agt1_pos[0]+1
                self.occupancy[self.agt1_pos[0]-1][self.agt1_pos[1]] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        elif action_list[0] == 2:  # move left
            if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]-1] != 1:  # if can move
                self.agt1_pos[1] = self.agt1_pos[1] - 1
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]+1] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        elif action_list[0] == 3:  # move right
            if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]+1] != 1:  # if can move
                self.agt1_pos[1] = self.agt1_pos[1] + 1
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]-1] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        
        ##########################################################################################
        # agent2 move
        if action_list[1] == 0:  # move up
            if self.occupancy[self.agt2_pos[0]-1][self.agt2_pos[1]] != 1:  # if can move
                self.agt2_pos[0] = self.agt2_pos[0] - 1
                self.occupancy[self.agt2_pos[0]+1][self.agt2_pos[1]] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        elif action_list[1] == 1:  # move down
            if self.occupancy[self.agt2_pos[0]+1][self.agt2_pos[1]] != 1:  # if can move
                self.agt2_pos[0] = self.agt2_pos[0] + 1
                self.occupancy[self.agt2_pos[0]-1][self.agt2_pos[1]] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        elif action_list[1] == 2:  # move left
            if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]-1] != 1:  # if can move
                self.agt2_pos[1] = self.agt2_pos[1] - 1
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]+1] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1
        elif action_list[1] == 3:  # move right
            if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]+1] != 1:  # if can move
                self.agt2_pos[1] = self.agt2_pos[1] + 1
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]-1] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward = reward - 0.1
                bad_n += 1

        # check lever
        if self.agt1_pos == self.lever_pos or self.agt2_pos == self.lever_pos:
            self.occupancy[self.half_pos][self.half_pos] = 0  # open secret door
            self.occupancy[self.half_pos][self.half_pos-1] = 0  # open secret door
            self.occupancy[self.half_pos][self.half_pos+1] = 0  # open secret door
        else:
            self.occupancy[self.half_pos][self.half_pos] = 1  # close secret door
            self.occupancy[self.half_pos][self.half_pos - 1] = 1  # close secret door
            self.occupancy[self.half_pos][self.half_pos + 1] = 1  # close secret door

        # check treasure
        if self.agt1_pos == self.treasure_pos or self.agt2_pos == self.treasure_pos:
            reward = reward + 100
            self.isGlobal = True

        if (self.agt1_pos == self.sub_pos and self.agt2_pos == self.lever_pos) or (self.agt1_pos == self.lever_pos and self.agt2_pos == self.sub_pos):
            reward = reward + 3

        done = False
        if reward > 0:
            done = True
            self.isTerminal = True

        # r1 Free (Not Pass Mid), r2 At Lever
        if (self.agt1_pos[0] > self.half_pos) and (self.agt1_pos != self.sub_pos) and (self.agt2_pos == self.lever_pos):
            self.numState = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]

        # r1 PassMid, r2 At Lever
        elif (self.agt1_pos[0] == self.half_pos) and (self.agt2_pos == self.lever_pos):
            self.numState = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 0]]

        # r1 At Lever, r2 Free (Not Pass Mid)
        elif (self.agt1_pos == self.lever_pos) and (self.agt2_pos[0] > self.half_pos) and (self.agt2_pos != self.sub_pos):
            self.numState = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]

        # r1 At Lever, r2 PassMid
        elif (self.agt1_pos == self.lever_pos) and (self.agt2_pos[0] == self.half_pos):
            self.numState = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0]]

        # r1 Up Part, r2 Any Pos (Not Local)
        elif (self.agt1_pos[0] < self.half_pos) and (self.agt1_pos != self.treasure_pos):
            self.numState = [[1, 0, 1, 1, 0], [1, 0, 0, 0, 0]]
        
        # r1 Get Treasure, r2 Any Pos (Not Local)
        elif (self.agt1_pos == self.treasure_pos):
            self.numState = [[0, 0, 0, 1, 1], [1, 0, 0, 0, 0]]

        # r2 Up Part, r1 Any Pos (Not Local)
        elif (self.agt2_pos[0] < self.half_pos) and (self.agt2_pos != self.treasure_pos):
            self.numState = [[1, 0, 0, 0, 0], [1, 0, 1, 1, 0]]

        # r2 Get Treasure, r1 Any Pos (Not Local)
        elif (self.agt2_pos == self.treasure_pos):
            self.numState = [[1, 0, 0, 0, 0], [0, 0, 0, 1, 1]]

        return [[[reward]]*self.num_agent, [done]*self.num_agent, [{}]*self.num_agent, [bad_n]]



    def get_global_obs(self):
        obs = np.zeros((self.map_size, self.map_size, 3))
        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.occupancy[i][j] == 0:
                    obs[i, j, 0] = 1.0
                    obs[i, j, 1] = 1.0
                    obs[i, j, 2] = 1.0

        obs[self.lever_pos[0], self.lever_pos[1], 0] = 1.0
        obs[self.lever_pos[0], self.lever_pos[1], 1] = 1.0
        obs[self.lever_pos[0], self.lever_pos[1], 2] = 0.0
        
        obs[self.treasure_pos[0], self.treasure_pos[1], 0] = 0.0
        obs[self.treasure_pos[0], self.treasure_pos[1], 1] = 1.0
        obs[self.treasure_pos[0], self.treasure_pos[1], 2] = 0.0

        obs[self.agt1_pos[0], self.agt1_pos[1], 0] = 1.0
        obs[self.agt1_pos[0], self.agt1_pos[1], 1] = 0.0
        obs[self.agt1_pos[0], self.agt1_pos[1], 2] = 0.0

        obs[self.agt2_pos[0], self.agt2_pos[1], 0] = 0.0
        obs[self.agt2_pos[0], self.agt2_pos[1], 1] = 0.0
        obs[self.agt2_pos[0], self.agt2_pos[1], 2] = 1.0

        obs[self.sub_pos[0], self.sub_pos[1], 0] = 1.0
        obs[self.sub_pos[0], self.sub_pos[1], 1] = 0.0
        obs[self.sub_pos[0], self.sub_pos[1], 2] = 1.0
        return obs

    def get_agt1_obs(self):
        obs = np.zeros((3, 3, 3))
        for i in range(3):
            for j in range(3):
                if self.occupancy[self.agt1_pos[0]-1+i][self.agt1_pos[1]-1+j] == 0:
                    obs[i, j, 0] = 1.0
                    obs[i, j, 1] = 1.0
                    obs[i, j, 2] = 1.0

                d_x = self.lever_pos[0] - self.agt1_pos[0]
                d_y = self.lever_pos[1] - self.agt1_pos[1]
                if d_x>=-1 and d_x<=1 and d_y>=-1 and d_y<=1:
                    obs[1+d_x, 1+d_y, 0] = 1.0
                    obs[1+d_x, 1+d_y, 1] = 1.0
                    obs[1+d_x, 1+d_y, 2] = 0.0

                d_x = self.treasure_pos[0] - self.agt1_pos[0]
                d_y = self.treasure_pos[1] - self.agt1_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1+d_x, 1+d_y, 0] = 0.0
                    obs[1+d_x, 1+d_y, 1] = 1.0
                    obs[1+d_x, 1+d_y, 2] = 0.0

                d_x = self.agt2_pos[0] - self.agt1_pos[0]
                d_y = self.agt2_pos[1] - self.agt1_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1: 
                    obs[1 + d_x, 1 + d_y, 0] = 0.0
                    obs[1 + d_x, 1 + d_y, 1] = 0.0
                    obs[1 + d_x, 1 + d_y, 2] = 1.0

        obs[1, 1, 0] = 1.0
        obs[1, 1, 1] = 0.0
        obs[1, 1, 2] = 0.0
        return obs

    def get_agt2_obs(self):
        obs = np.zeros((3, 3, 3))
        for i in range(3):
            for j in range(3):
                if self.occupancy[self.agt2_pos[0]-1+i][self.agt2_pos[1]-1+j] == 0:
                    obs[i, j, 0] = 1.0
                    obs[i, j, 1] = 1.0
                    obs[i, j, 2] = 1.0

                d_x = self.lever_pos[0] - self.agt2_pos[0]
                d_y = self.lever_pos[1] - self.agt2_pos[1]
                if d_x>=-1 and d_x<=1 and d_y>=-1 and d_y<=1:
                    obs[1+d_x, 1+d_y, 0] = 1.0
                    obs[1+d_x, 1+d_y, 1] = 1.0
                    obs[1+d_x, 1+d_y, 2] = 0.0

                d_x = self.treasure_pos[0] - self.agt2_pos[0]
                d_y = self.treasure_pos[1] - self.agt2_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1+d_x, 1+d_y, 0] = 0.0
                    obs[1+d_x, 1+d_y, 1] = 1.0
                    obs[1+d_x, 1+d_y, 2] = 0.0
                    
                d_x = self.agt1_pos[0] - self.agt2_pos[0]
                d_y = self.agt1_pos[1] - self.agt2_pos[1]
                if d_x >= -1 and d_x <= 1 and d_y >= -1 and d_y <= 1:
                    obs[1 + d_x, 1 + d_y, 0] = 1.0
                    obs[1 + d_x, 1 + d_y, 1] = 0.0
                    obs[1 + d_x, 1 + d_y, 2] = 0.0

        obs[1, 1, 0] = 0.0
        obs[1, 1, 1] = 0.0
        obs[1, 1, 2] = 1.0
        return obs

    def get_state(self):
        state = np.zeros((1, 4))
        state[0, 0] = self.agt1_pos[0] / self.map_size
        state[0, 1] = self.agt1_pos[1] / self.map_size
        state[0, 2] = self.agt2_pos[0] / self.map_size
        state[0, 3] = self.agt2_pos[1] / self.map_size
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
        gs = GridSpec(3, 2, figure=fig)
        ax1 = fig.add_subplot(gs[0:2, 0:2])
        plt.xticks([])
        plt.yticks([])
        ax2 = fig.add_subplot(gs[2, 0:1])
        plt.xticks([])
        plt.yticks([])
        ax3 = fig.add_subplot(gs[2, 1:2])
        plt.xticks([])
        plt.yticks([])

        ax1.imshow(self.get_global_obs())
        ax2.imshow(self.get_agt1_obs())
        ax3.imshow(self.get_agt2_obs())

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
                if obs[i][j][0] == 1.0 and obs[i][j][1] == 1.0 and obs[i][j][2] == 0.0:
                    cv2.rectangle(new_obs, (j * enlarge, i * enlarge), (j * enlarge + enlarge, i * enlarge + enlarge), (0, 255, 255), -1)
                if obs[i][j][0] == 1.0 and obs[i][j][1] == 0.0 and obs[i][j][2] == 1.0:
                    cv2.rectangle(new_obs, (j * enlarge, i * enlarge), (j * enlarge + enlarge, i * enlarge + enlarge), (255, 0, 255), -1)
        cv2.imshow('image', new_obs)
        cv2.waitKey(100)
