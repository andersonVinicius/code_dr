import  numpy as np
n_uavs = 5
prob_bulding = 0.3
prob_to_park = 0.05

m = 10 #kg
vw = 6.4#m/s
vp = vw#m/s
g = 9.8#m/s
t= 1800#sec
tot = 0
tot_i = 0


# calculo de energia para pairar
# entre os prédios
def energyCons2(m,g,t):
   return ((m * g * t) )/1000


# calculo de energia para pairar
# sob influência do vento
def energyCons(m,g,t,vp):
   return ((0.5*m*(vp**2)*t) + (m * g * t) )/1000


#=======================================
#       solucao Proposta
#---------------------------------------
#para cada UAV faca
v_tot = np.zeros((100,100))
for j in range(100):
    for k in range(100):
        tot = 0
        #para todos os UAVs do link faça
        for i in range(n_uavs):
            # verificar se há prédios
            if np.random.rand()<=j/100:
                # pousar sob os prédios
                if np.random.rand() <= k/100:
                    e=0
                # pairar entre os prédios
                else:
                    e = energyCons2(m,g,t)
            # pairar e sofrer os efeitos do vento
            else:
                e = energyCons(m, g, t, vp)
            tot = tot+e
        v_tot[j,k]= tot

print('Solucao Proposta:', np.mean(v_tot))

np.savetxt("solucaoProposta_vel6.4ms_10Kg.csv", v_tot, delimiter=";")
#=======================================
#       solucao ingenua
#---------------------------------------

m = 90 #kg
vw = 12#m/s
vp = vw#m/s
g = 9.8#m/s
t= 1800#sec

tot_i = energyCons(m, g, t, vp) * n_uavs
print('Solucao Ingenua:',tot_i)














