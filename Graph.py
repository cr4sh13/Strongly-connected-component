import numpy as np
from Vertice import *


class Graph:

    def __init__(self, vertices, prob):
        self.v = vertices
        self.matrix = np.zeros((vertices, vertices), dtype=int)
        prob = prob / 100
        for i in range(self.v):
            for j in range(self.v):
                if i != j:
                    self.matrix[i][j] = np.random.choice(np.arange(0, 2), p=[1 - prob, prob])
        self.listVertices = []
        for i in range(self.v):
            self.listVertices.append(Vertice(i))


