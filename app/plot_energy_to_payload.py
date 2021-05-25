import matplotlib.pyplot as plt
import numpy as np


dis = [10,15,20,25]
payL = [i for i in range(10,100,10)]
velToDistace= np.zeros((len(payL),40))
for i in range (len(payL)):
    for j in range(40):
        Cd = 0.54 # drag coefficient
        A = 1.2 #m - front surface of UAV
        D = 1.2754 #kgm3 - air density
        b = 8.7 #m - UAV width
        va = dis[1]+12.32
        battery = 8000
        payload = payL[i]#UAV weight + payload
        distance = 1000 * (1+j)
        p = (0.5 * Cd * A * D * ((va) ** 3)) + (((payload) ** 2)/ (D * (b ** 2) * va))
        t = distance/dis[1]

        velToDistace[i,j]=((((2*p)/1000)*t))



fig2, ax2 = plt.subplots(constrained_layout=True)
# ax2.plot(velToDistace[0,:],label="10 m/s")
# ax2.plot(velToDistace[1,:],label="15 m/s")
# ax2.plot(velToDistace[2,:],label="20 m/s")
# ax2.plot(velToDistace[3,:],label="25 m/s")
for i in range (len(payL)):
    ax2.plot(velToDistace[i, :], label=str(payL[i])+" Kg")

ax2.set_xlim([0,40])
# ax2.set_ylim([ymin,ymax])
plt.axhline(8000, color='b',ls='--')
ax2.text(1, 8899, r'battery limit', fontsize=9)
ax2.set_xlabel('Distance (Km)')
ax2.set_ylabel('Energy Consumer(J)')
plt.title('Propulsion speedb '+str(dis[1]+12.32)+" m/s")
ax2.legend()
plt.show()