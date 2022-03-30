#criar cenario
from matplotlib import pyplot as plt
import numpy as np
import random
import math
#=====================================================>
# Two dimensional rotation
# returns coordinates in a tuple (x,y)
class Cenario:
    def rotate(self,x, y, r):
        rx = (x*math.cos(r)) - (y*math.sin(r))
        ry = (y*math.cos(r)) + (x*math.sin(r))
        return (rx, ry)

    # create a ring of points centered on center (x,y) with a given radius
    # using the specified number of points
    # center should be a tuple or list of coordinates (x,y)
    # returns a list of point coordinates in tuples
    # ie. [(x1,y1),(x2,y2
    def point_ring(self,center, num_points, radius):
        arc = (2 * math.pi) / num_points # what is the angle between two of the points
        points = []
        for p in range(num_points):
            (px,py) = self.rotate(0, radius, arc * p)
            px += center[0]
            py += center[1]
            points.append((px,py))
        return points
    #=====================================++>

    # space_x = 100
    # space_y = 100
    # quant_blocks = 15
    # space_grid = []
    # id = 0
    # block_off_id = np.random.randint((space_x * space_y),size=(quant_blocks));
    #
    #
    # # Espaco de posicionamento do UAV
    # for x in range(space_x):
    #     for y in range(space_y):
    #         id = id+1
    #         space_grid.append(
    #             {
    #                 'id': id,
    #                 'x' : x,
    #                 'y' : y,
    #                 'block': 1 if (True==id in block_off_id) else 0
    #             }
    #         )
    #         id = id + 1
    def create(self):
            #quantidades de UAVs
            ND_max = 10 #numero de UAVs
            pop = 100 #populacao
            quantPositions = 1+(ND_max*3)+3
            matrix_UAVs = np.zeros((pop,quantPositions)) #matrix de processamento
            dim_x = 1000 #dimensao eixo x
            dim_y = 1000 #dimensao eixo y
            dim_z_max = 120 #altura maxima
            dim_z_min = 30 #altura minima

            posOPtoWire_A_x = 0
            posOPtoWire_A_y = 0
            posOPtoWire_A_z = 35

            posOPtoWire_B_x = 1000
            posOPtoWire_B_y = 1000
            posOPtoWire_B_z = 35


            enlace = 300 #m
            for i in range(pop):
                ND = 10
                matrix_UAVs[i, 0] = ND  #atribua o quantidade de UAVs
                range_sort = 100
                origem_x = posOPtoWire_A_x
                origem_y = posOPtoWire_A_y

                for j in range(1,(ND)*3,3):

                    coord = self.point_ring((origem_x, origem_y), range_sort, enlace)
                    x=[]
                    y=[]
                    cont = 0
                    for tuple in coord:
                        #verificar numeros fora do range do cenario
                        if (tuple[0] > 0 and tuple[0] <= dim_x and tuple[1] >0 and tuple[1]<= dim_y ):
                            x.append(tuple[0])
                            y.append(tuple[1])

                    # Dentre as possiblidade, escolha um
                    eleito = np.random.randint(len(x))
                    proximo_x =  x[eleito]
                    proximo_y =  y[eleito]
                    matrix_UAVs[i,j] = proximo_x # escolha o x
                    matrix_UAVs[i, j+1] = proximo_y # escolha o y
                    matrix_UAVs[i, j+2] = 50 # escolha o z

                    # Atribua o proximo ponto a origem
                    origem_x = proximo_x
                    origem_y = proximo_y
            return matrix_UAVs



## print points UAV================================================>
# for j in range(1,33,3):
#         print(j)
#         plt.plot(matrix_UAVs[0,j], matrix_UAVs[0,j+1],marker='*')
#
# plt.plot(matrix_UAVs[0,range(1,33,3)],matrix_UAVs[0,range(2,33,3)], linestyle = 'dotted')
# plt.show()

#teste
c = Cenario()
flowers = c.create()
print('fim')