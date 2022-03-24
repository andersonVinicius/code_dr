from grafico import grafico as grf
import numpy as np
import csv

# metodo de leitura csv e conv para array
def readCSV(nameDataset):
    data = []
    with open(nameDataset) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            data.append(row)
    return data
# metodo obter valores validos do dataset
def getValoresValidos(dataSets):
    dataNewNew = []
    for ds in dataSets:
        data = readCSV(ds[1])
        # verificando linhas validas
        dataNew = []
        for x in data:
            if np.sum(x) > 0:  # verifica se existem valores na row
                dataNew.append(x)

        dataNew = np.array(dataNew)
        dataNewNew.append([ds[0], dataNew[np.nonzero(dataNew)],ds[2]])

    return dataNewNew

# lista de dataSets
# energyConsumed------------
dataSetsEnergy = [
                    ["Q-learning","consumerEnergyUavForMissionQLe.csv","Energy consumed (j)"],
                    ["Naive","consumerEnergyUavForMissionQLeNaive.csv","Energy consumed (j)"]
                 ]
# windSpeed-----------------
dataSetsSWind = [
                    ["Q-learning","pontoDePartidaUavWindSpeed.csv","Wind speed (m/s)"],
                    ["Naive","pontoDePartidaUavWindSpeedNaive.csv","Wind speed (m/s)"]
                ]
# distance-----------------
dataSetsDistance = [
                        ["Q-learning", "pontoDePartidaUavNewDistace.csv", "Travelled distance (m)"],
                        ["Naive", "pontoDePartidaUavNewDistaceNaive.csv", "Travelled distance (m)"]
                   ]

#obter valores validos
data = getValoresValidos(dataSetsEnergy)
dataWind = getValoresValidos(dataSetsSWind)
dataDist = getValoresValidos(dataSetsDistance)

#instanciar objeto graficos
grf1 = grf()
#gerar graficos----------->
#barplot energy consumed
grf1.criarBarplotSeaborn(data)

#barplot wind speed
grf1.criarBarplotSeaborn(dataWind)

#barplot distance
grf1.criarBarplotSeaborn(dataDist)
#lineplot
# grf1.criarLineplotSeaborn(data)
