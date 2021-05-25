from Uavs import Uav
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#criar UAV
n_uavs = 4
list_uavs = list()
enlace_tec = 2000
x = 0
y = 20
z = [55,55,55,55]

xdata = list()
ydata = list()
zdata = list()

for i in range(n_uavs):


    x = x + enlace_tec
    y = y - 4
    list_uavs.append(Uav(x,y,z[i],5,10,100))

#  ponto optico-wireless
xpos = [0,x]
ypos = [20,1]
# num_elements = len(xpos)
zpos = [50,50]
dx = [1000, 1000]
dy = [1, 1]
dz = [1,1]

# %% uavs
for i in range(n_uavs):
    xdata.append(list_uavs.__getitem__(i).getPosX())
    ydata.append(list_uavs.__getitem__(i).getPosY())
    zdata.append(list_uavs.__getitem__(i).getPosZ())


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# UAV
ax.scatter3D(xdata, ydata, zdata, c='r', marker='*')
# base Station
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g')
ax.grid(linewidth=1)
plt.show()
# plt.savefig("mygraph.png")
