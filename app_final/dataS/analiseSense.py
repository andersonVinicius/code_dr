import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from grafico import grafico as grf
import numpy as np
g = 10 # m / s ^ 2
m= 90 # kg
vUav = 15 # m / s
# energy = zeros(1, 15);
# energyN = zeros(1, 15);
distanceTravel = [1,2,3,4,5,6,7,8,9,10,15,20] #km
saveSet = []

for winds in range(0,14):
    for dist in distanceTravel:


            energy = ((m * ( (vUav+winds) ** 2 ) * dist * 1000 ) + (m * g * dist * 1000 )) / (2 * vUav);
            print(energy)
            saveSet.append([winds, dist, m, energy])

df = pd.DataFrame(saveSet, columns = ['vento','distancia','massa','energia'] )
grf1 = grf()
grf1.criarLineplotSeaborn(df)

print('hello')
from grafico import grafico as grf
