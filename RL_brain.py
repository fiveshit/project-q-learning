import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class QLearningTable:
    def __init__(self, actions, learning_rate=1, reward_decay=0.9, e_greedy=0.9,status = 0,counter = 0,
                 counter1 = 0, counter2 = 0, counter3 = 0, counter4 = 0, counter5 = 0, lt = [], lt1 = [],
                 lt2 = [], lt3 = [], lt4 = [], lt5 = [], iterations = 0, iterations_next = 0):
        self.actions = actions  # a list
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions)
        self.status = status
        self.counter = counter
        self.counter1 = counter1
        self.counter2 = counter2
        self.counter3 = counter3
        self.counter4 = counter4
        self.counter5 = counter5
        self.lt = lt
        self.lt1 = lt1
        self.lt2 = lt2
        self.lt3 = lt3
        self.lt4 = lt4
        self.lt5 = lt5
        self.iterations = iterations
        self.iterations_next = iterations_next
    def choose_action(self, observation):
        self.check_state_exist(observation)
        # action selection
        if np.random.uniform() < self.epsilon:
            # choose best action
            state_action = self.q_table.ix[observation, :]
            state_action = state_action.reindex(np.random.permutation(state_action.index))     # some actions have same value
            action = state_action.argmax()
        else:
            # choose random action
            action = np.random.choice(self.actions)
        return action
    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.ix[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.ix[s_, :].max()  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table.ix[s, a] += self.lr * (q_target - q_predict)  # update
##        if r == 1:
##            self.iterations += 1
##            plt.plot([self.iterations,self.iterations_next],[(q_predict - q_target)**2,self.Q_table],color='black',lw=1.5)
##            self.iterations_next = self.iterations
##            self.Q_table = (q_predict - q_target)**2
##            plt.xlabel('iterations')
##            plt.ylabel('errors')
##            plt.yticks([0.01,0.1,1])
        return self.q_table
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )
       
