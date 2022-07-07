from math import sin, cos, sqrt, atan2, radians
import numpy as np
import csv
import networkx as nx
from geographiclib.geodesic import Geodesic
from app_final.QL import QL


# from scipy.spatial import distance as distAPI



def calTime(va, payload, battery, np):
    Cd = 0.54  # drag coefficient
    A = 1.2  # m - front surface of UAV
    D = 1.2754  # kgm3 - air density
    b = 8.7  # m - UAV width
    # payload = 90 #UAV weight + pay/load

    p = (0.5 * Cd * A * D * ((va) ** 3)) + ((payload) ** 2) / (D * (b ** 2) * va)
    t = np.ceil(battery / p)
    return t


def energyCons2(m, g, s, vg, vp):
    return ((m * (vp ** 2) * s) + (m * g * s)) / (2 * vg)


def distance(lat1, lon1, lat2, lon2):
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


# Calcular a distancia euclidiana entre lat e long de dois pontos
def positionUav(lat1, long1, lat2, long2, distEnlace, tecAcessMax):
    A = (lat1, long1)  # Point A (lat, lon)
    B = (lat2, long2)  # Point B (lat, lon)
    s = tecAcessMax * 1000  # Distance (m)
    distEnlace = distEnlace * 1000  # convert to m to km
    if distEnlace <= tecAcessMax:
        s = distEnlace / 2
    dtot = s
    saveCoorUAV = []
    while dtot <= distEnlace:
        # Define the ellipsoid
        geod = Geodesic.WGS84

        # Solve the Inverse problem
        inv = geod.Inverse(A[0], A[1], B[0], B[1])
        azi1 = inv['azi1']
        # print('Initial Azimuth from A to B = ' + str(azi1))

        # Solve the Direct problem
        dir = geod.Direct(A[0], A[1], azi1, s)
        C = (dir['lat2'], dir['lon2'])
        saveCoorUAV.append(C)

        # print('C = ' + str(C))
        dtot += s
        A = C
    return saveCoorUAV


# variaveis da topologia ================================================================================================
file = '../stockholm.txt'
name = 'stockholm'
graph = nx.DiGraph(name=name)  # DiGraph because we have two fibers (one each way) between any pair of nodes
nNodes = 0
nLinks = 0
idEdge = 0
nodes = []
edges = []

# =======================================================================================================================
import math

with open(file, 'r') as nodes_lines:
    for idx, line in enumerate(nodes_lines):
        if idx > 2 and idx <= nNodes + 2:  # skip title line
            info = line.replace("\n", "").split(" ")
            graph.add_node(info[0], name=info[1], pos=(float(info[3]), float(info[2])))
            nodes.append(info[0])
        elif idx > 2 + nNodes and idx <= 2 + nNodes + nLinks:  # skip title line
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

# pontos estação===================================================
graph.add_node('34', name='Base A', pos=(18.3087, 59.2127))
graph.add_node('35', name='Base B', pos=(17.7847, 59.4176))
graph.add_node('36', name='Base C', pos=(16.7284, 59.4983))
graph.add_node('37', name='Base D', pos=(18.7073, 59.4387))
# =================================================================


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
names = nx.get_node_attributes(graph, 'name')
pos = nx.get_node_attributes(graph, 'pos')
distances = nx.get_edge_attributes(graph, 'weight')
# show graph=======================================================
# plt.figure(figsize=(12,10))
#
# nx.draw_networkx(graph, pos, with_labels=False, labels=names)
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
for z in range(1, 5):
    baseFixaToNodes = []
    for i in range(len(pos)):
        lat1 = radians(pos[str(33 + z)][1])
        lon1 = radians(pos[str(33 + z)][0])
        lat2 = radians(pos[str(i + 1)][1])
        lon2 = radians(pos[str(i + 1)][0])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        baseFixaToNodes.append(R * c)
    AllBaseFixaToNode.append(baseFixaToNodes)

menorDistanciaBaseFixa = []
mat = np.matrix(AllBaseFixaToNode)
for i in range(33):
    result = np.where(mat[:, i] == np.amin(mat[:, i]))
    menorDistanciaBaseFixa.append(result[0][0])

# ===========================================================================
desastre = '../desastres.csv'
listDes = []

with open(desastre, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        listDes.append(row)

nodesOfDisastre = []
for des in listDes:
    des = list(map(int, des))
    nodesOfDisastre.append(np.trim_zeros(des))

# =====================================================
#   O desastre '12' foi escolhido,
#   logo, precisamos separar os pares de nos
#   que compoem os links rompidos
# =====================================================
linksDesastre = np.array_split(nodesOfDisastre[12], 12)
linksDesastre[0]
distanceEnlaceTec = 2  # km
desRangeUavs = []
pontoDePartidaUavId = np.zeros((len(linksDesastre), 50)) - 1
pontoDePartidaUavDistance = np.zeros((len(linksDesastre), 50)) - 1
numDesastre = 0
for j in linksDesastre:

    # id_baseA = menorDistanciaBaseFixa[j[0] - 1]
    # id_baseB = menorDistanciaBaseFixa[j[1]-1]
    posNodA = pos[str(j[0])]
    posNodB = pos[str(j[1])]

    pontsBetwNodeAB = positionUav(posNodA[1], posNodA[0], posNodB[1], posNodB[0],
                                  graph[str(j[0])][str(j[1])]['weight'], distanceEnlaceTec)

    # if
    matAux = np.zeros((4, len(pontsBetwNodeAB)))
    vetDistance = []
    for i in range(4):
        vetDistance = []
        for p in pontsBetwNodeAB:
            pos[str(34 + i)]  # bases fixas
            vetDistance.append(distance(pos[str(34 + i)][1], pos[str(34 + i)][0], p[0], p[1]))

        matAux[i, 0:len(vetDistance)] = vetDistance
    pontoDePartidaUavId[numDesastre, 0:len(np.argmin(matAux, axis=0))] = np.argmin(matAux, axis=0)
    pontoDePartidaUavDistance[numDesastre, 0:len(np.min(matAux, axis=0))] = np.min(matAux, axis=0)
    numDesastre += 1

# =======================================================================================================================
#                                        Calculo consumo de energia
# =======================================================================================================================
# variaveis gerais ======================================================================================================
consumerEnergyUavForMission = np.zeros((len(linksDesastre), 50))
zeroPaths = np.zeros(50)
consumerEnergyUavForMissionQLe = np.zeros((len(linksDesastre), 50))
consumerEnergyUavForMissionQLeNaive = np.zeros((len(linksDesastre), 50))
energiaDisponivel = np.zeros((len(linksDesastre), 50))
energiaDisponivelQLe = np.zeros((len(linksDesastre), 50))
tf = np.zeros((len(linksDesastre), 50))
tfQLe = np.zeros((len(linksDesastre), 50))
vUav = 15  # m/s
# referece: http://xn--drmstrre-64ad.dk/wp-content/wind/miller/windpower%20web/en/tour/wres/calculat.htm
vWindNoBuilding = [12.03, 12.70, 13.1]  # without obstacules
vWindBuilding = [6.4, 7.69, 8.44]
alturas = [50, 100, 150]  # m
m = 90  # massa uav
g = 9.8  # aceleracao da gravidade m/s
# tf = 40 # tempo de voo
s = 0  # distancia de voo
vp = vUav + vWindNoBuilding[2]
bateriaUAV = 8000  # kj
payload = 90  # kg

# =======================================================================================================================
# =================Calculo de consumo de energia dos UAVs durante Ida/Volta [heuristica sarsa]======================
# =======================================================================================================================

# Variaveis para a heuristica sarsa=================================================================================
pontoDePartidaUavWindSpeed = np.zeros((len(linksDesastre), 50))
pontoDePartidaUavWindSpeedNaive = np.zeros((len(linksDesastre), 50))

pontoDePartidaUavNewDistace = np.zeros((len(linksDesastre), 50))
pontoDePartidaUavNewDistaceNaive = np.zeros((len(linksDesastre), 50))

n_segms = [30]
num_episodes = [20000]
conj_learning_rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
conj_discount_rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
allPaths = []
# allPaths.append(zeroPaths)
# =====================================================================
# quant_uavs_service = len(pontoDePartidaUavDistance[0, :])
quant_uavs_service = 1
quant_links_broke = len(pontoDePartidaUavDistance[0:1, 0])
all_sts = []
# all_sts.append(['n_segmentos', 'num_episodes', 'learning_rate', 'discount_rate','sarsa fail'])

for n_segm in n_segms:
    for n_ep in num_episodes:
        for learning_rate in conj_learning_rate:
            for discount_rate in conj_discount_rate:
                for i in range(quant_links_broke):
                    print('Destino:', i + 1)
                    for j in range(quant_uavs_service):
                        print('Link Optico _>', '[' + str(i + 1) + '] ', 'UAV mission -> [' + str(j + 1) + '] ')
                        s = pontoDePartidaUavDistance[i, j] * 1000  # convert km to m
                        if s >= 0:
                            segm = int(np.ceil(s / (vUav * n_segm)))
                            percentAumentoDist = []
                            segmVdsolo = []
                            sumPath = 0
                            d = 0
                            dNaive = 0
                            segm=1
                            for z in range(segm):
                                # print(f'segmento: {z}')
                                # criar instancia do Objeto Sarsa
                                seed = i + j + z
                                ql = QL(np, n_segm, seed, n_ep, learning_rate, discount_rate)
                                # criar ambiente a ser explorado
                                # ql.creatEnv(i + j + z)

                                # chamar o metodo responsavel pelo Sarsa
                                sarsa_q_table, sarsa_list_epsForsteps, \
                                sarsa_rewards_all_episodes, sarsa_deltas = ql.start_sarsa()

                                # retorne o caminho e a falha ao encontrar uma rota valida
                                path_sarsa, fail_sarsa = ql.findPath(sarsa_q_table, ql.init_space, ql.state_obj)
                                print(path_sarsa, "sts fail:", fail_sarsa)
                                # # chamar o metodo responsavel pelo ql_simple
                                # simple_ql_q_table, sarsa_list_epsForsteps, \
                                # sarsa_rewards_all_episodes, sarsa_deltas = ql.start_simpleQL()
                                #
                                # path_ql_sample, fail_ql_sample = ql.findPath(simple_ql_q_table, ql.init_space, ql.state_obj)
                                #
                                # # chamar o metodo responsavel pelo Sarsa
                                # egreedy_q_table, egreedy_list_epsForsteps, \
                                # egreedy_rewards_all_episodes, egreedy_deltas = ql.start_egreed()
                                #
                                # # retorne o caminho e a falha ao encontrar uma rota valida
                                # path_egreedy, fail_egreedy = ql.findPath(egreedy_q_table, ql.init_space, ql.state_obj)
                                # n_segmentos | num_episodes | learning_rate | discount_rate | egreedy fail | sarsa fail | simple q-learning fail|
                                vet_estatistica = [n_segm, num_episodes, learning_rate, discount_rate, fail_sarsa]
                                info = ['id_uav', 'n_segmentos','num_episodes', 'learning_rate', 'discount_rate', 'fail', 'path']
                                dict_row = {
                                    'id_uav': j,
                                    'n_segmentos': n_segm,
                                    'num_episodes': n_ep,
                                    'learning_rate': learning_rate,
                                    'discount_rate': discount_rate,
                                    'fail': fail_sarsa,
                                    'path': path_sarsa
                                }

                                all_sts.append(dict_row)
                                with open('../data_sarsa/'+str(n_segm)+'_x_'+str(n_segm)+'_'+str(n_ep)+'learning_rate_x_discount_rate_sarsa_estatistica_ml_cenario_6.csv', 'w') as csvfile:
                                    writer = csv.DictWriter(csvfile, fieldnames=info)
                                    writer.writeheader()
                                    writer.writerows(all_sts)
