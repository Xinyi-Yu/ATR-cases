import numpy as np
import matplotlib.pyplot as plt
from parameters import *


def PrintSol(state):
    path = []
    for n in range(0, num):
        path.append([])
        for i in range(0, T+1):
            path[n].append([i, state[i, n]])
        path[n] = np.array(path[n]) 
        plt.scatter(path[n][ :, 0], path[n][:, 1])
        plt.plot(path[n][ :, 0], path[n][:, 1], linewidth=1.3)

    plt.savefig('./case.png')
    plt.show()
