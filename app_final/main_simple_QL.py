
from math import sin, cos, sqrt, atan2, radians
import numpy as np
import csv
import networkx as nx
from geographiclib.geodesic import Geodesic
from QL import QL

def calTime(va, payload, battery,np):
    Cd = 0.54  # drag coefficient
    A = 1.2  # m - front surface of UAV
    D = 1.2754  # kgm3 - air density
    b = 8.7  # m - UAV width
    # payload = 90 #UAV weight + payload

    p = (0.5 * Cd * A * D * ((va) ** 3)) + ((payload) ** 2) / (D * (b ** 2) * va)
    t = np.ceil(battery/p)
    return t


# def calEnergy3(vg,va, distance, payload, battery,np):
#
#     #return (battery - (((p) / 1000) * t))
#     return p * t


def energyCons2(m,g,s,vg,vp):
   return (  (m*(vp ** 2)* s) + (m * g * s) )/ (2*vg)

def distance(lat1,lon1,lat2,lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return (R * c)

def positionUav(lat1,long1,lat2,long2,distEnlace,tecAcessMax):
    A = (lat1, long1)  # Point A (lat, lon)
    B = (lat2, long2)  # Point B (lat, lon)
    s = tecAcessMax * 1000 # Distance (m)
    distEnlace = distEnlace * 1000 #convert to m to km
    if distEnlace <= tecAcessMax:
        s = distEnlace/2
    dtot = s
    saveCoorUAV = []
    while dtot <=distEnlace:

        # Define the ellipsoid
        geod = Geodesic.WGS84

        # Solve the Inverse problem
        inv = geod.Inverse(A[0], A[1], B[0], B[1])
        azi1 = inv['azi1']
        #print('Initial Azimuth from A to B = ' + str(azi1))

        # Solve the Direct problem
        dir = geod.Direct(A[0], A[1], azi1, s)
        C = (dir['lat2'], dir['lon2'])
        saveCoorUAV.append( C )

        #print('C = ' + str(C))
        dtot += s
        A=C
    return saveCoorUAV


# from multiprocessing import Pool
# from multiprocessing import Manager
# from path import Path
# from demand  import Demand
# from solution import Solution
# from IPython import display
#

t.tic()
file='../../../../tccDaFernanda/stockholm.txt'
name ='stockholm'
# # initializing the graph object and computing the k_shortest_path
# topology = read_txt_file(topology_name + '.txt', topology_name)
graph = nx.DiGraph(name=name) # DiGraph because we have two fibers (one each way) between any pair of nodes
nNodes = 0
nLinks = 0
idEdge = 0
nodes = []
edges = []
with open(file, 'r') as nodes_lines:
    for idx, line in enumerate(nodes_lines):
        if idx > 2 and idx <= nNodes + 2: # skip title line
            info = line.replace("\n", "").split(" ")
            graph.add_node(info[0], name=info[1], pos=(float(info[3]), float(info[2])))
            nodes.append(info[0])
        elif idx > 2 + nNodes and idx <= 2 + nNodes + nLinks: # skip title line
            info = line.replace("\n", "").split(" ")
            graph.add_edge(info[1], info[2], id=idEdge, weight=float(info[3]))
            idEdge += 1
            edges.append((info[1], info[2]))
            graph.add_edge(info[2], info[1], id=idEdge, weight=float(info[3]))
            idEdge += 1
            edges.append((info[2], info[1]))
        elif idx == 1:
            nNodes = int(line)
        elif idx == 2:
            nLinks = int(line)

graph.graph['nodes'] = nodes
graph.graph['edges'] = edges
graph.add_node('34', name='Base A', pos=(18.3087,59.2127))
graph.add_node('35', name='Base B', pos=(17.7847,59.4176))
graph.add_node('36', name='Base C', pos=(16.7284,59.4983))
graph.add_node('37', name='Base D', pos=(18.7073,59.4387))
# graph.add_node('38', name='uav 1', pos=( 16.47167725028532,59.368296323082404))
# graph.add_node('39', name='uav 2', pos=(16.682698215835877,59.37005156181506))
# graph.add_node('40', name='uav 3', pos=(16.964089382749982,59.3718608755255))
# graph.add_node('38', name='meio', pos=(16.70028424301845,59.37018242406991))
# print(nx.spring_layout(graph))

# graph.draw_networkx(graph, 1,node_color= 'red')
# nx.dr
# graph.remove_edge('1', '7')
# graph.remove_edge('7', '1')
teste = graph.number_of_edges()
names = nx.get_node_attributes(graph,'name')
pos = nx.get_node_attributes(graph,'pos')
distances = nx.get_edge_attributes(graph, 'weight')
# show graph=======================================================
# plt.figure(figsize=(12,10))
#
# nx.draw_networkx(graph, pos, with_labels=True, labels=names)
# nx.draw_networkx_nodes(graph, pos, nodelist=['34'], node_color="r")
# nx.draw_networkx_nodes(graph, pos, nodelist=['35'], node_color="r")
# nx.draw_networkx_nodes(graph, pos, nodelist=['36'], node_color="r")
# nx.draw_networkx_nodes(graph, pos, nodelist=['37'], node_color="r")
# # nx.draw_networkx_nodes(graph, pos, nodelist=['38'], node_color="g")
# # nx.draw_networkx_nodes(graph, pos, nodelist=['39'], node_color="g")
# # nx.draw_networkx_nodes(graph, pos, nodelist=['40'], node_color="g")
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=distances)
#
# plt.ylabel('latitude')
# plt.xlabel('longitude')
# plt.tight_layout()
# plt.show()
# plt.close()
# ==================================================================
#
baseFixaToNodes = []
AllBaseFixaToNode = []
# approximate radius of earth in km
R = 6373.0
for z in range(1,5):
    baseFixaToNodes = []
    for i in range(len(pos)):

        lat1 = radians(pos[str(33+z)][1] )
        lon1 = radians(pos[str(33+z)][0] )
        lat2 = radians(pos[str(i+1)][1] )
        lon2 = radians(pos[str(i+1)][0] )

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        baseFixaToNodes.append(R * c)
    AllBaseFixaToNode.append(baseFixaToNodes)


menorDistanciaBaseFixa = []
mat=np.matrix(AllBaseFixaToNode)

for i in range(33):
    result = np.where(mat[:,i] == np.amin(mat[:,i]))
    menorDistanciaBaseFixa.append(result[0][0])



#===========================================================================
desastre = 'desastres.csv'
# with open(desastre, 'r') as nodes_lines:
#     for idx, line in enumerate(nodes_lines):
#         print (idx," : ",lines.numeric)

listDes=[]
with open(desastre, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        listDes.append(row)

nodesOfDisastre = []
for des in listDes:
    des = list(map(int, des))
    nodesOfDisastre.append(np.trim_zeros(des))


# print(baseFixaToNodes)
#=====================================================
#seperar em grupo
# spl = 1
# linksDesastre = []
# for i in range(13):
#     print (i)
#
#     linksDesastre.append(np.array_split(nodesOfDisastre[i],))
#     spl += 1

#=====================================================
#   O desastre '12' foi escolhido,
#   logo, precisamos separar os pares de nos
#   que compoem os links rompidos
#=====================================================
linksDesastre = np.array_split(nodesOfDisastre[12],12)
linksDesastre[0]
distanceEnlaceTec = 2 #km
desRangeUavs = []
pontoDePartidaUavId = np.zeros((len(linksDesastre),50))-1
pontoDePartidaUavDistance = np.zeros((len(linksDesastre),50))-1
numDesastre = 0
for j in linksDesastre:

    # id_baseA = menorDistanciaBaseFixa[j[0] - 1]
    # id_baseB = menorDistanciaBaseFixa[j[1]-1]
    posNodA = pos[str(j[0])]
    posNodB = pos[str(j[1])]

    pontsBetwNodeAB=positionUav( posNodA[1],  posNodA[0], posNodB[1],  posNodB[0],
                                 graph[str(j[0])][str(j[1])]['weight'], distanceEnlaceTec)


    # if
    matAux=np.zeros((4,len(pontsBetwNodeAB)))
    vetDistance = []
    for i in range(4):
        vetDistance = []
        for p in pontsBetwNodeAB:
            pos[str(34+i)] #bases fixas
            vetDistance.append(distance(pos[str(34+i)][1], pos[str(34+i)][0],p[0],p[1]))

        matAux[i, 0:len( vetDistance )] = vetDistance
    pontoDePartidaUavId [numDesastre,0:len(np.argmin(matAux, axis=0))] = np.argmin(matAux, axis=0)
    pontoDePartidaUavDistance [numDesastre,0:len(np.min(matAux, axis=0))] = np.min(matAux, axis=0)
    numDesastre += 1

#===========================
#calculo consumo de energia
#===========================

consumerEnergyUavForMission = np.zeros((len(linksDesastre),50))
consumerEnergyUavForMissionQLe = np.zeros((len(linksDesastre),50))
energiaDisponivel = np.zeros((len(linksDesastre),50))
energiaDisponivelQLe = np.zeros((len(linksDesastre),50))
tf = np.zeros((len(linksDesastre),50))
tfQLe = np.zeros((len(linksDesastre),50))



vUav = 15 #m/s
#referece: http://xn--drmstrre-64ad.dk/wp-content/wind/miller/windpower%20web/en/tour/wres/calculat.htm
vWindNoBuilding = [12.03,12.70,13.1]#without obstacules
vWindBuilding = [6.4,7.69,8.44]
alturas = [50,100,150]#m
m = 90 #massa uav
g = 9.8 # aceleracao da gravidade m/s
#tf = 40 # tempo de voo
s = 0 # distancia de voo
vp = vUav+vWindNoBuilding[2]
# e = ( (m * ( (vp) ** 2) * s) + (m*g*s) )/(2*(vUav))
bateriaUAV = 8000 #kj
# costEnergy = []
# for i in range (len(desRangeUavs[0])):
#     s=desRangeUavs[0][i]
#     e = ((m * ((vp) ** 2) * s) + (m * g * s)) / (2 * (vUav))
#     costEnergy.append(e)

# print()
# quantUavs = distanceEnlace-1
#

#load matlab
#mat = scipy.io.loadmat('file.mat')
# print()
# equacao 2
# Cd = 0.54
# A = 1.2 #m
# D = 1.2754 #kgm3
# b = 8.7 #mm
payload = 90
# va=vp
#energyCons(Cd,A,D,b,ep,va,payload)
#=============Ida / Volta ===================================
# for i in range(len(pontoDePartidaUavDistance[:,0])):
#     for j in range (len(pontoDePartidaUavDistance[0,:])):
#         s = pontoDePartidaUavDistance[i,j]*1000 #convert km to m
#         if s>=0:
#             #consumerEnergyUavForMission[i, j] = calEnergy3(vUav,vp, s, payload, bateriaUAV,np)/1000
#             consumerEnergyUavForMission[i,j] = energyCons2(payload,g,s,vUav,vp)/1000
#             energiaDisponivel[i,j] = bateriaUAV - (2*consumerEnergyUavForMission[i,j])
#            # tf[i,j] =((energiaDisponivel[i,j] * 1000)  /(m * g ))/60
#             tf[i,j] = (calTime(vWindNoBuilding[2], payload,energiaDisponivel[i,j]*1000,np))/60
#
# meanConsumer = [np.mean(consumerEnergyUavForMission[i,np.nonzero(consumerEnergyUavForMission[i,:])])
#                 for i in range(12)]
# meanTimeOperation = [np.mean(tf[i,np.nonzero(tf[i ,:])]) for i in range(len(tf[:,0]))]
# #save
# np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
#            "qualis_paper/dataS/meanConsumer.csv", meanConsumer, delimiter=";")
# np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
#            "qualis_paper/dataS/meanTimeOperation.csv", meanTimeOperation, delimiter=";")


#============Durante==========================================

# plt.figure(figsize=(12,10))
#y_pos = np.arange(12)
# plt.bar(y_pos,meanConsumer)
# plt.ylabel('Flight Energy consumption (kj)')
# plt.xlabel('Broken links')
# plt.title('Scenario n 12 - [going to the incidents]')

# plt.figure(figsize=(12,10))
# plt.bar(y_pos,meanTimeOperation)
# plt.ylabel('AVG - Operation Time (min)')
# plt.xlabel('Broken links')
# plt.title('Disaster scenario n 12 - [during the mission]')
#plt.show()

#============QLearnigProcess==========================================





# ql = QL(np)
# ql.creatEnv(1190)
# egreedy_q_table, egreedy_list_epsForsteps, \
#         egreedy_rewards_all_episodes, egreedy_deltas = ql.start()
#
#
#
# path=ql.findPath(egreedy_q_table,ql.init_space,ql.state_obj)
#
# print(path)
# from scipy.spatial import distance
# d=0
# for i in range(len(path)-1):
#     p1 = (ql.env[ path[i] ].x_init,ql.env[ path[i] ] .y_init)
#     p2 = (ql.env[ path[i+1] ].x_init,ql.env[path[i+1]].y_init)
#     d += distance.euclidean(p1, p2)
#
# print(d)
# p1 = (ql.env[ ql.init_space ].x_init,ql.env[ ql.init_space ].y_init)
# p2 = (ql.env[ ql.state_obj ].x_init,ql.env[ql.state_obj].y_init)
# d2 = distance.euclidean(p1, p2)
#
# print('Distancia em linha reta:', d2)
# print('Distncia otimizada:',d)

pontoDePartidaUavWindSpeed = np.zeros((len(linksDesastre),50))
pontoDePartidaUavNewDistace = np.zeros((len(linksDesastre),50))
#=============Ida / Volta QL-egreedy ===================================
from scipy.spatial import distance
import math
meanConsumerQLe = []
meanTimeOperationQLe = []
for i in range(len(pontoDePartidaUavDistance[:,0])):
    print('Destino:',i+1)
    for j in range (len(pontoDePartidaUavDistance[0,:])):
        print('UAV', '['+str(i + 1)+'] ','['+str(j + 1)+'] ')
        s = pontoDePartidaUavDistance[i,j]*1000 #convert km to m

        if s>=0:
            segm = int(np.ceil(s/(vUav * 50)))
            percentAumentoDist = []
            segmVdsolo = []
            for z in range(segm):

                ql = QL(np)
                ql.creatEnv(i+j+z)
                # egreedy_q_table, egreedy_list_epsForsteps, \
                # egreedy_rewards_all_episodes, egreedy_deltas = ql.start_sarsa()
                qs_q_table, qs_list_epsForsteps, \
                qs_rewards_all_episodes, qs_deltas = ql.start_simpleQL()
                path,fail=ql.findPath(qs_q_table,ql.init_space,ql.state_obj)
                wind = []
                dsolo = []
                if fail == False:
                    print('Sucesso')
                    for p in path:
                        wind.append(ql.env[p].windSpeed)
                        dsolo.append(ql.env[p].altura)
                    d=0
                    for k in range(len(path)-1):
                        if abs(dsolo[k]-dsolo[k+1]) != 0:
                            d+=math.sqrt((vUav**2)+ ((abs(dsolo[k]-dsolo[k+1])) ** 2))
                        else:

                            p1 = (ql.env[ path[k] ].x_init,ql.env[ path[k] ] .y_init)
                            p2 = (ql.env[ path[k+1] ].x_init,ql.env[path[k+1]].y_init)
                            d += distance.euclidean(p1, p2)
                    p1 = (ql.env[ ql.init_space ].x_init,ql.env[ ql.init_space ].y_init)
                    p2 = (ql.env[ ql.state_obj ]. x_init,ql.env[ql.state_obj].y_init)
                    d2 = distance.euclidean(p1, p2)
                    percentAumentoDist.append( d2/d )
                else:
                    print('Algoritmo falhou na busca pelo caminho!')
                    for p in range(50):
                        wind.append(vWindNoBuilding[2])
                        dsolo.append(151)
                        percentAumentoDist.append(0)

            pontoDePartidaUavWindSpeed[i,j] = np.mean(wind)
            pontoDePartidaUavNewDistace[i,j] = (s*(1+np.mean( percentAumentoDist)))

            vp = vUav + pontoDePartidaUavWindSpeed[i,j]
            #consumerEnergyUavForMissionQLe[i,j] = calEnergy3(vUav,vp, s, payload, bateriaUAV,np)/1000
            consumerEnergyUavForMissionQLe[i,j] = energyCons2(payload,g,s,vUav,vp)/1000
            energiaDisponivelQLe[i,j] = bateriaUAV - (2*consumerEnergyUavForMissionQLe[i,j])
            #tfQLe[i,j] =((energiaDisponivelQLe[i,j] * 1000)  /(m * g ))/60
            tfQLe[i, j] = (calTime(pontoDePartidaUavWindSpeed[i,j], payload, energiaDisponivelQLe[i, j]*1000,np)) / 60

meanConsumerQLe = [np.mean(consumerEnergyUavForMissionQLe[i,np.nonzero(consumerEnergyUavForMissionQLe[i,:])]) for i in range(12)]
meanTimeOperationQLe = [np.mean(tfQLe[i,np.nonzero(tfQLe[i,:])]) for i in range(len(tfQLe[:,0]))]
meanDistanceRun = [np.mean(pontoDePartidaUavNewDistace[i,np.nonzero(pontoDePartidaUavNewDistace[i,:])]) for i in range(12)]

#rastreio
# np.savetxt("dataS/meanConsumerQLSimple.csv", meanConsumerQLe, delimiter=";")
# np.savetxt("dataS/meanTimeOperationQLSimple.csv", meanTimeOperationQLe, delimiter=";")
np.savetxt("dataS/distanceRunQLSimple.csv", meanDistanceRun, delimiter=";")

#
# import numpy as np
# import matplotlib.pyplot as plt
# data = [[30, 25, 50, 20],
# [40, 23, 51, 17],
# [35, 22, 45, 19]]
# X = np.arange(1)
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(X + 0.00, meanTimeOperation[5], color = 'b', width = 0.25)
# ax.bar(X + 0.25, meanTimeOperationQLe[5], color = 'g', width = 0.25)
# plt.show()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # data to plot
# n_groups = 4
# means_frank = (90, 55, 40, 65)
# means_guido = (85, 62, 54, 20)
#
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.35
# opacity = 0.8
#
# rects1 = plt.bar(index, means_frank, bar_width,
# alpha=opacity,
# color='b',
# label='Frank')
#
# rects2 = plt.bar(index + bar_width, means_guido, bar_width,
# alpha=opacity,
# color='g',
# label='Guido')
#
# plt.xlabel('Person')
# plt.ylabel('Scores')
# plt.title('Scores by person')
# plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
# plt.legend()
#
# plt.tight_layout()
# plt.show()



