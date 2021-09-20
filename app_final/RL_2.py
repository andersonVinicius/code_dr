import operator
class Egreedy:

    # variables
    num_episodes = 1000
    learning_rate = 0.9
    discount_rate = 0.1
    q_table = {}
    init_space = 0
    r = []
    env={}
    np=0
    limitStoped = 0
    exploration_rate = 1
    max_exploration_rate = 1
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.01
    state_obj = 0

    # construtor UAV
    def __init__(self, num_episodes,learning_rate,
                 discount_rate,init_space,q_table,
                 env,r,np,exploration_rate,max_exploration_rate,
                 min_exploration_rate,exploration_decay_rate,limitStoped,state_obj):

                  self.exploration_rate = exploration_rate
                  self.max_exploration_rate = max_exploration_rate
                  self.min_exploration_rate = min_exploration_rate
                  self.exploration_decay_rate = exploration_decay_rate

                  self.num_episodes = num_episodes
                  self.learning_rate = learning_rate
                  self.discount_rate = discount_rate
                  self.init_space = init_space
                  self.q_table = q_table
                  self.r = r
                  self.env = env
                  self.np = np
                  self.limitStoped = limitStoped
                  self.state_obj = state_obj


    def start(self):

        #iteration for episode
        list_epsForsteps = []
        rewards_all_episodes = []
        deltas = []
        i = 0
        while i <= self.num_episodes:
            state = self.init_space  # init
            n_steps = 0
            rewards_current_episode = 0
            key = True
            # print("Episodio --- ", i)
            # ...Step to episodes
            biggest_change = 0

            while True:
                # Exploration-exploitation trade-off
                exploration_rate_threshold = self.np.random.uniform(0, 1)
                if exploration_rate_threshold > self.exploration_rate:
                    actionsPossibles = []
                    for x in self.env[state].actions:
                        if self.env[state].actions[x] >= 0:
                            actionsPossibles.append(x)

                    # get maximun value of the actions
                    action = max(self.q_table[state].items(), key=operator.itemgetter(1))[0].replace(str(state), '')
                    try:
                        actionsPossibles[action]
                    except:
                        action = actionsPossibles[self.np.random.randint(0, len(actionsPossibles))]
                    # print('caiu no if')
                else:
                    actionsPossibles = []
                    # print('caiu no else')
                    for x in self.env[state].actions:
                        if self.env[state].actions[x] >= 0:
                            actionsPossibles.append(x)
                    # choose random actions
                    action = actionsPossibles[self.np.random.randint(0, len(actionsPossibles))]
                    # print("random",action)

                new_state = self.env[state].actions[action]
                # print('action: ',action)
                # print('new_state: ', new_state)
                # #print(new_state)
                # print(self.q_table[new_state].items())
                nextStateMaxQvalue = max(self.q_table[new_state].items(), key=operator.itemgetter(1))[1]
                rwd = self.env[new_state].r
                old_qsa = self.q_table[state][str(state) + action]

                # UPDATE Q ========================================================================

                q_target = rwd + self.learning_rate * nextStateMaxQvalue


                self.q_table[state][str(state) + action] += self.discount_rate * (q_target - self.q_table[state][str(state) + action])
                biggest_change = max(biggest_change, self.np.abs(old_qsa - self.q_table[state][str(state) + action]))
                state = new_state
                n_steps = n_steps + 1
                rewards_current_episode += rwd

                #if (self.env[state].r == self.r[2] or self.env[state].r == self.r[0] ) :
                if (state == self.state_obj):

                    # if (min_step <= n_steps):
                    #     n_steps = min_step
                    #     quantTime += 1
                    #     if quantTime >= self.limitStoped:
                    #         self.num_episodes = 0
                    #
                    # else:
                    #     quantTime = 0
                    #     min_step = n_steps

                    # print('steps :', n_steps)
                    list_epsForsteps.append(n_steps)
                    rewards_all_episodes.append(rewards_current_episode)
                    deltas.append(biggest_change)
                    break
                    # key = False

                # Exploration rate decay
                self.exploration_rate = self.min_exploration_rate + \
                                   (self.max_exploration_rate - self.min_exploration_rate) * \
                                   self.np.exp(-self.exploration_decay_rate * i)
            i += 1
        return self.q_table, list_epsForsteps,rewards_all_episodes, deltas


class SimpleQL:
    # variables
    num_episodes = 1000
    learning_rate = 0.9
    discount_rate = 0.1
    q_table = {}
    init_space = 0
    r = []
    env = {}
    np = 0
    state_obj = 0
    limitStoped=0
    exploration_rate = 1
    # construtor UAV
    def __init__(self, num_episodes, learning_rate,
                 discount_rate, init_space, q_table,
                 env, r, np,limitStoped,state_obj):



        self.num_episodes = num_episodes
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.init_space = init_space
        self.q_table = q_table
        self.r = r
        self.env = env
        self.np = np
        self.limitStoped = limitStoped
        self.state_obj = state_obj

    def start(self):

        #iteration for episode
        list_epsForsteps = []
        rewards_all_episodes = []
        deltas = []
        min_step = 99999999
        quantTime = 0
        i = 0
        while i <= self.num_episodes:
            state = self.init_space  # init
            n_steps = 0
            rewards_current_episode = 0
            key = True
            # print("Episodio --- ", i)
            # ...Step to episodes
            biggest_change = 0
            while True:
                # Exploration-exploitation trade-off

                actionsPossibles = []
                # print('caiu no else')
                for x in self.env[state].actions:
                    if self.env[state].actions[x] >= 0:
                        actionsPossibles.append(x)
                # choose random actions
                action = actionsPossibles[self.np.random.randint(0, len(actionsPossibles))]
                # print("random",action)

                new_state = self.env[state].actions[action]
                # print('action: ',action)
                # print('new_state: ', new_state)
                nextStateMaxQvalue = max(self.q_table[new_state].items(), key=operator.itemgetter(1))[1]
                rwd = self.env[new_state].r
                old_qsa = self.q_table[state][str(state) + action]

                # UPDATE Q ========================================================================
                if self.env[state].r != self.r[2] or self.env[state].r != self.r[0]:
                    q_target = rwd + self.learning_rate * nextStateMaxQvalue
                else:
                    q_target = rwd

                self.q_table[state][str(state) + action] += self.discount_rate * (q_target - self.q_table[state][str(state) + action])
                biggest_change = max(biggest_change, self.np.abs(old_qsa - self.q_table[state][str(state) + action]))
                state = new_state
                n_steps = n_steps + 1
                rewards_current_episode += rwd

                #if (self.env[state].r == self.r[2] or self.env[state].r == self.r[0] ) :
                if (self.env[state].r == self.r[2]):

                    # if (min_step <= n_steps):
                    #     n_steps = min_step
                    #     quantTime += 1
                    #     if quantTime >= self.limitStoped:
                    #         self.num_episodes = 0
                    #
                    # else:
                    #     quantTime = 0
                    #     min_step = n_steps

                    # print('steps :', n_steps)
                    list_epsForsteps.append(n_steps)
                    rewards_all_episodes.append(rewards_current_episode)
                    deltas.append(biggest_change)
                    break
                    # key = False

            i += 1
        return self.q_table, list_epsForsteps,rewards_all_episodes, deltas
class Sarsa:
# variables
    num_episodes = 1000
    learning_rate = 0.9
    discount_rate = 0.1
    q_table = {}
    init_space = 0
    r = []
    env = {}
    np = 0
    limitStoped = 0
    exploration_rate = 1
    state_obj=0
    # construtor UAV
    def __init__(self, num_episodes, learning_rate,
                 discount_rate, init_space, q_table,
                 env, r, np,limitStoped,state_obj):



        self.num_episodes = num_episodes
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.init_space = init_space
        self.q_table = q_table
        self.r = r
        self.env = env
        self.np = np
        self.limitStoped = limitStoped
        self.state_obj = state_obj
    def start(self):

        #iteration for episode
        list_epsForsteps = []
        rewards_all_episodes = []
        deltas = []
        min_step = 99999999
        quantTime = 0
        i = 0
        while i <= self.num_episodes:
            state = self.init_space  # init
            n_steps = 0
            rewards_current_episode = 0
            key = True
            # print("Episodio --- ", i)
            # ...Step to episodes
            biggest_change = 0
            while True:
                # Exploration-exploitation trade-off

                actionsPossibles = []
                # Q(s,a)
                for x in self.env[state].actions:
                    if self.env[state].actions[x] >= 0:
                        actionsPossibles.append(x)
                # choose random actions
                action = actionsPossibles[self.np.random.randint(0, len(actionsPossibles))]
                # print("random",action)

                new_state = self.env[state].actions[action]


                #Q(s',a')
                for x in self.env[ new_state].actions:
                    if self.env[ new_state].actions[x] >= 0:
                        actionsPossibles.append(x)
                # choose random actions
                action2 = actionsPossibles[self.np.random.randint(0, len(actionsPossibles))]
                # print("random",action)


                # print('action: ',action)
                # print('new_state: ', new_state)
                nextStateMaxQvalue = self.q_table[new_state][str(new_state) + action2]
                rwd = self.env[new_state].r
                old_qsa = self.q_table[state][str(state) + action]

                # UPDATE Q ========================================================================
               # if self.env[state].r != self.r[2] or self.env[state].r != self.r[0]:
                q_target = rwd + self.learning_rate *  nextStateMaxQvalue-self.q_table[state][str(state) + action]
               # else:
               #     q_target = rwd

                self.q_table[state][str(state) + action] += self.discount_rate * (q_target)
                biggest_change = max(biggest_change, self.np.abs(old_qsa - self.q_table[state][str(state) + action]))
                state = new_state
                n_steps = n_steps + 1
                rewards_current_episode += rwd

                #if (self.env[state].r == self.r[2] or self.env[state].r == self.r[0] ) :
                if (state == self.state_obj):

                    # if (min_step <= n_steps):
                    #     n_steps = min_step
                    #     quantTime += 1
                    #     if quantTime >= self.limitStoped:
                    #         self.num_episodes = 0
                    #
                    # else:
                    #     quantTime = 0
                    #     min_step = n_steps

                    # print('steps :', n_steps)
                    list_epsForsteps.append(n_steps)
                    rewards_all_episodes.append(rewards_current_episode)
                    deltas.append(biggest_change)
                    break
                    # key = False

            i += 1
        return self.q_table, list_epsForsteps,rewards_all_episodes, deltas
