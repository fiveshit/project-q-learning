from envir import ENVIR
from RL_brain import QLearningTable
import threading
import time
import matplotlib.pyplot as plt
from ble_rf import Rfcomm
import numpy as np
##import pymongo
import pandas as pd
##connection = pymongo.MongoClient("localhost",27017)
##tdb = connection.RL_data1
##post_info = tdb.test

T = Rfcomm()
##fig = plt.figure()
##ax = fig.add_subplot(1,1,1)
def update():
    mid = env._build_ENVIR(vo1,vo2,vo3,vo4,vo5,vo6)
##    mid = env._build_ENVIR(50,50,50,50,180,50)
##    print(mid)
    print('Algorithm start')
    for A in range(6):
        print(A)
        if mid[A] == 0.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            episode_low = 0
            for episode in range(1000):
                        # initial observation
                observation = env.reset()
                while True:
                            # fresh env
                    env.render()

                            # RL choose action based on observation
                    action = RL.choose_action(str(observation))
                    RL.lt.append(action)
                            # RL take action and get next observation and reward
                    observation_, reward, done = env.step(action)

                            # RL learn from this transition
                    table = RL.learn(str(observation), action, reward, str(observation_))
                        
                            # swap observation
                    observation = observation_

                            #count episode
                    episode_next = episode
                    episode_count += 1

                            # break while loop when end of this episode
                    if reward == 1:
##                        plt.subplot(231)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='red',lw=1.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
                                # min path
                        if episode_low >= count_lt:
                                # convergence
                            if episode_low == count_lt:
                                RL.counter += 1
                            episode_low = len(RL.lt)
                        episode_low = count_lt
                                
                        if RL.counter >= 10:
                            break
                    if done:
                        if RL.counter >= 10:
                            break
                        del RL.lt[:]
                        break
                if RL.counter >= 10:
##                    print('learning is over1')
                    print('robot_1 path:',RL.lt)
##                    table.to_csv('data.csv')
                    break

        if mid[A] == 1.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            episode_low1 = 0
            for episode in range(1000):
                # initial observation
                observation = env.reset1()
                while True:
                    # fresh env
                    env.render()

                    # RL choose action based on observation
                    action = RL1.choose_action(str(observation))
                    RL1.lt1.append(action)
                    # RL take action and get next observation and reward
                    observation_, reward, done  = env.step1(action)


                    # RL learn from this transition
                    table1 = RL1.learn(str(observation), action, reward, str(observation_))

                    # swap observation
                    observation = observation_

                    #count episode
                    episode_next = episode
                    episode_count += 1

                    # break while loop when end of this episode
                    if reward == 1:
##                        plt.subplot(232)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='blue',lw=1.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
                        if episode_low1 >= count_lt:
                            if episode_low1 == count_lt:
                                RL1.counter1 += 1
                            episode_low1 = len(RL.lt1)
                        episode_low1 = count_lt
                        if RL1.counter1 >= 10:
                            break
                    if done:
                        if RL1.counter1 >= 10:
                            break
                        del RL1.lt1[:]
                        break
                if RL1.counter1 >= 10:
##                    print('learning is over2')
                    print('robot_2 path:',RL1.lt1)
##                    table1.to_csv('data1.csv')
                    break
        if mid[A] == 2.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            episode_low2 = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset2()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL2.choose_action(str(observation))
                        
                    RL2.lt2.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step2(action)

                        # RL learn from this transition
                    table2 = RL2.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_
                        #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
##                        plt.subplot(233)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='pink',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
                        if episode_low2 >= count_lt:
                            if episode_low2 == count_lt:
                                RL2.counter2 += 1
                            episode_low2 = len(RL.lt2)
                        episode_low2 = count_lt
                        if RL2.counter2 >= 10:
                            break
                    if done:
                        if RL2.counter2 >= 10:
                            break
                        del RL2.lt2[:]
                        break
                if RL2.counter2 >= 10:
##                    print('learning is over3')
                    print('robot_3 path:',RL2.lt2)
##                    table2.to_csv('data2.csv')
                    break
        if mid[A] == 3.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            episode_low3 = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset3()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL3.choose_action(str(observation))
                        
                    RL3.lt3.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step3(action)

                        # RL learn from this transition
                    table3 = RL3.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_
                        #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
##                        plt.subplot(234)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='green',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
                        if episode_low3 >= count_lt:
                            if episode_low3 == count_lt:
                                RL3.counter3 += 1
                            episode_low3 = len(RL.lt3)
                        episode_low3 = count_lt
                        if RL3.counter3 >= 10:
                            break
                    if done:
                        if RL3.counter3 >= 10:
                            break
                        del RL3.lt3[:]
                        break
                if RL3.counter3 >= 10:
##                    print('learning is over4')
                    print('robot_4 path:',RL3.lt3)
##                    table3.to_csv('data3.csv')
                    break
        if mid[A] == 4.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            episode_low4 = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset4()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL4.choose_action(str(observation))
                        
                    RL4.lt4.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step4(action)

                        # RL learn from this transition
                    table4 = RL4.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_
                    #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
##                        plt.subplot(235)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='purple',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
                        if episode_low4 >= count_lt:
                            if episode_low4 == count_lt:
                                RL4.counter4 += 1
                            episode_low4 = len(RL.lt4)
                        episode_low4 = count_lt
                        if RL4.counter4 >= 10:
                            break
                    if done:
                        if RL4.counter4 >= 10:
                            break
                        del RL4.lt4[:]
                        break
                if RL4.counter4 >= 10:
##                    print('learning is over5')
                    print('robot_5 path:',RL4.lt4)
##                    table4.to_csv('data4.csv')
                    break
        if mid[A] == 5.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            episode_low5 = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset5()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL5.choose_action(str(observation))
                        
                    RL5.lt5.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step5(action)

                        # RL learn from this transition
                    table5 = RL5.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_

                    #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
##                        plt.subplot(236)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='orange',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
                        if episode_low5 >= count_lt:
                            if episode_low5 == count_lt:
                                RL5.counter5 += 1
                            episode_low5 = len(RL.lt5)
                        episode_low5 = count_lt
                        if RL5.counter5 >= 10:
                            break
                    if done:
                        if RL5.counter5 >= 10:
                            break
                        del RL5.lt5[:]
                        break
                if RL5.counter5 >= 10:
##                    print('learning is over6')
                    print('robot_6 path:',RL5.lt5)
##                    table5.to_csv('data5.csv')
                    break
            
    # end of game
    print('game over')
    T._Thread(RL.lt,RL1.lt1,RL2.lt2,RL3.lt3,RL4.lt4,RL5.lt5)
##plt.show()
def main(): 
    global env,RL,RL1,RL2,RL3,RL4,RL5
    env = ENVIR()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    RL1 = QLearningTable(actions=list(range(env.n_actions)))
    RL2 = QLearningTable(actions=list(range(env.n_actions)))
    RL3 = QLearningTable(actions=list(range(env.n_actions)))
    RL4 = QLearningTable(actions=list(range(env.n_actions)))
    RL5 = QLearningTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()
def _rfcomm():
    global vo1,vo2,vo3,vo4,vo5,vo6
##    vd1_ = en.rfcomm0()
##    vd2_ = en.rfcomm1()
##    vd3_ = en.rfcomm2()
##    vd4_ = en.rfcomm3()
##    vd5_ = en.rfcomm4()
##    vd6_ = en.rfcomm5()
    while(True):
        vo1,vo2,vo3,vo4,vo5,vo6 = T.rfcomm2robot()
        if [vo1,vo2,vo3,vo4,vo5,vo6] in list(range(15,25)):
            vo1 = T.rfcomm0(2)
            vo2 = T.rfcomm1(2)
            vo3 = T.rfcomm2(2)
            vo4 = T.rfcomm3(2)
            vo5 = T.rfcomm4(2)
            vo6 = T.rfcomm5(2)
            break
if __name__ == "__main__":
    _rfcomm()
    main()

