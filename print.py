import numpy as np
import matplotlib.pyplot as plt
from parameters import *


def PrintSol(state):
    path1 = []
    path2 = []
    for i in range(0, T+1):
        path1.append([i, state[i, 0]])
        path2.append([i, state[i, 1]])

    path1 = np.array(path1)
    path2 = np.array(path2)

    ax = plt.gca()
    plt.scatter(path1[:, 0], path1[:, 1], c='b')
    plt.plot(path1[:, 0], path1[:, 1], c='b', linewidth=1.3)
    plt.scatter(path2[:, 0], path2[:, 1], c='r')
    plt.plot(path2[:, 0], path2[:, 1], c='r', linewidth=1.3)
    plt.savefig('./case1.svg')