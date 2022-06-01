import numpy as np
import random
from scipy.stats import levy
from Cenario import Cenario
class FPA():
    def __init__(self, switch_probability=0.8, n_flowers=50, n_parameters=2, constraints=None, n_uavs=2):
        # Initialization of variables
        self.sp = switch_probability
        self.n_flowers = n_flowers
        self.flowers = []
        self.cost = np.zeros(5000)
        self.random = np.random
        self.n_parameters = n_parameters
        self.const = constraints
        self.n_uavs = n_uavs
        self.var = 3

        # Random Initial Flowers
        self.init_flowers()

        # Get the best flower from initial population
        self.best = self.flowers[self.cost.argmin()]

    def get_line(self,x1, y1, x2, y2):
        points = []
        issteep = abs(y2 - y1) > abs(x2 - x1)
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(int(x1), int(x2) + 1):
            if issteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()
        return points

    def calcularObstaculos(self,vet):
        n_var = 3
        out =0
        # for i in range(0,len(vet),n_var):
        #
        #     get_line(vet[i], vet[i+1], x2, y2)
        #     if (vet[i]>=400 and vet[i]<=600 and vet[i+1]>=400 and vet[i+1]<=600):
        #         out = 10000000
        #         break
        # return out

        for i in range(0, len(vet), n_var):
            x = vet[i]
            y = vet[i + 1]
            z = vet[i + 2]
            if i == 0:
                pass
            elif i == (len(vet) - n_var):
                pass
            else:
                x_next = vet[i + n_var]
                y_next = vet[i + 1 + n_var]
                z_next = vet[i + 2 + n_var]
                points = self.get_line(x, y, x_next, y_next)
                # dist = np.sqrt(np.power((x - x_next), 2) + np.power((y - y_next), 2))
                print(points)


    def calcularDist(self,vet):
        dim_vet = len(vet)
        n_var = 3
        savaDist = []

        #Ponto Optico Wireless Inicial==>
        x_opw_A = 0
        y_opw_A = 0
        z_opw_A = 50

        #Ponto Optico Wireless Final =====>
        x_opw_B = 1000
        y_opw_B = 1000
        z_opw_B = 50
        totDist = 0

        for i in range(0,dim_vet,n_var):

            x = vet[i]
            y = vet[i + 1]
            z = vet[i + 2]
            if i == 0:

                x_next = vet[i + n_var]
                y_next = vet[i + 1 + n_var]
                z_next = vet[i + 2 + n_var]
                partA = np.sqrt(np.power((x - x_opw_A), 2) + np.power((y - y_opw_A), 2))
                partB = np.sqrt(np.power((x - x_opw_A), 2) + np.power((y - y_opw_A), 2))

                savaDist.append(partA)
                savaDist.append(partB)

                dist = partA + partB
                print("Primero link", dist)
            elif i==(dim_vet-n_var):
                dist = np.sqrt(np.power((x - x_opw_B), 2) + np.power((y - y_opw_B), 2))
                savaDist.append(dist)
                print("Ultimos links-->", dist)
            else:
                x_next = vet[i + n_var]
                y_next = vet[i + 1 + n_var]
                z_next = vet[i + 2 + n_var]
                dist = np.sqrt(np.power((x - x_next), 2) + np.power((y - y_next), 2))
                print("links do meio-->",dist)
                savaDist.append(dist)
            totDist = totDist + dist
        return totDist,savaDist

    def function_obj(self,x):
        qtd_var = 3 # X, Y, Z
        n_uavs = len(x)/qtd_var
        qtd_links = n_uavs+1
        out = 0

        linkMax = 300 #metros

        #calcular quantidade de obstaculos presentes no obstaculos
        qtd_obstaculos = self.calcularObstaculos(x)

        #calcular a distancia euclidiana entre o ultimo UAV e o ponto optico_wireless
        dist_optWirelessToUAV,saveDist = self.calcularDist(x)

        if dist_optWirelessToUAV> (linkMax * qtd_links):
            out = 10000000
        else:
            for item in saveDist:
                if (item>linkMax):
                    out = 10000000 +  qtd_obstaculos
                    break
                else:
                    out += (item/linkMax) + qtd_obstaculos

        return out

    def global_pollination(self,x): #Global Pollination
        x_new = x + levy.rvs(size=x.shape[0])*(self.best - x)
        return x_new

    def local_pollination(self,x,x1,x2):
        x_new = x + self.random.randn() * (x1-x2)
        return x_new
    def init_flowers(self):
        c = Cenario(self.n_uavs)
        self.flowers = c.create()
        i=0
        for flw in self.flowers:
            self.cost[i]=self.function_obj(flw)
            i=i+1
        return 0

    def optimize(self,max_gen=1000):

        # Save history for plotting
        history = np.zeros((max_gen, self.var * self.n_uavs))

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
                # calcule custo
                cost_temp = self.function_obj(x_temp)

                # Compare the newly generated flower with the previous flower
                if cost_temp < self.cost[j]:
                    self.flowers[j] = x_temp
                    self.cost[j] = cost_temp
                else:
                    continue
            # Update best
            self.best = self.flowers[self.cost.argmin()]
        return self.flowers, self.cost, history
