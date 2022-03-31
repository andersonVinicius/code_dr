import numpy as np
import random
from scipy.stats import levy
from main_cenario import Cenario
class FPA():
    def __init__(self, switch_probability=0.8, n_flowers=50, n_parameters=2, constraints=None):
        # Initialization of variables
        self.sp = switch_probability
        self.n_flowers = n_flowers
        self.flowers = []
        self.cost = np.zeros(n_flowers)
        self.random = np.random
        self.n_parameters = n_parameters
        self.const = constraints

        # Random Initial Flowers
        self.init_flowers()
        # Get the best flower from initial population
        self.best = self.flowers[self.cost.argmin()]

    def calcularObstaculos(self,x):
        return np.random.randint(20)
    def calcularDist(self,x):

        return x

    def function_obj(self,x):
        qtd_var = 3 # X, Y, Z

        n_uavs = len(x)/qtd_var
        qtd_links = n_uavs+1

        linkMax = 300 #metros

        #calcular quantidade de obstaculos presentes no obstaculos
        qtd_obstaculos = self.calcularObstaculos(x)

        #calcular a distancia euclidiana entre o ultimo UAV e o ponto optico_wireless
        dist_optWirelessToUAV = self.calcularDist(x)

        if dist_optWirelessToUAV>linkMax:
            out = 10000000
        else:
            out = (dist_optWirelessToUAV/linkMax) + qtd_obstaculos

        return out

    def global_pollination(self,x): #Global Pollination
        x_new = x + levy.rvs(size=x.shape[0])*(self.best - x)
        return x_new

    def local_pollination(self,x,x1,x2):
        x_new = x + self.random.randn() * (x1-x2)
        return x_new
    def init_flowers(self):
        c = Cenario()
        self.flowers = c.create()
        i=0
        for flw in self.flowers:
            self.cost[i]=self.function_obj(flw)
            i=i+1
        return 0

    def optimize(self,max_gen=100):

        # Save history for plotting
        history = np.zeros((max_gen, self.n_parameters))

        # Generation loop
        for i in range(max_gen):

            history[i, :] = self.best # update history

            # Flower loop
            for j in range(self.n_flowers):
                p = self.random.rand()

                # Global Pollination if  p <= switch probability
                if p <= self.sp:
                    x_temp = self.global_pollination(self.flowers[j])

                # Local Pollination if p > switch probability
                else:
                    [r1,r2] = random.sample((0,self.n_flowers), 2)
                    x_temp = self.local_pollination(self.flowers[j],self.flowers[r1],self.flowers[r2])

                # Apply  constraints

