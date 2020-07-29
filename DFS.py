time = 0  # Variabile globale


def dfs(g):
    for i in range(g.v):
        if g.listVertices[i].color == "W":
            dfsVisit(g, g.listVertices[i])


def dfsVisit(g, u):
    global time
    time += 1
    u.d = time
    u.color = "G"
    for i in range(g.v):
        if g.matrix[u.id][i]:
            if g.listVertices[i].color == "W":
                g.listVertices[i].pi = u
                dfsVisit(g, g.listVertices[i])
    u.color = "B"
    time += 1
    u.f = time
