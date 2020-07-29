from SCC import *
import matplotlib.pyplot as plt
from Graph import *


def testBase():
    vertices = 50

    # test con probabilità 0%
    prob = 0
    graphTest1 = Graph(vertices, prob)
    numSccTest1 = len(SCC(graphTest1))
    print(
        "Numero di SCC trovate in un grafo da 50 nodi con probabilità di presenza degli archi pari a 0 --> %d" % numSccTest1)

    # test con probabilità 100%
    prob = 100
    graphTest2 = Graph(vertices, prob)
    numSccTest2 = len(SCC(graphTest2))
    print(
        "Numero di SCC trovate in un grafo da 50 nodi con probabilità di presenza degli archi pari a 100 --> %d" % numSccTest2)


def testIncProb():  # test su grafo da 50 nodi con incremento probabilità
    listScc = []
    vertices = 50
    X = []  # serve per il plot

    for i in range(10):
        numOfScc = []
        for p in range(101):  # aumento la probabilità di presenza di archi
            graph = Graph(vertices, p)
            scc = SCC(graph)
            numOfScc.append(len(scc))  # numero di scc trovate
        listScc.append(numOfScc)

    for j in range(101):
        X.append(j)

    plotMean = []
    length = len(listScc)

    for k in range(len(listScc[0])):  # calcolo la media
        media = 0
        for c in range(length):
            media += listScc[c].pop(0)
        media = media / length
        plotMean.append(media)

    plt.figure()
    plt.plot(X, plotMean, 'b', label='Media test')
    plt.xlabel("Probabilità di presenza degli archi in %")
    plt.ylabel("Numero SCC")

    plt.legend(loc='upper right')
    plt.show()


def testIncNodes(probability):  # test incrementando il numero di nodi con probabilità fissa
    listScc = []
    prob = probability
    X = []  # serve per il plot

    for i in range(10):
        numOfScc = []
        for k in range(100):  # aumento il numero di vertici fino ad un max di 50
            graph = Graph(k, prob)
            scc = SCC(graph)
            numOfScc.append(len(scc))  # numero di scc trovate
        listScc.append(numOfScc)

    for j in range(100):
        X.append(j)

    plotMean = []
    length = len(listScc)

    for k in range(len(listScc[0])):  # calcolo la media
        media = 0
        for c in range(length):
            media += listScc[c].pop(0)
        media = media / length
        plotMean.append(media)

    plt.figure()
    plt.plot(X, plotMean, 'b', label='Media test')
    plt.xlabel("Numero di nodi")
    plt.ylabel("Numero SCC")
    plt.legend(loc='upper right')
    plt.show()


# testBase()
# testIncProb()
# testIncNodes(15)

