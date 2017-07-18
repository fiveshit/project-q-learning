import numpy as np
np.random.seed(1)
import tkinter as tk
import time
import serial
import sys
import time
##voice_data_1 = float()
##voice_data_2 = float()
##voice_data_3 = float()
##voice_data_4 = float()
##voice_data_5 = float()
##voice_data_6 = float()
UNIT = 40   # pixels
ENVIR_H = 10# grid heigh 
ENVIR_W = 6 # grid width
class ENVIR(tk.Tk, object):
    def __init__(self):
        super(ENVIR, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('ENVIR')
        self.geometry('{0}x{1}'.format(ENVIR_H * UNIT, ENVIR_H * UNIT))
##        self._build_ENVIR()
    def _build_ENVIR(self,A,B,C,D,E,F):
        vo1 = round(A / 10)
        vo2 = round(B / 10)
        vo3 = round(C / 10)
        vo4 = round(D / 10)
        vo5 = round(E / 10)
        vo6 = round(F / 10)
        vd1 = ENVIR_H - vo1
        vd2 = ENVIR_H - vo2
        vd3 = ENVIR_H - vo3
        vd4 = ENVIR_H - vo4
        vd5 = ENVIR_H - vo5
        vd6 = ENVIR_H - vo6
        mid1 = ENVIR_W/2 - 3
        mid2 = ENVIR_W/2 - 2
        mid3 = ENVIR_W/2 - 1
        mid4 = ENVIR_W/2 
        mid5 = ENVIR_W/2 + 1
        mid6 = ENVIR_W/2 + 2
        vd_all = [vd1,vd2,vd3,vd4,vd5,vd6]
        mid_all = [mid4,mid3,mid5,mid2,mid6,mid1]
        row = 0
##        if max(vd_all) > 12:
##            vd_all[vd_all.index(max(vd_all))] = -1
##        if min(vd_all) <= 0:
##            vd_all[vd_all.index(min(vd_all))] = -1
##        vd_max = vd_all.index(min(vd_all))+1
        for x in range(len(vd_all)):
            if vd_all[x] >= 9 or vd_all[x] <= 0:
                row += 1
                vd_all[vd_all.index(vd_all[x])] = -1
                if vd_all[vd_all.index(vd_all[x])] == -1:
                    if row == 1:
                        y = x
                        vd_max = y
                    if row == 2:
                        z = x
                        vd_max_1 = z
                    if row == 3:
                        w = x
                        vd_max_2 = w
                    if row == 4:
                        p = x
                        vd_max_3 = p
                    if row == 5:
                        o = x
                        vd_max_4 = o
        if row == 0:
            vd_max = vd_all.index(min(vd_all))+1
        self.canvas = tk.Canvas(self, bg='white',
                           height=ENVIR_H * UNIT,
                           width=ENVIR_W * UNIT)

        # create grids
        for c in range(0, ENVIR_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, ENVIR_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, ENVIR_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, ENVIR_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])
        # hell
        hell1_center = origin + np.array([UNIT*mid1 , UNIT * (vd_all[0]-2)])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 20, hell1_center[1] - 20,
            hell1_center[0] + 20, hell1_center[1] + 20,
            fill='black')
        hell2_center = origin + np.array([UNIT*mid2, UNIT * (vd_all[1]-2)])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 20, hell2_center[1] - 20,
            hell2_center[0] + 20, hell2_center[1] + 20,
            fill='black')
        hell3_center = origin + np.array([UNIT*mid3, UNIT * (vd_all[2]-2)])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 20, hell3_center[1] - 20,
            hell3_center[0] + 20, hell3_center[1] + 20,
            fill='black')
        hell4_center = origin + np.array([UNIT*mid4, UNIT * (vd_all[3]-2)])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 20, hell4_center[1] - 20,
            hell4_center[0] + 20, hell4_center[1] + 20,
            fill='black')
        hell5_center = origin + np.array([UNIT*mid5, UNIT * (vd_all[4]-2)])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 20, hell5_center[1] - 20,
            hell5_center[0] + 20, hell5_center[1] + 20,
            fill='black')
        hell6_center = origin + np.array([UNIT*mid6, UNIT * (vd_all[5]-2)])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 20, hell6_center[1] - 20,
            hell6_center[0] + 20, hell6_center[1] + 20,
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
        if row == 0:
            oval_center = origin + np.array([UNIT * vd_max, UNIT *(vd_all[0]-1)])
            self.oval = self.canvas.create_rectangle(
                oval_center[0] - 20, oval_center[1] - 20,
                oval_center[0] + 20, oval_center[1] + 20,
                fill='yellow')
            # create oval
            oval1_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval1 = self.canvas.create_rectangle(
                oval1_center[0] - 20, oval1_center[1] - 20,
                oval1_center[0] + 20, oval1_center[1] + 20,
                fill='yellow')
            oval2_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval2 = self.canvas.create_rectangle(
                oval2_center[0] - 20, oval2_center[1] - 20,
                oval2_center[0] + 20, oval2_center[1] + 20,
                fill='white')
            oval3_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval3 = self.canvas.create_rectangle(
                oval3_center[0] - 20, oval3_center[1] - 20,
                oval3_center[0] + 20, oval3_center[1] + 20,
                fill='white')
            oval4_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval4 = self.canvas.create_rectangle(
                oval4_center[0] - 20, oval4_center[1] - 20,
                oval4_center[0] + 20, oval4_center[1] + 20,
                fill='white')
##            oval5_center = origin + np.array([UNIT * vd_max, UNIT* 7])
##            self.oval5 = self.canvas.create_rectangle(
##                oval5_center[0] - 20, oval5_center[1] - 20,
##                oval5_center[0] + 20, oval5_center[1] + 20,
##                fill='white')
##            # create red rect
            
        if row == 1:
            # create oval
            oval_center = origin + np.array([UNIT * vd_max, UNIT *(vd_all[0]-1)])
            self.oval = self.canvas.create_rectangle(
                oval_center[0] - 20, oval_center[1] - 20,
                oval_center[0] + 20, oval_center[1] + 20,
                fill='yellow')
            # create oval
            oval1_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval1 = self.canvas.create_rectangle(
                oval1_center[0] - 20, oval1_center[1] - 20,
                oval1_center[0] + 20, oval1_center[1] + 20,
                fill='yellow')
            oval2_center = origin + np.array([UNIT * vd_max, UNIT* (vd_all[0]-1)])
            self.oval2 = self.canvas.create_rectangle(
                oval2_center[0] - 20, oval2_center[1] - 20,
                oval2_center[0] + 20, oval2_center[1] + 20,
                fill='white')
            oval3_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval3 = self.canvas.create_rectangle(
                oval3_center[0] - 20, oval3_center[1] - 20,
                oval3_center[0] + 20, oval3_center[1] + 20,
                fill='white')
            oval4_center = origin + np.array([UNIT * vd_max, UNIT* (vd_all[0]-1)])
            self.oval4 = self.canvas.create_rectangle(
                oval4_center[0] - 20, oval4_center[1] - 20,
                oval4_center[0] + 20, oval4_center[1] + 20,
                fill='white')
##            oval5_center = origin + np.array([UNIT * vd_max, UNIT* 7])
##            self.oval5 = self.canvas.create_rectangle(
##                oval5_center[0] - 20, oval5_center[1] - 20,
##                oval5_center[0] + 20, oval5_center[1] + 20,
##                fill='white')
##            # create red rect
        if row == 2:
            # create oval
            oval1_center = origin + np.array([UNIT * vd_max_1, UNIT *(vd_all[0]-1)])
            self.oval1 = self.canvas.create_rectangle(
                oval1_center[0] - 20, oval1_center[1] - 20,
                oval1_center[0] + 20, oval1_center[1] + 20,
                fill='yellow')
            # create ova
            oval_center = origin + np.array([UNIT * vd_max, UNIT*(vd_all[0]-1)])
            self.oval = self.canvas.create_rectangle(
                oval_center[0] - 20, oval_center[1] - 20,
                oval_center[0] + 20, oval_center[1] + 20,
                fill='yellow')
            oval2_center = origin + np.array([UNIT * vd_max_1, UNIT* (vd_all[0]-1)])
            self.oval2 = self.canvas.create_rectangle(
                oval2_center[0] - 20, oval2_center[1] - 20,
                oval2_center[0] + 20, oval2_center[1] + 20,
                fill='white')
            oval3_center = origin + np.array([UNIT * vd_max_1, UNIT* (vd_all[0]-1)])
            self.oval3 = self.canvas.create_rectangle(
                oval3_center[0] - 20, oval3_center[1] - 20,
                oval3_center[0] + 20, oval3_center[1] + 20,
                fill='white')
            oval4_center = origin + np.array([UNIT * vd_max_1, UNIT* (vd_all[0]-1)])
            self.oval4 = self.canvas.create_rectangle(
                oval4_center[0] - 20, oval4_center[1] - 20,
                oval4_center[0] + 20, oval4_center[1] + 20,
                fill='white')
##            oval5_center = origin + np.array([UNIT * vd_max, UNIT* 8])
##            self.oval5 = self.canvas.create_rectangle(
##                oval5_center[0] - 20, oval5_center[1] - 20,
##                oval5_center[0] + 20, oval5_center[1] + 20,
##                fill='white')
        if row == 3:
            oval1_center = origin + np.array([UNIT * vd_max, UNIT *(vd_all[0]-1)])
            self.oval1 = self.canvas.create_rectangle(
                oval1_center[0] - 20, oval1_center[1] - 20,
                oval1_center[0] + 20, oval1_center[1] + 20,
                fill='yellow')
            # create ova
            oval_center = origin + np.array([UNIT * vd_max_1, UNIT*(vd_all[0]-1)])
            self.oval = self.canvas.create_rectangle(
                oval_center[0] - 20, oval_center[1] - 20,
                oval_center[0] + 20, oval_center[1] + 20,
                fill='yellow')
            oval2_center = origin + np.array([UNIT * vd_max_2, UNIT* (vd_all[0]-1)])
            self.oval2 = self.canvas.create_rectangle(
                oval2_center[0] - 20, oval2_center[1] - 20,
                oval2_center[0] + 20, oval2_center[1] + 20,
                fill='white')
            oval3_center = origin + np.array([UNIT * vd_max_2, UNIT* (vd_all[0]-1)])
            self.oval3 = self.canvas.create_rectangle(
                oval3_center[0] - 20, oval3_center[1] - 20,
                oval3_center[0] + 20, oval3_center[1] + 20,
                fill='white')
            oval4_center = origin + np.array([UNIT * vd_max_2, UNIT* (vd_all[0]-1)])
            self.oval4 = self.canvas.create_rectangle(
                oval4_center[0] - 20, oval4_center[1] - 20,
                oval4_center[0] + 20, oval4_center[1] + 20,
                fill='white')
        if row == 4:
            oval1_center = origin + np.array([UNIT * vd_max, UNIT *(vd_all[0]-1)])
            self.oval1 = self.canvas.create_rectangle(
                oval1_center[0] - 20, oval1_center[1] - 20,
                oval1_center[0] + 20, oval1_center[1] + 20,
                fill='yellow')
            # create ova
            oval_center = origin + np.array([UNIT * vd_max_1, UNIT*(vd_all[0]-1)])
            self.oval = self.canvas.create_rectangle(
                oval_center[0] - 20, oval_center[1] - 20,
                oval_center[0] + 20, oval_center[1] + 20,
                fill='yellow')
            oval2_center = origin + np.array([UNIT * vd_max_2, UNIT* (vd_all[0]-1)])
            self.oval2 = self.canvas.create_rectangle(
                oval2_center[0] - 20, oval2_center[1] - 20,
                oval2_center[0] + 20, oval2_center[1] + 20,
                fill='white')
            oval3_center = origin + np.array([UNIT * vd_max_3, UNIT* (vd_all[0]-1)])
            self.oval3 = self.canvas.create_rectangle(
                oval3_center[0] - 20, oval3_center[1] - 20,
                oval3_center[0] + 20, oval3_center[1] + 20,
                fill='white')
            oval4_center = origin + np.array([UNIT * vd_max_3, UNIT* (vd_all[0]-1)])
            self.oval4 = self.canvas.create_rectangle(
                oval4_center[0] - 20, oval4_center[1] - 20,
                oval4_center[0] + 20, oval4_center[1] + 20,
                fill='white')
        if row == 5:
            oval1_center = origin + np.array([UNIT * vd_max, UNIT *(vd_all[0]-1)])
            self.oval1 = self.canvas.create_rectangle(
                oval1_center[0] - 20, oval1_center[1] - 20,
                oval1_center[0] + 20, oval1_center[1] + 20,
                fill='yellow')
            # create ova
            oval_center = origin + np.array([UNIT * vd_max_1, UNIT*(vd_all[0]-1)])
            self.oval = self.canvas.create_rectangle(
                oval_center[0] - 20, oval_center[1] - 20,
                oval_center[0] + 20, oval_center[1] + 20,
                fill='yellow')
            oval2_center = origin + np.array([UNIT * vd_max_2, UNIT* (vd_all[0]-1)])
            self.oval2 = self.canvas.create_rectangle(
                oval2_center[0] - 20, oval2_center[1] - 20,
                oval2_center[0] + 20, oval2_center[1] + 20,
                fill='white')
            oval3_center = origin + np.array([UNIT * vd_max_3, UNIT* (vd_all[0]-1)])
            self.oval3 = self.canvas.create_rectangle(
                oval3_center[0] - 20, oval3_center[1] - 20,
                oval3_center[0] + 20, oval3_center[1] + 20,
                fill='white')
            oval4_center = origin + np.array([UNIT * vd_max_4, UNIT* (vd_all[0]-1)])
            self.oval4 = self.canvas.create_rectangle(
                oval4_center[0] - 20, oval4_center[1] - 20,
                oval4_center[0] + 20, oval4_center[1] + 20,
                fill='white')
        
        rect_center = origin + np.array([UNIT*mid1,UNIT*(ENVIR_H -1)])
        self.rect = self.canvas.create_rectangle(
            rect_center[0] - 20, rect_center[1] - 20,
            rect_center[0] + 20, rect_center[1] + 20,
            fill='red')
        
         # create red rect
        rect1_center = origin + np.array([UNIT*mid2,UNIT*(ENVIR_H -1)])
        self.rect1 = self.canvas.create_rectangle(
            rect1_center[0] - 20, rect1_center[1] - 20,
            rect1_center[0] + 20, rect1_center[1] + 20,
            fill='blue')
        
        rect2_center = origin + np.array([UNIT*mid3,UNIT*(ENVIR_H -1)])
        self.rect2 = self.canvas.create_rectangle(
            rect2_center[0] - 20, rect2_center[1] - 20,
            rect2_center[0] + 20, rect2_center[1] + 20,
            fill='pink')
        
        rect3_center = origin + np.array([UNIT*mid4,UNIT*(ENVIR_H -1)])
        self.rect3 = self.canvas.create_rectangle(
            rect3_center[0] - 20, rect3_center[1] - 20,
            rect3_center[0] + 20, rect3_center[1] + 20,
            fill='green')
        rect4_center = origin + np.array([UNIT*mid5,UNIT*(ENVIR_H -1)])
        self.rect4 = self.canvas.create_rectangle(
            rect4_center[0] - 20, rect4_center[1] - 20,
            rect4_center[0] + 20, rect4_center[1] + 20,
            fill='purple')
        rect5_center = origin + np.array([UNIT*mid6,UNIT*(ENVIR_H -1)])
        self.rect5 = self.canvas.create_rectangle(
            rect5_center[0] - 20, rect5_center[1] - 20,
            rect5_center[0] + 20, rect5_center[1] + 20,
            fill='orange')
        # pack all
        self.canvas.pack()
        return mid_all
    def reset(self):
        self.update()
##        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        rect_center = origin + np.array([UNIT*0,UNIT*(ENVIR_H -1)])
        self.rect = self.canvas.create_rectangle(
            rect_center[0] - 20, rect_center[1] - 20,
            rect_center[0] + 20, rect_center[1] + 20,
            fill='red')
        # return observation
        return self.canvas.coords(self.rect)
    def reset1(self):
        self.update()
##        time.sleep(0.5)
        self.canvas.delete(self.rect1)
        origin = np.array([20,20])
        rect1_center = origin + np.array([UNIT*1,UNIT*(ENVIR_H -1)])
        self.rect1 = self.canvas.create_rectangle(
            rect1_center[0] - 20, rect1_center[1] - 20,
            rect1_center[0] + 20, rect1_center[1] + 20,
            fill='blue')
        return self.canvas.coords(self.rect1)
    def reset2(self):
        self.update()
##        time.sleep(0.5)
        self.canvas.delete(self.rect2)
        origin = np.array([20,20])
        rect2_center = origin + np.array([UNIT*2,UNIT*(ENVIR_H -1)])
        self.rect2 = self.canvas.create_rectangle(
            rect2_center[0] - 20, rect2_center[1] - 20,
            rect2_center[0] + 20, rect2_center[1] + 20,
            fill='pink')
        return self.canvas.coords(self.rect2)
    def reset3(self):
        self.update()
##        time.sleep(0.5)
        self.canvas.delete(self.rect3)
        origin = np.array([20,20])
        rect3_center = origin + np.array([UNIT*3,UNIT*(ENVIR_H -1)])
        self.rect3 = self.canvas.create_rectangle(
            rect3_center[0] - 20, rect3_center[1] - 20,
            rect3_center[0] + 20, rect3_center[1] + 20,
            fill='green')
        return self.canvas.coords(self.rect3)
    def reset4(self):
        self.update()
##        time.sleep(0.5)
        self.canvas.delete(self.rect4)
        origin = np.array([20,20])
        rect4_center = origin + np.array([UNIT*4,UNIT*(ENVIR_H -1)])
        self.rect4 = self.canvas.create_rectangle(
            rect4_center[0] - 20, rect4_center[1] - 20,
            rect4_center[0] + 20, rect4_center[1] + 20,
            fill='purple')
        return self.canvas.coords(self.rect4)
    def reset5(self):
        self.update()
##        time.sleep(0.5)
        self.canvas.delete(self.rect5)
        origin = np.array([20,20])
        rect5_center = origin + np.array([UNIT*5,UNIT*(ENVIR_H -1)])
        self.rect5 = self.canvas.create_rectangle(
            rect5_center[0] - 20, rect5_center[1] - 20,
            rect5_center[0] + 20, rect5_center[1] + 20,
            fill='orange')
        return self.canvas.coords(self.rect5)
    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt.append(2)
            if s[1] < (ENVIR_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt.append(3)
            if s[0] < (ENVIR_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4)]:
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect1),self.canvas.coords(self.rect2),
                    self.canvas.coords(self.rect3),self.canvas.coords(self.rect4),self.canvas.coords(self.rect5)]:
            reward = -1
            
            done = True
        else:
            reward = 0
        
            done = False

        return s_, reward, done 
    def step1(self,action):
        s = self.canvas.coords(self.rect1)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt1.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt1.append(2)
            if s[1] < (ENVIR_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt1.append(3)
            if s[0] < (ENVIR_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt1.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect1, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect1)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4)]:
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect),self.canvas.coords(self.rect2),
                  self.canvas.coords(self.rect3),self.canvas.coords(self.rect4),self.canvas.coords(self.rect5)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def step2(self,action):
        s = self.canvas.coords(self.rect2)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt2.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt2.append(2)
            if s[1] < (ENVIR_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt2.append(3)
            if s[0] < (ENVIR_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt2.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect2, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect2)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4)]:
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect),self.canvas.coords(self.rect1),
                    self.canvas.coords(self.rect3),self.canvas.coords(self.rect4),self.canvas.coords(self.rect5)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def step3(self,action):
        s = self.canvas.coords(self.rect3)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt2.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt2.append(2)
            if s[1] < (ENVIR_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt2.append(3)
            if s[0] < (ENVIR_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt2.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect3, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect3)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4)]:
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect),self.canvas.coords(self.rect1),
                    self.canvas.coords(self.rect2),self.canvas.coords(self.rect4),self.canvas.coords(self.rect5)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def step4(self,action):
        s = self.canvas.coords(self.rect4)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt2.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt2.append(2)
            if s[1] < (ENVIR_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt2.append(3)
            if s[0] < (ENVIR_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt2.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect4, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect4)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4)]:
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect),self.canvas.coords(self.rect1),
                    self.canvas.coords(self.rect2),self.canvas.coords(self.rect3),self.canvas.coords(self.rect5)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def step5(self,action):
        s = self.canvas.coords(self.rect5)
        base_action = np.array([0, 0])
        if action == 0:   # up
            #lt2.append(1)
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            #lt2.append(2)
            if s[1] < (ENVIR_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            #lt2.append(3)
            if s[0] < (ENVIR_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            #lt2.append(4)
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect5, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect5)  # next state

        # reward function
        if s_ in [self.canvas.coords(self.oval),self.canvas.coords(self.oval1),self.canvas.coords(self.oval2),self.canvas.coords(self.oval3),
                  self.canvas.coords(self.oval4)]:
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),
                    self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.rect),self.canvas.coords(self.rect1),
                    self.canvas.coords(self.rect2),self.canvas.coords(self.rect3),self.canvas.coords(self.rect4)]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False    
        return s_, reward,done
    def render(self):
##        time.sleep(0.01)
        self.update()
##    def rfcomm0(self):
##    ##    lock.acquire()
##        port0 = '/dev/rfcomm1'
##        ser = serial.Serial(port0,115200,timeout=2)
##        chr_open = 'a'
##        cmd = (str(chr_open).encode('utf-8'))
##        ser.write(cmd)
##        ser.open
##        voice_data_1 = float(ser.readline(2))
##        print('robot_1 sensor average value:',voice_data_1)
##        #c = (int(s).encode('utf-8'))
##    ##    lock.release()
##        ser.flushInput()
##        #ser.close()
##        return voice_data_1
##    def rfcomm1(self):
##    ##    lock.acquire()
##        port1 = '/dev/rfcomm2'
##        ser = serial.Serial(port1,115200,timeout=2)
##        chr_open = 97
##        cmd = (chr(chr_open).encode('utf-8'))
##        ser.write(cmd)
##        ser.open
##        voice_data_2 = float(ser.readline(2))
##        print('robot_2 sensor average value:',voice_data_2)
##    ##    lock.release()
##        ser.flushInput()
##        #ser.close()
##        return voice_data_2
##    def rfcomm2(self):
##    ##    lock.acquire()
##        port2 = '/dev/rfcomm3'
##        ser = serial.Serial(port2,115200,timeout=2)
##        chr_open = 97
##        cmd = (chr(chr_open).encode('utf-8'))
##        ser.write(cmd)
##        ser.open
##        voice_data_3 = float(ser.readline(2))
##        print('robot_3 sensor average value:',voice_data_3)
##    ##    lock.release()
##        ser.flushInput()
##        #ser.close()
##        return voice_data_3
##    def rfcomm3(self):
##    ##    lock.acquire()
##        port3 = '/dev/rfcomm4'
##        ser = serial.Serial(port3,115200,timeout=2)
##        chr_open = 97
##        cmd = (chr(chr_open).encode('utf-8'))
##        ser.write(cmd)
##        ser.open
##        voice_data_4 = float(ser.readline(2))
##        print('robot_4 sensor average value:',voice_data_4)
##    ##    lock.release()
##        ser.flushInput()
##        #ser.close()
##        return voice_data_4
##    def rfcomm4(self):
##    ##    lock.acquire()
##        port4 = '/dev/rfcomm5'
##        ser = serial.Serial(port4,115200,timeout=2)
##        chr_open = 97
##        cmd = (chr(chr_open).encode('utf-8'))
##        ser.write(cmd)
##        ser.open
##        voice_data_5 = float(ser.readline(2))
##        print('robot_5 sensor average value:',voice_data_5)
##    ##    lock.release()
##        ser.flushInput()
##        #ser.close()
##        return voice_data_5
##    def rfcomm5(self):
##    ##    lock.acquire()
##        port5 = '/dev/rfcomm6'
##        ser = serial.Serial(port5,115200,timeout=2)
##        chr_open = 97
##        cmd = (chr(chr_open).encode('utf-8'))
##        ser.write(cmd)
##        ser.open
##        voice_data_6 = float(ser.readline(2))
##        print('robot_6 sensor average value:',voice_data_6)
##    ##    lock.release()
##        ser.flushInput()
##        #ser.close()
##        return voice_data_6
##
##        
##
##        
