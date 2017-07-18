import numpy as np
np.random.seed(1)
import tkinter as tk
import time
import serial
import sys
import time
voice_data_1 = 100
voice_data_2 = 100
voice_data_3 = 100
voice_data_4 = 100
voice_data_5 = 100
voice_data_6 = 120
UNIT = 40   # pixels
MAZE_H = 15# grid height
MAZE_W = 6 # grid width
class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()
    def _build_maze(self):
        global voice_data_1,voice_data_2,voice_data_3,voice_data_4,voice_data_5,voice_data_6
        vd1 = MAZE_H - int(voice_data_1 / 10)
        vd2 = MAZE_H - int(voice_data_2 / 10)
        vd3 = MAZE_H - int(voice_data_3 / 10)
        vd4 = MAZE_H - int(voice_data_4 / 10)
        vd5 = MAZE_H - int(voice_data_5 / 10)
        vd6 = MAZE_H - int(voice_data_6 / 10)
        vd_all = [vd1,vd2,vd3,vd4,vd5,vd6]
        vd_max = vd_all.index(min(vd_all))
        self.canvas = tk.Canvas(self, bg='green',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])
        # hell
        hell1_center = origin + np.array([UNIT*0 , UNIT * vd1])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        hell2_center = origin + np.array([UNIT*1, UNIT * vd2 ])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')
        hell3_center = origin + np.array([UNIT*2, UNIT * vd3 ])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell3_center[1] + 15,
            fill='black')
        hell4_center = origin + np.array([UNIT*3, UNIT * vd4 ])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 15, hell4_center[1] - 15,
            hell4_center[0] + 15, hell4_center[1] + 15,
            fill='black')
        hell5_center = origin + np.array([UNIT*4, UNIT * vd5 ])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 15, hell5_center[1] - 15,
            hell5_center[0] + 15, hell5_center[1] + 15,
            fill='black')
        hell6_center = origin + np.array([UNIT*5, UNIT * vd6 ])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 15, hell6_center[1] - 15,
            hell6_center[0] + 15, hell6_center[1] + 15,
            fill='black')
        """
        hell7_center = origin + np.array([UNIT*1, UNIT*0 ])
        self.hell7 = self.canvas.create_rectangle(
            hell7_center[0] - 15, hell7_center[1] - 15,
            hell7_center[0] + 15, hell7_center[1] + 15,
            fill='black')
        hell8_center = origin + np.array([UNIT*2, UNIT*0 ])
        self.hell8 = self.canvas.create_rectangle(
            hell8_center[0] - 15, hell8_center[1] - 15,
            hell8_center[0] + 15, hell8_center[1] + 15,
            fill='black')
        hell9_center = origin + np.array([UNIT*4, UNIT*0 ])
        self.hell9 = self.canvas.create_rectangle(
            hell9_center[0] - 15, hell9_center[1] - 15,
            hell9_center[0] + 15, hell9_center[1] + 15,
            fill='black')
        """
        # create oval
        oval1_center = origin + np.array([UNIT * vd_max, UNIT * 12])
        self.oval1 = self.canvas.create_oval(
            oval1_center[0] - 15, oval1_center[1] - 15,
            oval1_center[0] + 15, oval1_center[1] + 15,
            fill='yellow')
        # create oval
        oval_center = origin + np.array([UNIT * vd_max, UNIT* 11])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')
        oval2_center = origin + np.array([UNIT * vd_max, UNIT* 10])
        self.oval2 = self.canvas.create_oval(
            oval2_center[0] - 15, oval2_center[1] - 15,
            oval2_center[0] + 15, oval2_center[1] + 15,
            fill='yellow')
        oval3_center = origin + np.array([UNIT * vd_max, UNIT* 9])
        self.oval3 = self.canvas.create_oval(
            oval3_center[0] - 15, oval3_center[1] - 15,
            oval3_center[0] + 15, oval3_center[1] + 15,
            fill='yellow')
        oval4_center = origin + np.array([UNIT * vd_max, UNIT* 8])
        self.oval4 = self.canvas.create_oval(
            oval4_center[0] - 15, oval4_center[1] - 15,
            oval4_center[0] + 15, oval4_center[1] + 15,
            fill='yellow')
        oval5_center = origin + np.array([UNIT * vd_max, UNIT* 7])
        self.oval5 = self.canvas.create_oval(
            oval5_center[0] - 15, oval5_center[1] - 15,
            oval5_center[0] + 15, oval5_center[1] + 15,
            fill='yellow')
        # create red rect
        
        rect_center = origin + np.array([UNIT*0,UNIT*14])
        self.rect = self.canvas.create_rectangle(
            rect_center[0] - 15, rect_center[1] - 15,
            rect_center[0] + 15, rect_center[1] + 15,
            fill='red')
        
         # create red rect
        rect1_center = origin + np.array([UNIT*1,UNIT*14])
        self.rect1 = self.canvas.create_rectangle(
            rect1_center[0] - 15, rect1_center[1] - 15,
            rect1_center[0] + 15, rect1_center[1] + 15,
            fill='blue')
        
        rect2_center = origin + np.array([UNIT*2,UNIT*14])
        self.rect2 = self.canvas.create_rectangle(
            rect2_center[0] - 15, rect2_center[1] - 15,
            rect2_center[0] + 15, rect2_center[1] + 15,
            fill='white')
        
        rect3_center = origin + np.array([UNIT*3,UNIT*14])
        self.rect3 = self.canvas.create_rectangle(
            rect3_center[0] - 15, rect3_center[1] - 15,
            rect3_center[0] + 15, rect3_center[1] + 15,
            fill='blue')
        rect4_center = origin + np.array([UNIT*4,UNIT*14])
        self.rect4 = self.canvas.create_rectangle(
            rect4_center[0] - 15, rect4_center[1] - 15,
            rect4_center[0] + 15, rect4_center[1] + 15,
            fill='blue')
        rect5_center = origin + np.array([UNIT*5,UNIT*14])
        self.rect5 = self.canvas.create_rectangle(
            rect5_center[0] - 15, rect5_center[1] - 15,
            rect5_center[0] + 15, rect5_center[1] + 15,
            fill='blue')
        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        rect_center = origin + np.array([UNIT*0,UNIT*14])
        self.rect = self.canvas.create_rectangle(
            rect_center[0] - 15, rect_center[1] - 15,
            rect_center[0] + 15, rect_center[1] + 15,
            fill='red')
        # return observation
        return self.canvas.coords(self.rect)
    def reset1(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect1)
        origin = np.array([20,20])
        rect1_center = origin + np.array([UNIT*1,UNIT*14])
        self.rect1 = self.canvas.create_rectangle(
            rect1_center[0] - 15, rect1_center[1] - 15,
            rect1_center[0] + 15, rect1_center[1] + 15,
            fill='blue')
        return self.canvas.coords(self.rect1)
    def reset2(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect2)
        origin = np.array([20,20])
        rect2_center = origin + np.array([UNIT*2,UNIT*14])
        self.rect2 = self.canvas.create_rectangle(
            rect2_center[0] - 15, rect2_center[1] - 15,
            rect2_center[0] + 15, rect2_center[1] + 15,
            fill='white')
        return self.canvas.coords(self.rect2)
    def reset3(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect3)
        origin = np.array([20,20])
        rect3_center = origin + np.array([UNIT*3,UNIT*14])
        self.rect3 = self.canvas.create_rectangle(
            rect3_center[0] - 15, rect3_center[1] - 15,
            rect3_center[0] + 15, rect3_center[1] + 15,
            fill='blue')
        return self.canvas.coords(self.rect3)
    def reset4(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect4)
        origin = np.array([20,20])
        rect4_center = origin + np.array([UNIT*4,UNIT*14])
        self.rect4 = self.canvas.create_rectangle(
            rect4_center[0] - 15, rect4_center[1] - 15,
            rect4_center[0] + 15, rect4_center[1] + 15,
            fill='blue')
        return self.canvas.coords(self.rect4)
    def reset5(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect5)
        origin = np.array([20,20])
        rect5_center = origin + np.array([UNIT*5,UNIT*14])
        self.rect5 = self.canvas.create_rectangle(
            rect5_center[0] - 15, rect5_center[1] - 15,
            rect5_center[0] + 15, rect5_center[1] + 15,
            fill='blue')
        return self.canvas.coords(self.rect5)
    def step(self, action):
        global A
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt.append(2)
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt.append(3)
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
            if s_ == self.canvas.coords(self.oval):
                A = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                #A = 1
            if s_ == self.canvas.coords(self.oval1):
                A = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                #A = 2
            if s_ == self.canvas.coords(self.oval2):
                A = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                #A = 3
            if s_ == self.canvas.coords(self.oval3):
                A = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
            if s_ == self.canvas.coords(self.oval4):
                A = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
            if s_ == self.canvas.coords(self.oval5):
                A = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
                
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect1),self.canvas.coords(self.rect2),
                    self.canvas.coords(self.rect3),self.canvas.coords(self.rect4),self.canvas.coords(self.rect5),self.canvas.coords(self.oval),
                    self.canvas.coords(self.ova1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.ova4),
                    self.canvas.coords(self.ova5 )]:
            reward = -1
            
            done = True
        else:
            reward = 0
        
            done = False

        return s_, reward, done 
    def step1(self,action):
        global A
        global B
        """
        if A == [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
            #B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2)]
            B = self.canvas.coords(self.oval)
        elif A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
            #B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2)]
            B = self.canvas.coords(self.oval1)
        elif A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
            #B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1)]
            B = self.canvas.coords(self.oval2)
        elif A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
            B = self.canvas.coords(self.oval3)
        elif A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]:
            B = self.canvas.coords(self.oval4)
        elif A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]:
            B = self.canvas.coords(self.oval5)
            """
        s = self.canvas.coords(self.rect1)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt1.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt1.append(2)
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt1.append(3)
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt1.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect1, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect1)  # next state

        # reward function
        if s_ in A:
            """
            if A == [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
                if s_ == self.canvas.coords(self.oval1):
                    B = [self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval2):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval3):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval4):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval5):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
            if A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
                if s_ == self.canvas.coords(self.oval):
                    B = [self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval2):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval3):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval4):
                    B == [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval5):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
            if A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
                if s_ == self.canvas.coords(self.oval):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval1):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval3):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval4):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval5):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
            if A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
                if s_ == self.canvas.coords(self.oval):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval1):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if c_ == self.canvas.coords(self.oval2):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]
                if c_ == self.canvas.coords(self.oval4):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval5)]
                if c_ == self.canvas.coords(self.oval5):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4)]
            if A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]:
                if s_ == self.canvas.coords(self.oval):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval1):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval2):
                    B == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval3):
                    B == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval5)]
                if s_ == self.canvas.coords(self.oval5):
                    B == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3)]
            if A == [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]:
                if s_ == self.canvas.coords(self.oval):
                    B = [self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
                if s_ == self.canvas.coords(self.oval1):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
                if s_ == self.canvas.coords(self.oval2):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval3),self.canvas.coords(self.oval4)]
                if s_ == self.canvas.coords(self.oval3):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval4)]
                if s_ == self.canvas.coords(self.oval4):
                    B = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3)]
                    """
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect2),self.canvas.coords(self.rect3),
                    self.canvas.coords(self.rect4),self.canvas.coords(self.rect5),self.canvas.coords(self.oval),self.canvas.coords(self.oval1),
                    self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),self.canvas.coords(self.ova4),self.canvas.coords(self.oval5)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def step2(self,action):
        global B
##        F = [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2)]
        s = self.canvas.coords(self.rect2)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt2.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt2.append(2)
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt2.append(3)
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt2.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect2, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect2)  # next state

        # reward function
        if s_ == B:
            B ==  
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect3),self.canvas.coords(self.rect4),
                    self.canvas.coords(self.rect5),self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),
                    self.canvas.coords(self.oval3),self.canvas.coords(self.oval4),self.canvas.coords(self.oval5)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def render(self):
        time.sleep(0.1)
        self.update()       
    
