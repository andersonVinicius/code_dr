from Uavs import Uav
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from Grid_space import Grid_space
import operator
import random
import matplotlib.pyplot as plt
from RL import Egreedy,SimpleQL,Sarsa

#environmente dimensions
xdim = 20 #meter
ydim = 20 #meter
zdim = 20 #meter

#start state
init_space = 4210

limitStoped = 300

# uavVel = 20 # m/s

#reward
r = [-0.01,0,100] # yes wind - no_wind - no_windBest

num_episodes = 100
learning_rate = 0.9
discount_rate = 0.1
# create table Q

# number of grids or states
N_blocks = (xdim *ydim*zdim)
all_blocks = np.arange(N_blocks)
n_sta = N_blocks
env = []
count = 0
read=np.genfromtxt("/home/anderson/Dropbox/posGraduacao/doutorado/qualis_paper/dataS/seedDisponibles.csv",delimiter=";").astype(int)
seed = 1
QLEgreedymatrixSteToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)
QLSimplematrixSteToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)
SarsamatrixSteToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)

QLEgreedymatrixRWDToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)
QLSimplematrixRWDToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)
SarsamatrixRWDToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)

QLEgreedymatrixDeltaToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)
QLSimplematrixDeltaToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)
SarsamatrixDeltaToEP = np.zeros(shape=(seed, num_episodes+1), dtype=int)

#=====================================================================
# Find Neighborhood===================================================
def calNeighborhood(id,x,y,z,z_point):

    z_space = (x*y)
    y_space = y
    x_space = 1

    left =(id-x_space) if ((id-x_space)>=0) & (id%x!=0) else -1
    right =(id+x_space) if ((id+x_space)>=0) & ((id+x_space)%x!=0)  else -1
    up =   (id+y_space) if (id+y_space)<((x*y*z_point)+(x*y)) else -1
    down = (id-y_space) if ((id-y_space)>=0) else -1

    leftUp =   (up-x_space) if  (up>-1) & (left>-1) else -1
    rightUp =  (up+x_space) if (up>-1) & (right>-1) else -1
    rightDown =  (down+x_space)  if (down>-1) & (right>-1) else -1
    leftDown =  (down-x_space) if  (down>-1) & (left>-1) else -1

    front = (id+z_space) if (id+z_space)<(x*y*z) else -1
    back = (id-z_space) if (id-z_space)>=0 else -1

    actions = {"stoped":id,
              "left":left,
              "right":right,
              "up":up,
              "down":down,
              "leftUp":leftUp,
              "rightUp":rightUp,
              "rightDown":rightDown,
              "leftDown":leftDown,
              "front":front,
              "back":back
    }
    return actions

#=====================================================================
#                         CREATE ENV
#=====================================================================
for z in range(zdim):
    for y in range(ydim):
        for x in range(xdim):
            env.append(Grid_space(count, x, x+1,
                                      y, y+1, z, z+1,
                                      calNeighborhood(count,xdim,ydim,zdim,z),
                                      r[1]))
            count = count+1

for s in range(seed):
    # seed simule
    np.random.seed(read[s])
    print('Seed is:',read[s])

    #Event wind==========================================================
    BlockInterference = np.round(N_blocks*0.60).astype(int) # 10%
    windInterference = np.random.choice(range(N_blocks),
                                        BlockInterference, replace=False)
    blockWithoutWind = np.setdiff1d(all_blocks,windInterference)


    #Set wind Interference reward==========================================
    for i in windInterference:
        env[i].r = r[0]
    next = []

    ids_next=[]
    # Find grid target =====================================================
    for i in blockWithoutWind:
        if env[init_space].id != env[i].id:
            p1=np.array([env[init_space].x_init,
                         env[init_space].y_init,
                         env[init_space].z_init])
            p2=np.array([env[i].x_init,
                         env[i].y_init,
                         env[i].z_init])
            next.append( np.sqrt(np.sum((p1-p2)**2, axis=0)))
            ids_next.append(env[i].id)

    #target no wind Best
    env[ids_next[ np.argmin(next)]].r = r[2]

    # =================================================================================
    #                                   RL PROCESS
    #==================================================================================
    # variables


    # create tab Q
    q_table = {}
    for i in range(n_sta):
        q_table.update({i: {str(i) + "stoped": 0,
                            str(i) + "left": 0,
                            str(i) + "right": 0,
                            str(i) + "up": 0,
                            str(i) + "down": 0,
                            str(i) + "leftUp": 0,
                            str(i) + "rightUp": 0,
                            str(i) + "rightDown": 0,
                            str(i) + "leftDown": 0,
                            str(i) + "front": 0,
                            str(i) + "back": 0
                            }})
    #======================================================================================
    #Q_learning e-greedy===================================================================
    #======================================================================================
    exploration_rate = 1
    max_exploration_rate = 1
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.01

    q_egr = Egreedy(num_episodes,
          learning_rate,
          discount_rate,
          init_space,
          q_table,
          env,
          r,
          np,
          exploration_rate,
          max_exploration_rate,
          min_exploration_rate,
          exploration_decay_rate,
          limitStoped)

    egreedy_q_table, egreedy_list_epsForsteps,\
    egreedy_rewards_all_episodes, egreedy_deltas = q_egr.start()

    #======================================================================================
    #Simple QLearning======================================================================
    #======================================================================================
    q_simple = SimpleQL(num_episodes,
          learning_rate,
          discount_rate,
          init_space,
          q_table,
          env,
          r,
          np,
          limitStoped)

    qs_q_table, qs_list_epsForsteps,\
    qs_rewards_all_episodes, qs_deltas = q_simple.start()
    #=============================================================================
    #SARSA
    #=============================================================================
    sarsa = Sarsa(num_episodes,
          learning_rate,
          discount_rate,
          init_space,
          q_table,
          env,
          r,
          np,
          limitStoped)

    ss_q_table, ss_list_epsForsteps,\
    ss_rewards_all_episodes, ss_deltas = sarsa.start()
    # Steps x Episiodes===============================

    # Q- e-greedy
    # Simple Q-learning
    # Sarsa
    qle_eps = np.array(egreedy_list_epsForsteps)#Q- e-greedy
    qs_eps = np.array(qs_list_epsForsteps)
    ss_eps = np.array(ss_list_epsForsteps)

    QLEgreedymatrixSteToEP[s,0:len(qle_eps)] = qle_eps
    QLSimplematrixSteToEP[s,0:len(qs_eps)] = qs_eps
    SarsamatrixSteToEP[s,0:len(ss_eps)] = ss_eps
    #==================================================
    # Reward x Episiodes===============================
    qle_epsToRWD = np.array(egreedy_rewards_all_episodes)
    qs_epsToRWD = np.array(qs_rewards_all_episodes)
    ss_epsToRWD = np.array(ss_rewards_all_episodes)

    QLEgreedymatrixRWDToEP[s, 0:len(qle_epsToRWD)] = qle_epsToRWD
    QLSimplematrixRWDToEP[s, 0:len(qs_epsToRWD)] = qs_epsToRWD
    SarsamatrixRWDToEP[s, 0:len(ss_epsToRWD)] = ss_epsToRWD

    # ==================================================
    # DeltaQ x Episodes===============================
    qle_epsToDelta = np.array(egreedy_deltas)
    qs_epsToDelta = np.array(qs_deltas)
    ss_epsToDelta = np.array(ss_deltas)

    QLEgreedymatrixDeltaToEP[s, 0:len(qle_epsToDelta)] = qle_epsToDelta
    QLSimplematrixDeltaToEP[s, 0:len(qs_epsToDelta)] = qs_epsToDelta
    SarsamatrixDeltaToEP[s, 0:len(ss_epsToDelta)] = ss_epsToDelta

#================================================================
#                           SAVE
#================================================================
# Q- e-greedy-----------------------------
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/QLEgreedymatrixSteToEP.csv",QLEgreedymatrixSteToEP, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/QLEgreedymatrixRWDToEP.csv",QLEgreedymatrixRWDToEP, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/QLEgreedymatrixDeltaToEP.csv",QLEgreedymatrixDeltaToEP, delimiter=";")
# Simple Q-learning-----------------------
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/QLSimplematrixSteToEP.csv", QLSimplematrixSteToEP, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/QLSimplematrixRWDToEP.csv",QLSimplematrixRWDToEP, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/QLSimplematrixDeltaToEP.csv", QLSimplematrixDeltaToEP, delimiter=";")
# Sarsa----------------------------------
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/SarsamatrixSteToEP.csv", SarsamatrixSteToEP, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/SarsamatrixRWDToEP.csv", SarsamatrixRWDToEP, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/SarsamatrixDeltaToEP.csv",SarsamatrixDeltaToEP, delimiter=";")

#================================================================
#                           PLOT
#================================================================

#Steps x Episiodes===============================================
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(QLEgreedymatrixSteToEP.mean(0),label="QL e-greedy")
ax.plot(QLSimplematrixSteToEP.mean(0),label="simple QL ")
ax.plot(SarsamatrixSteToEP.mean(0),label="Sarsa")

ax.set_xlabel('Episodes')
ax.set_ylabel('AVG - Steps')
ax.legend()
# plt.xlim(0,80)
# plt.show()

#Acumulate reward===============================================
fig3, ax1 = plt.subplots(constrained_layout=True)

rec=0
meanQLEgreedymatrixRWDToEP = QLEgreedymatrixRWDToEP.mean(0)
meanQLSimplematrixRWDToEP = QLSimplematrixRWDToEP.mean(0)
meanSarsamatrixRWDToEP = SarsamatrixRWDToEP.mean(0)

addegreedy = []
addeSq = []
addSs = []
rec=0
for g in range(len(meanQLEgreedymatrixRWDToEP)):
    rec = meanQLEgreedymatrixRWDToEP[g] + rec
    addegreedy.append(rec)

rec=0
for g in range(len(meanQLSimplematrixRWDToEP)):
    rec = meanQLSimplematrixRWDToEP[g] + rec
    addeSq.append(rec)

rec=0
for g in range(len(meanSarsamatrixRWDToEP)):
    rec =meanSarsamatrixRWDToEP[g] + rec
    addSs.append(rec)

ax1.plot(addegreedy,label="QL e-greedy")
ax1.plot(addeSq,label="simple QL ")
ax1.plot(addSs,label="Sarsa")

ax1.set_xlabel('Episodes')
ax1.set_ylabel('AVG - Acumulate Reward')
ax1.legend()
# plt.xlim(0,300)
# plt.show()
#Delta Q========================================================
fig2, ax2 = plt.subplots(constrained_layout=True)
ax2.plot(QLEgreedymatrixDeltaToEP.mean(0),label="QL e-greedy")
ax2.plot(QLSimplematrixDeltaToEP.mean(0),label="simple QL ")
ax2.plot(SarsamatrixDeltaToEP.mean(0),label="Sarsa")

ax2.set_xlabel('Episodes')
ax2.set_ylabel('AVG - Delta Q')
ax2.legend()
# plt.xlim(0,500)
plt.show()