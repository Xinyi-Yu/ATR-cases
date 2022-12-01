import numpy as np
import matplotlib.pyplot as plt
from parameters import *


def PrintSol(state):
    if num == 2: 
        path1 = []
        path2 = []
        for i in range(0, T+1):
            path1.append([i, state[i, 0]])
            path2.append([i, state[i, 1]])

        path1 = np.array(path1)
        path2 = np.array(path2)

        ax = plt.gca()
        plt.scatter(path1[:, 0], path1[:, 1], c='b')
        plt.plot(path1[:, 0], path1[:, 1], c='b', linewidth=1.3, label="x1")
        plt.scatter(path2[:, 0], path2[:, 1], c='r')
        plt.plot(path2[:, 0], path2[:, 1], c='r', linewidth=1.3, label="x2")
        plt.legend()
        plt.savefig('./case1.png')
        plt.show()

    if num == 3: 
        path1 = []
        path2 = []
        path3 = []
        for i in range(0, T+1):
            path1.append([i, state[i, 0]])
            path2.append([i, state[i, 1]])
            path3.append([i, state[i, 2]])

        path1 = np.array(path1)
        path2 = np.array(path2)
        path3 = np.array(path3)

        # ax = plt.gca()
        plt.scatter(path1[:, 0], path1[:, 1], c='b')
        plt.plot(path1[:, 0], path1[:, 1], c='b', linewidth=1.3, label="x1")
        plt.scatter(path2[:, 0], path2[:, 1], c='r')
        plt.plot(path2[:, 0], path2[:, 1], c='r', linewidth=1.3, label="x2")
        plt.scatter(path3[:, 0], path3[:, 1], c='k')
        plt.plot(path3[:, 0], path3[:, 1], c='k', linewidth=1.3, label="x3")
        plt.legend()
        plt.savefig('./case2.png')
        plt.show()


    if num == 4: 
        path1 = []
        path2 = []
        path3 = []
        path4 = []
        for i in range(0, T+1):
            path1.append([i, state[i, 0]])
            path2.append([i, state[i, 1]])
            path3.append([i, state[i, 2]])
            path4.append([i, state[i, 3]])

        path1 = np.array(path1)
        path2 = np.array(path2)
        path3 = np.array(path3)
        path4 = np.array(path4)

        # ax = plt.gca()
        plt.scatter(path1[:, 0], path1[:, 1], c='b')
        plt.plot(path1[:, 0], path1[:, 1], c='b', linewidth=1.3, label="x1")
        plt.scatter(path2[:, 0], path2[:, 1], c='r')
        plt.plot(path2[:, 0], path2[:, 1], c='r', linewidth=1.3, label="x2")
        plt.scatter(path3[:, 0], path3[:, 1], c='k')
        plt.plot(path3[:, 0], path3[:, 1], c='k', linewidth=1.3, label="x3")
        plt.scatter(path4[:, 0], path4[:, 1], c='c')
        plt.plot(path4[:, 0], path4[:, 1], c='c', linewidth=1.3, label="x4")
        plt.legend()
        # plt.savefig('./case3.png')
        plt.show()