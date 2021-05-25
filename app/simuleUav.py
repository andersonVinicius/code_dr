import numpy as np

nUavs = 5
pathMax = 10
h = 1
times = 3600*h # sec

read=np.genfromtxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
                   "qualis_paper/dataS/seedDisponibles.csv",delimiter=";").astype(int)

# =============================================================================================
#                                      SIMULATION
# =============================================================================================
#time x uav x path 3d array
withStrategy = np.zeros(shape=(times,nUavs,pathMax), dtype=int)
withoutStrategy = np.zeros(shape=(times,nUavs,pathMax), dtype=int)

for t in range():
    print(t)
    #upadete seed
    np.random.seed(read[t])
    print(np.random.uniform(0, 1))

    # for u in range(nUavs):
    #
    #     #with strategy -------
    #     withStrategy[t,u,:]
    #
    #     #without strategy-----
    #     withoutStrategy[t,u,:]


