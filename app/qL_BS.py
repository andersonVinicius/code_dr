#definir bibliotecas
from Bs import Bs
import numpy as np
import random
import operator
import matplotlib.pyplot as plt

def getMaxvaluesQ(state,q_table,switchDb):
    maxAllDict={}
    for i in switchDb:
        if i!='0db':
            id_position = np.where(q_table[state][i]==np.amax(q_table[state][i]))
            max_val = np.amax(q_table[state][i])
            maxAllDict.update({i:[id_position[0][0],max_val]})
    # print(maxAllDict)
    bs_action_id = max(maxAllDict.items(), key=operator.itemgetter(1))[1][0]
    switch_action = max(maxAllDict.items(), key=operator.itemgetter(1))[0]
    return [ switch_action,bs_action_id ]

# def getMaxvaluesR(r,switchDb):
#     maxAllDict={}
#     for i in switchDb:
#         if i!='0db':
#             id_position = np.where(r[i]==np.amax(r[i]))
#             max_val = np.amax(r[i])
#             maxAllDict.update({i:[id_position[0][0],max_val]})
#     print(maxAllDict)
#     #
#     value = max(maxAllDict.items(), key=operator.itemgetter(1))[1][1]
#     return value

def getR(r,action,switchDb):
   return r[action[0]][action[1]]

def getNewState(dict_statBs,action):
    return np.floor((dict_statBs[action[0]][action[1]] / 10)).astype(int)

def getMaxvaluesQNextState(state,q_table,switchDb):
    maxAllDict={}
    for i in switchDb:
        if i!='0db':
            id_position = np.where(q_table[state][i]==np.amax(q_table[state][i]))
            max_val = np.amax(q_table[state][i])
            maxAllDict.update({i:[id_position[0][0],max_val]})
    # print(maxAllDict)
    value = max(maxAllDict.items(), key=operator.itemgetter(1))[1][1]
    return value

#definir variaveis QL
num_episodes = 1000

learning_rate = 0.09
discount_rate = 0.99

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

n_act = 3
n_sta =  10


# r = np.random.randint(100, size=(10, 10))

#definir variaveis de entrada
#..quantidade BS
n_bs = 1
#..criar objeto BS
listBS = []

#..lista BS

# gerar cenarios ===============================================
# resultado inicial
# obter o nivel satisfacao especifico
switchDb = ['-15db','-10db','-5db','5db','10db','15db']
dict_statBs = {'nome':['bs0','bs1','bs2'],
               '-15db':np.array([30,25,15]),
               '-10db':np.array([32,45,25]),
               '-5db':np.array([45,45,28]),
                '5db':np.array([55,47,38]),
                '10db':np.array([55,47,38]),
                '15db':np.array([90,35,80])}
#===============================================================
##REWARD
Init_satis = 5
r={}
for i in switchDb:
    r[i] = np.floor((dict_statBs[i])).astype(int)

# [Bs0 Bs1 Bs2 ] x [-15 -10 -5 5 10 15]
dict_actions = {'nome':['bs0','bs1','bs2'],
                '-15db':np.array([0,0,0]),
                '-10db':np.array([0,0,0]),
                '-5db':np.array([0,0,0]),
                '5db':np.array([0,0,0]),
                '10db':np.array([0,0,0]),
                '15db':np.array([0,0,0])
        }

#criar tabela Q
q_table={}
for i in range(n_sta):
     q_table.update ({i:dict_actions})

list_epsForsteps = []
#processamento QL
#..iteracao por episodios
for i in range(num_episodes):
    print("Episodio --- ", i)
#...definir recompensa a cada novo episodio

    # state = random.uniform(0, n_act-1)
    #or
    state = Init_satis - 1
    n_steps=0
    key = True
#...iteracao passos por episodio
    while key == True:

        # Exploration-exploitation trade-off
        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = getMaxvaluesQ(state, q_table, switchDb)
        else:
            bs_action_id = random.randint(0, n_act-1)
            switch_action = switchDb[random.randint(0, len(switchDb)-1)]

            action = [switch_action,bs_action_id]

        rwd = getR(r, action, switchDb)
        new_state = getNewState(dict_statBs, action)
        nextStateMaxQvalue=getMaxvaluesQNextState(new_state, q_table, switchDb)


        #update q_table value
        q_table[state][action[0]][action[1]] = q_table[state][action[0]][action[1]] *\
                                                (1 - learning_rate) + learning_rate *\
                                                (rwd + discount_rate * nextStateMaxQvalue)

        state = new_state
        n_steps = n_steps + 1
        if state == 9:
            list_epsForsteps.append(n_steps)
            key = False

        # Exploration rate decay
        exploration_rate = min_exploration_rate + \
                           (max_exploration_rate - min_exploration_rate) *\
                           np.exp(-exploration_decay_rate * i)

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(list_epsForsteps)
ax.set_xlabel('Episodes')
ax.set_ylabel('Steps')
plt.show()

q_table












