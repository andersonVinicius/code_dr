import math
import operator
import numpy as np

from app_final.Grid_space2 import Grid_space2
from app_final.RL_2 import Egreedy, SimpleQL, Sarsa


class QL:
    # reward
     # yes wind - no_wind - TheBestPos
    # env = []

    # num_episodes = 1000
    # learning_rate = 0.9
    # discount_rate = 0.5
    # create tab Q

    # vetWind = [6.4, 6.74, 7.02, 7.27, 7.49, 7.69]
    # distanceSolo = [50, 60, 70, 80, 90, 100]

    # number of grids or states
    # environmente dimensions
    # xdim = 5  # dimensao eixo x
    # ydim = 5  # dimensao eixo y
    # zdim = 1  # dimensao eixo z

    # N_blocks = (xdim * ydim * zdim)
    # # start state
    # init_space = int(xdim / 2)
    # state_obj = int((xdim * ydim) - (xdim / 2))
    # limitStoped = 1000
    # all_blocks = np.arange(N_blocks)
    # n_sta = N_blocks


    # Egreedy = Egreedy
    # Sarsa = Sarsa
    # SimpleQL =  SimpleQL
    # Grid_space2 =Grid_space2
    # np = np
    # exploration_rate = learning_rate
    # max_exploration_rate = learning_rate
    # min_exploration_rate = 0.01
    # exploration_decay_rate = 0.01

    # QLEgreedymatrixSteToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    # QLSimplematrixSteToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    # SarsamatrixSteToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    #
    # QLEgreedymatrixRWDToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    # QLSimplematrixRWDToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    # SarsamatrixRWDToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    #
    # QLEgreedymatrixDeltaToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    # QLSimplematrixDeltaToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)
    # SarsamatrixDeltaToEP = np.zeros(shape=(seed, num_episodes + 1), dtype=int)

    # read = np.genfromtxt("/home/anderson/Dropbox/posGraduacao/doutorado/qualis_paper/dataS/seedDisponibles.csv",
    #                      delimiter=";").astype(int)

    def __init__(self, np, segm, seed, num_episodes, learning_rate, discount_rate):
        self.num_episodes = num_episodes
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.np = np
        self.xdim = segm
        self.ydim = segm
        self.init_space = int(self.xdim / 2)
        self.state_obj = int((self.xdim * self.ydim) - (self.xdim / 2))

        self.zdim = 1
        self.r = [-1, 1, 200]
        self.env = []
        self.q_table = {}
        self.vetWind = [6.4, 6.74, 7.02, 7.27, 7.49, 7.69, 7.86, 8.02, 8.17, 8.31, 12.32]
        self.distanceSolo = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

        self.N_blocks = (self.xdim * self.ydim * self.zdim)
        # start state
        self.init_space = int(self.xdim / 2)
        self.state_obj = int((self.xdim * self.ydim) - (self.xdim / 2))
        self.limitStoped = 1000
        self.all_blocks = np.arange(self.N_blocks)
        self.n_sta = self.N_blocks

        self.exploration_rate = 1
        self.max_exploration_rate = 1
        self.min_exploration_rate = 0.01
        self.exploration_decay_rate = 0.01

        self.creatEnv(seed)


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

    def calcule_distancia_entre_obstaculos_fixos(self, obst_fixed):
        dis_btw_obs_poin_current_position = []
        for i in range(len(self.env)):
            dis_btw_obs_poin_current_position = []
            for ob in obst_fixed:
                # math.sqrt((15 ** 2) + ((abs(dsolo[k] - dsolo[k + 1])) ** 2))
                dis_btw_obs_poin_current_position.append( {'id':ob, 'distancia':
                math.sqrt(abs(self.env[ob].x_init-self.env[i].x_init) +
                          abs(self.env[ob].y_init-self.env[i].y_init))
                }
                )
            self.env[i].dist_from_obs = dis_btw_obs_poin_current_position

    def calcular_distancia_para_o_taget(self):

        for i in range(len(self.env)):
            self.env[i].dist_from_target = \
                math.sqrt(abs(self.env[self.state_obj].x_init - self.env[i].x_init) +
                          abs(self.env[self.state_obj].y_init - self.env[i].y_init))

    def somar_distancia_entre_obstaculos_fixos(self, array):

        sum = 0
        for i in range(len(array)):
            if array[i]['distancia']>0:
                sum += (1/(array[i]['distancia'] * 15))

        return sum

    def calcula_diferenca_entre_pos_anteria_pos_atual_para_o_target(self, a, b, c, actions, target, obstaculos, dif_wind):
        act_label = ['left', 'right',
                     'up', 'down',
                     'leftUp', 'rightUp',
                     'rightDown', 'leftDown'
                     ]
        rwd_by_act = {}
        for act in act_label:
           if actions[act] >= 0:
            # {id do grid : valor da recompensa)
               rwd_by_act[str(actions[act])] = a * (self.env[actions[act]].dist_from_target - target) \
                                                - b * self.somar_distancia_entre_obstaculos_fixos(obstaculos)\
                                                + c * dif_wind

        return rwd_by_act

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

        # Event fixed obstacles ============================================
        if self.xdim == 5:
            obst_fixed = [11, 12, 13, 9]
        if self.xdim == 10:
            obst_fixed = [12, 17, 18, 22, 27, 28, 32, 43, 45, 46, 55, 78, 88]
        if self.xdim == 30:

            # obst_fixed = [835,834,805,804,775,774,745,744,726,715,714,710,696,685,684,680,666,650,636,620,619,618,617,609,608,607,606,439,438,437,
            #               436,435,434,433,432,431,425,424,423,405,404,403,402,401,395,365,335,311,310,281,280,265,264,263,262,261,235,225,205,195,175,156,155,145,126,125,]

            ## 1 x obstacle
            # obst_fixed = [467,466,465,464,463,437,433,407,406,405,404,403]

            # 2 x obstacle
            # obst_fixed = [467,466,465,464,463,437,433,407,406,405,404,403,226,225,224,223,222,196,195,194,193,192,]
            # Mult obstacles
            obst_fixed = [621,619,617,615,613,611,609,561,559,557,555,553,551,549,501,499,497,495,493,491,489,441,439,437,435,433,431,429,381,379,377,375,373,371,369,321,319,317,315,313,311,309,261,259,257,255,253,251,249]

        self.calcule_distancia_entre_obstaculos_fixos(obst_fixed)
        self.calcular_distancia_para_o_taget()
        # Event wind and obst ===============================================
        a = 1000
        b = 1
        c = 10
        wind_high_speed = [807,806,805,804,803,802,801,800,799,798,797,796,795,
                           777,776,775,774,773,772,771,770,769,768,767,766,765,
                           747,746,745,744,743,742,741,740,739,738,737,736,735,
                           717,716,715,714,713,712,711,710,709,708,707,706,705,
                           687,686,685,684,683,682,681,680,679,678,677,676,675,
                           657,656,655,654,653,652,651,650,649,648,647,646,645,
                           627,626,625,624,623,622,621,620,619,618,617,616,615,
                           597,596,595,594,593,592,591,590,589,588,587,586,585,
                           567,566,565,564,563,562,561,560,559,558,557,556,555,
                           537,536,535,534,533,532,531,530,529,528,527,526,525,507,506,505,504,503,
                           502,501,500,499,498,497,496,495,477,476,475,474,473,472,471,470,469,468,467,466,465,447,446,445,444,443,442,441,440,439,438,437,436,
                           435,417,416,415,414,413,412,411,410,409,408,407,406,405,387,386,385,384,383,382,381,380,379,378,377,376,375,357,356,355,354,353,352,
                           351,350,349,348,347,346,345,327,326,325,324,323,322,321,320,319,318,317,316,315,297,296,295,294,293,292,291,290,289,288,287,286,285,
                           267,266,265,264,263,262,261,260,259,258,257,256,255,237,236,235,234,233,232,231,230,229,228,227,226,225,207,206,205,204,203,202,201,
                           200,199,198,197,196,195,177,176,175,174,173,172,171,170,169,168,167,166,165,147,146,145,144,143,142,141,140,139,138,137,136,135,117,
                           116,115,114,113,112,111,110,109,108,107,106,105,87,86,85,84,83,82,81,80,79,78,77,76,75]
        for i in range(self.xdim * self.ydim):
            id_rand = self.np.random.randint(len(self.vetWind))
            self.env[i].obst_fixo = 0
            # self.env[i].r = self.vetWind[5] - self.vetWind[id_rand]
            self.env[i].altura = self.distanceSolo[id_rand]

            if i in wind_high_speed:
                self.env[i].windSpeed = self.vetWind[10]
            else:
                self.env[i].windSpeed = self.vetWind[id_rand]

            self.env[i].r = \
                self.calcula_diferenca_entre_pos_anteria_pos_atual_para_o_target(a, b, c, self.env[i].actions,
                                                                                           self.env[i].dist_from_target,
                                                                                           self.env[i].dist_from_obs,
                                                                                           (self.vetWind[10] - self.env[i].windSpeed )
                                                                                 )
        for ob in obst_fixed:
            self.env[ob].obst_fixo = 1
        # Defina
        # Find grid target =====================================================
        # self.env[self.state_obj].r = self.r[2]

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

        q_egr = Egreedy(self.num_episodes,
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
        sarsa = Sarsa(self.num_episodes,
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
        q_simple = SimpleQL(self.num_episodes,
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
