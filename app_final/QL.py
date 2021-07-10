

from Grid_space2 import Grid_space2
import operator
from RL_2 import Egreedy, SimpleQL, Sarsa
import numpy as np

class QL:
    # reward
    r = [-1, 1, 1000]  # yes wind - no_wind - no_windBest

    num_episodes = 500
    learning_rate = 0.9
    discount_rate = 0.5
    # create tab Q
    q_table = {}
    vetWind = [6.4, 6.74, 7.02, 7.27, 7.49, 7.69, 7.86, 8.02, 8.17, 8.31, 12.32]
    distanceSolo = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

    # number of grids or states
    # environmente dimensions
    xdim = 10  # meter
    ydim = 10  # meter
    zdim = 1  # meter

    N_blocks = (xdim * ydim * zdim)
    # start state
    init_space = int(xdim / 2)
    state_obj = int((xdim * ydim) - (xdim / 2))
    limitStoped = 500
    all_blocks = np.arange(N_blocks)
    n_sta = N_blocks
    env = []
    Egreedy = Egreedy
    Sarsa = Sarsa
    SimpleQL =  SimpleQL
    Grid_space2 =Grid_space2
    np = np
    exploration_rate = learning_rate
    max_exploration_rate = learning_rate
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.01

    # read = np.genfromtxt("/home/anderson/Dropbox/posGraduacao/doutorado/qualis_paper/dataS/seedDisponibles.csv",
    #                      delimiter=";").astype(int)
    seed = 1
    QLEgreedymatrixSteToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    QLSimplematrixSteToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    SarsamatrixSteToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)

    QLEgreedymatrixRWDToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    QLSimplematrixRWDToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    SarsamatrixRWDToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)

    QLEgreedymatrixDeltaToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    QLSimplematrixDeltaToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    SarsamatrixDeltaToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)

    def __init__(self,np):
         self.np = np

    # =====================================================================
    # Find Neighborhood===================================================
    def calNeighborhood(self, id, x, y):

        # z_space = (x*y)
        y_space = y
        x_space = 1
        z_point = 0

        left = (id - x_space) if ((id - x_space) >= 0) & (id % x != 0) else -1
        right = (id + x_space) if ((id + x_space) >= 0) & ((id + x_space) % x != 0) else -1
        up = (id + x) if (id + x) < (x * y) else -1
        down = (id - x) if ((id - x) >= 0) else -1

        leftUp = (up - x_space) if (up > -1) & (left > -1) else -1
        rightUp = (up + x_space) if (up > -1) & (right > -1) else -1
        rightDown = (down + x_space) if (down > -1) & (right > -1) else -1
        leftDown = (down - x_space) if (down > -1) & (left > -1) else -1
        actions = {  # "stoped":id,
            "left": left,
            "right": right,
            "up": up,
            "down": down,
            "leftUp": leftUp,
            "rightUp": rightUp,
            "rightDown": rightDown,
            "leftDown": leftDown
            # "front":front,
            # "back":back
        }
        return actions

    def creatEnv(self, seed):
        count = 0
        # print('Criando Ambiente')
        for y in range(self.ydim):
            for x in range(self.xdim):
                self.env.append(Grid_space2(count, x, x+1,
                                      y, y+1,
                                      self.calNeighborhood(count,self.xdim,self.ydim),
                                      self.r[1]))
                count = count+1

        # seed simule
        self.np.random.seed(seed)
        # print('Seed is:', seed)

        # Event wind==========================================================
        for i in range(self.xdim * self.ydim):
            id_rand = self.np.random.randint(len(self.vetWind))
            self.env[i].r = self.vetWind[10] - self.vetWind[id_rand]
            self.env[i].altura = self.distanceSolo[id_rand]
            self.env[i].windSpeed = self.vetWind[id_rand]

        # Find grid target =====================================================
        self.env[self.state_obj].r = self.r[2]

        # =================================================================================
        #                                   RL PROCESS
        # ==================================================================================
        # variables


        for i in range(self.n_sta):
            self.q_table.update({i: {  # str(i) + "stoped": 0,
                str(i) + "left": 0,
                str(i) + "right": 0,
                str(i) + "up": 0,
                str(i) + "down": 0,
                str(i) + "leftUp": 0,
                str(i) + "rightUp": 0,
                str(i) + "rightDown": 0,
                str(i) + "leftDown": 0
                    # str(i) + "front": 0,
                    # str(i) + "back": 0
                }})

        # print('Criou o Env!')


    def start_egreed(self):
        # print('Start process ql')
        # ======================================================================================
        # Q_learning e-greedy===================================================================
        # ======================================================================================
        # print('Iniciou o Q-Learning e-greedy')

        q_egr = self.Egreedy(self.num_episodes,
                        self.learning_rate,
                        self.discount_rate,
                        self.init_space,
                        self.q_table,
                        self.env,
                        self.r,
                        self.np,
                        self.exploration_rate,
                        self.max_exploration_rate,
                        self.min_exploration_rate,
                        self.exploration_decay_rate,
                        self.limitStoped,
                        self.state_obj)

        egreedy_q_table, egreedy_list_epsForsteps, \
        egreedy_rewards_all_episodes, egreedy_deltas = q_egr.start()

        # print('Terminou o processo de QL-egreedy!')
        return egreedy_q_table, egreedy_list_epsForsteps, \
        egreedy_rewards_all_episodes, egreedy_deltas

    def start_sarsa(self):
        sarsa = self.Sarsa(self.num_episodes,
                             self.learning_rate,
                             self.discount_rate,
                             self.init_space,
                             self.q_table,
                             self.env,
                             self.r,
                             self.np,
                             self.limitStoped,
                             self.state_obj)

        ss_q_table, ss_list_epsForsteps, \
        ss_rewards_all_episodes, ss_deltas = sarsa.start()

        # print('Terminou o processo de QL-egreedy!')
        return ss_q_table, ss_list_epsForsteps, \
               ss_rewards_all_episodes, ss_deltas
    def start_simpleQL(self):
        q_simple = self.SimpleQL(self.num_episodes,
                           self.learning_rate,
                           self.discount_rate,
                           self.init_space,
                           self.q_table,
                           self.env,
                           self.r,
                           self.np,
                           self.limitStoped,
                           self.state_obj)
        qs_q_table, qs_list_epsForsteps, \
        qs_rewards_all_episodes, qs_deltas = q_simple.start()

        return qs_q_table, qs_list_epsForsteps, \
        qs_rewards_all_episodes, qs_deltas


    def findPath(self,q_table,init_space,state_obj):
            st = init_space
            fail= False
            stp = 0
            storeSt = []
            storeSt.append(st)
            x = True
            p_obj = state_obj
            # print('saiu do:',st)
           # print('Objective:', p_obj)
            stAux = -1
            while x == True:
                act = max(q_table[st].items(), key=operator.itemgetter(1))[0].replace(str(st), '')
                st = self.env[st].actions[act]
                stp += 1

                # print(st)
                if st in storeSt:
                    fail= True
                    break
                storeSt.append(st)
                # print(storeSt)
                if stAux==st:
                    break


                if st == p_obj :
                    # print("seed target:",st)
                    #seedDisponible.append(s)

                    break
                stAux = st
            #print('quantity steps:', stp)
            #print('path to objective point:', storeSt)
            return storeSt, fail
