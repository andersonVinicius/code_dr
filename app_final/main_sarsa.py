import csv
from math import sin, cos, sqrt, atan2, radians

import networkx as nx
import numpy as np
from QL import QL
from geographiclib.geodesic import Geodesic
import math


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


linksDesastre = np.array_split(nodesOfDisastre[12],12)
linksDesastre[0]
distanceEnlaceTec = 2 #km
desRangeUavs = []
pontoDePartidaUavId = np.zeros((len(linksDesastre),50))-1
pontoDePartidaUavDistance = np.zeros((len(linksDesastre),50))-1
numDesastre = 0
for j in linksDesastre:

    posNodA = pos[str(j[0])]
    posNodB = pos[str(j[1])]

    pontsBetwNodeAB=positionUav( posNodA[1],  posNodA[0], posNodB[1],  posNodB[0],
                                 graph[str(j[0])][str(j[1])]['weight'], distanceEnlaceTec)

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

#===============================================================================
#                         Calculo Consumo de Energia
#===============================================================================

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
s = 0 # distancia de voo
vp = vUav+vWindNoBuilding[2]
# e = ( (m * ( (vp) ** 2) * s) + (m*g*s) )/(2*(vUav))
bateriaUAV = 8000 #kj

payload = 90

#============QLearnigProcess==========================================

pontoDePartidaUavWindSpeed = np.zeros((len(linksDesastre),50))
pontoDePartidaUavNewDistace = np.zeros((len(linksDesastre),50))

#=============Ida / Volta QL-egreedy ===================================
meanConsumerQLe = []
meanTimeOperationQLe = []
for i in range(len(pontoDePartidaUavDistance[:,0])):
    print('Destino:',i+1)
    for j in range (len(pontoDePartidaUavDistance[0,:])):
        print('UAV', '['+str(i + 1)+'] ','['+str(j + 1)+'] ')
        s = pontoDePartidaUavDistance[i,j]*1000 #convert km to m

        if s>=0:
            segm = int(np.ceil(s/(vUav * 10)))
            percentAumentoDist = []
            segmVdsolo = []
            for z in range(segm):

                ql = QL(np)
                ql.creatEnv(i+j+z)
                # egreedy_q_table, egreedy_list_epsForsteps, \
                # egreedy_rewards_all_episodes, egreedy_deltas = ql.start_sarsa()
                ss_q_table, ss_list_epsForsteps, \
                ss_rewards_all_episodes, ss_deltas = ql.start_sarsa()
                path,fail=ql.findPath( ss_q_table,ql.init_space,ql.state_obj)
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
                    p2 = (ql.env[ ql.state_obj ].x_init,ql.env[ql.state_obj].y_init)
                    d2 = distance.euclidean(p1, p2)
                    percentAumentoDist.append( d2/d )
                else:
                    print('Algoritmo falhou na busca pelo caminho!')
                    for p in range(10):
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

# np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
#            "qualis_paper/dataS/meanConsumerSarsa.csv", meanConsumerQLe, delimiter=";")
# np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
#            "qualis_paper/dataS/meanTimeOperationSarsa.csv", meanTimeOperationQLe, delimiter=";")
np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
           "qualis_paper/dataS/distanceRunSarsa.csv", meanDistanceRun, delimiter=";")


def saveData(path,variable):
    np.savetxt("/home/anderson/Dropbox/posGraduacao/doutorado/"
               "qualis_paper/dataS/distanceRunSarsa.csv", variable, delimiter=";")