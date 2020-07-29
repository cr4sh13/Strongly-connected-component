from DFS import *

time = 0  # Variabile globale


def SCC(g):
    dfs(g)
    trMatrix = g.matrix.transpose()  # calcolo la trasposta di g
    listScc = extendedDFS(g, trMatrix)
    return listScc


def extendedDFS(g, trMatrix):
    listScc = []  # ho una lista di scc composta da liste di vertici
    vf = []
    for i in range(g.v):
        vf.append(g.listVertices[i].f)  # inserisco in una lista tutti gli u.f
        g.listVertices[i].color = "W"
        g.listVertices[i].pi = None
    for j in range(g.v):
        maxFIndex = vf.index(max(vf))  # indico u.f maggiore
        u = g.listVertices[maxFIndex]  # prende dalla lista degli u.f il maggiore
        vf.pop(maxFIndex)  # toglie dalla lista il vertice con u.f maggiore
        if u.color == "W":
            listScc.append(extendedDfsVisit(g, trMatrix, u))
    return listScc


def extendedDfsVisit(g, trMatrix, u):
    scc = []
    extendedDfsVisitAux(g, trMatrix, u, scc)
    return scc


def extendedDfsVisitAux(g, trMatrix, u, scc):
    scc.append(u)
    global time
    time = time + 1
    u.d = time
    u.color = "G"
    for j in range(g.v):
        if trMatrix[u.id][j] == 1:  # scopre i nodi adiacenti
            v = g.listVertices[j]
            if v.color == "W":
                v.pi = u
                extendedDfsVisitAux(g, trMatrix, v, scc)
    u.color = "B"
    time = time + 1
    u.f = time
    return scc
