from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
velToDistace= np.zeros((90,4,40))
payloadVet = np.zeros(90*4*40)
sped = np.zeros(90*4*40)
distKm = np.zeros(90*4*40)
energ = np.zeros(90*4*40)
dis = [10,15,20,25]
c=0
for z in range(90):
    for i in range (4):
        for j in range(40):
            payloadVet[c] = z
            sped[c] = i
            distKm[0] = j
            Cd = 0.54 # drag coefficient
            A = 1.2 #m - front surface of UAV
            D = 1.2754 #kgm3 - air density
            b = 8.7 #m - UAV width
            va = dis[i]+12.32
            battery = 8000
            payload = z+1 #UAV weight + payload
            distance = 1000 * (1+j)
            p = (0.5 * Cd * A * D * ((va) ** 3)) + ((payload) ** 2)/ (D * (b ** 2) * va)
            t = distance/va

            velToDistace[z,i,j]=((((2*p)/1000)*t))
            energ = velToDistace[z,i,j]
            c=+1
#ax.plot_surface(velToDistace)
X, Y = np.meshgrid(sped, payloadVet)
ax.plot_surface(payloadVet, sped, energ)
#np.savetxt('yourfile.mat',velToDistace)
plt.show()
