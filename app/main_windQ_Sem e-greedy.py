from Uavs import Uav
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from Grid_space import Grid_space
import operator
import random
import matplotlib.pyplot as plt

#create environmente
xdim = 20 #meter
ydim = 20 #meter
zdim = 20 #meter
# init_space = 63750
init_space = 4210
np.random.seed(9)

uavVel = 20 # m/s
list_grid = []
count = 0
N_blocks = (xdim *ydim*zdim)
all_blocks = np.arange(N_blocks)
#event wind==========================================================
BlockInterference = np.round(N_blocks*0.99).astype(int) # 10%
windInterference = np.random.choice(range(N_blocks), BlockInterference, replace=False)

blockWithoutWind = np.setdiff1d(all_blocks,windInterference)

# Find Neighborhood
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
r = [-1,10,100] # yes wind - no_wind - no_windBest

#create states===========================================================
for z in range(zdim):
    for y in range(ydim):
        for x in range(xdim):
                list_grid.append(Grid_space(count, x, x+1, y, y+1, z, z+1,
                                            calNeighborhood(count,xdim,
                                                            ydim,zdim,z),
                                            r[1]))
                count = count+1

# [list_grid[i].r= for i in windInterference]

for i in windInterference:
    list_grid[i].r = r[0]
next = []
ids_next=[]
for i in blockWithoutWind:
    if list_grid[init_space].id != list_grid[i].id:
        p1=np.array([list_grid[init_space].x_init,
                     list_grid[init_space].y_init,
                     list_grid[init_space].z_init])
        p2=np.array([list_grid[i].x_init, list_grid[i].y_init, list_grid[i].z_init])
        next.append( np.sqrt(np.sum((p1-p2)**2, axis=0)))
        ids_next.append(list_grid[i].id)

#target no wind Best
list_grid[ids_next[ np.argmin(next)]].r = r[2]


# =================================================================================
#                                   Q_LEARNING
#==================================================================================
aryLr = [0.9]
fig, ax = plt.subplots(constrained_layout=True)

#definir variaveis QL
for z in aryLr:
    num_episodes = 1000
    learning_rate = z
    discount_rate = 0.1
    n_act = 11
    n_sta =  N_blocks
    #criate tab Q
    q_table={}
    for i in range(n_sta):
         q_table.update ({i:{str(i)+"stoped":0,
                        str(i)+"left": 0,
                        str(i)+"right": 0,
                        str(i)+"up": 0,
                        str(i)+"down": 0,
                        str(i)+"leftUp": 0,
                        str(i)+"rightUp": 0,
                        str(i)+"rightDown": 0,
                        str(i)+"leftDown": 0,
                        str(i)+"front": 0,
                        str(i)+"back": 0
                         }})


    key = True
    list_epsForsteps = []

    #processamento QL =======================================================================================
    #..iteracao por episodios
    list_epsForsteps =[]
    rewards_all_episodes=[]
    deltas = []
    min_step = 99999999
    quantTime = 0
    i=0
    while i <=num_episodes:

        # state = np.random.randint(0, N_blocks)
        # print (state)
        state = init_space # init
        n_steps = 0
        rewards_current_episode=0
        key = True
        print("Episodio --- ", i)
        # ...Step to episodes

        biggest_change = 0
        while key == True:

            # # Exploration-exploitation trade-off
            # exploration_rate_threshold = np.random.uniform(0,1)
            # if exploration_rate_threshold > exploration_rate:
            #     actionsPossibles = []
            #     for x in list_grid[state].actions:
            #         if list_grid[state].actions[x] >= 0:
            #             actionsPossibles.append(x)
            #
            #     #get maximun value of the actions
            #     action = max(q_table[state].items(), key=operator.itemgetter(1))[0].replace(str(state),'')
            #     try:
            #         actionsPossibles[action]
            #     except:
            #         action = actionsPossibles[np.random.randint(0,len(actionsPossibles))]
            #     # print('caiu no if')
            # else:
            actionsPossibles = []
            # print('caiu no else')
            for x in list_grid[state].actions:
                if list_grid[state].actions[x] >= 0:
                    actionsPossibles.append(x)
            #choose random actions
            action = actionsPossibles[np.random.randint(0, len(actionsPossibles))]
            # print("random",action)


            new_state = list_grid[state].actions[action]
            # print('action: ',action)
            # print('new_state: ', new_state)
            nextStateMaxQvalue = max(q_table[new_state].items(), key=operator.itemgetter(1))[1]
            rwd = list_grid[new_state].r
            old_qsa= q_table[state][str(state)+action]


            # print(rwd)
            # UPDATE Q ========================================================================
            # q_table[state][str(state)+action] = q_table[state][str(state)+action] *\
            #                                     (1 - learning_rate) +( learning_rate *\
            #                                     (rwd + discount_rate * nextStateMaxQvalue))
            # q_table[state][str(state) + action] = q_table[state][str(state) + action] + \
            #                                       learning_rate * \
            #                                       (rwd + (discount_rate * \
            #                                               ( nextStateMaxQvalue - q_table[state][str(state) + action])))


            # if list_grid[state].r != r[2]  or list_grid[state].r != r[0]:
            if list_grid[state].r != r[2]  or list_grid[state].r != r[0]:
                q_target = rwd + learning_rate * nextStateMaxQvalue
            else:
                q_target = rwd

            q_table[state][str(state) + action] += discount_rate * (q_target - q_table[state][str(state) + action])

            # q_table[state][str(state) + action] = rwd + ( learning_rate * nextStateMaxQvalue)

            biggest_change = max(biggest_change, np.abs(old_qsa - q_table[state][str(state)+action]))
            state = new_state
            n_steps = n_steps + 1
            rewards_current_episode += rwd



            # if (list_grid[state].r == r[2] or list_grid[state].r == r[0] ) :
            if (list_grid[state].r == r[2]) :

               if (min_step<=n_steps):
                   n_steps = min_step
                   quantTime+=1
                   if quantTime>=50:
                       num_episodes=0

               else:
                   quantTime=0
                   min_step = n_steps

               print('steps :',n_steps)
               list_epsForsteps.append(n_steps)
               rewards_all_episodes.append(rewards_current_episode)
               deltas.append(biggest_change)
               break
                # key = False

            # # Exploration rate decay
            # exploration_rate = min_exploration_rate +\
            #                     (max_exploration_rate - min_exploration_rate) *\
            #                     np.exp(-exploration_decay_rate * i)
        i+=1
    # plt.plot(deltas)
    # plt.show()
    #
    ax.plot(list_epsForsteps,label="learning rate "+str(z))
    ax.set_xlabel('Episodes')
    ax.set_ylabel('Steps')
    ax.legend()

 # Calculate and print the average reward per thousand episodes
# rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes / 10)
# count = 10
print("********Average reward per thousand episodes********\n")
add=[]
# for r in rewards_per_thousand_episodes:
#
#     print(count, ": ", str(sum(r / 10)))
#     count += 10
# rec=0
# for g in range(len(rewards_all_episodes)):
#     rec = rewards_all_episodes[g] + rec
#     add.append(rec)
#
# plt.plot(add)
plt.show()
    # plt.hold(True)
    # print('')
#find best path
st = init_space
stp = 0
storeSt = []
x = True
p_obj = ids_next[np.argmin(next)]
print('Objective:',p_obj)

while x == True:
    act = max(q_table[st].items(), key=operator.itemgetter(1))[0].replace(str(st),'')
    st =  list_grid[st].actions[act]
    stp+=1
    storeSt.append(st)
    print(st)
    if st == ids_next[np.argmin(next)]:
        break
print( 'quantity steps:',stp )
print('path to objective point:',storeSt)
