import matplotlib.pyplot as plt
from parameters import *
from matplotlib.patches import Rectangle
import numpy as np

def PrintSol(stater, stateb):
    path1 = []
    path2 = []
    for i in range(t_start, t_start+T+1):
        path1.append([stater[i, 0], stater[i, 2]])
    for i in range(t_start, t_start+T+1):
        path2.append([stateb[i, 0], stateb[i, 2]])
    path1 = np.array(path1)
    path2 = np.array(path2)

    # draw the map
    a1 = Rectangle((mu1x[0], mu1y[0]), mu1x[1] - mu1x[0], mu1y[1] - mu1y[0], facecolor ="cyan", alpha=0.2)
    a2 = Rectangle((mu2x[0], mu2y[0]), mu2x[1] - mu2x[0], mu2y[1] - mu2y[0], facecolor ="grey", alpha=0.3)
    a3 = Rectangle((mu3x[0], mu3y[0]), mu3x[1] - mu3x[0], mu3y[1] - mu3y[0], facecolor ="grey", alpha=0.3)
    plt.figure(figsize=(10, 10))
    ax = plt.gca()
    ax.add_patch(a1)
    ax.add_patch(a2)
    ax.add_patch(a3)
    
    # The following three lines are used to avoid the bug "Type 3 font" when submitting the paper in CSS paperplaza
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rcParams['pdf.fonttype'] = 42

    plt.text(4.4, 3.1, r"$\mu_{1}\geq 0$", family='Calibri', fontsize=24, color='black')
    plt.text(1, 7.1, r"$\mu_{2}\geq 0$", family='Calibri', fontsize=24, color='black')
    plt.text(8, 7.1, r"$\mu_{3}\geq 0$", family='Calibri', fontsize=24, color='black')

    plt.plot(path1[ :, 0], path1[:, 1], color='red', linewidth=1.3)
    plt.plot(path2[ :, 0], path2[:, 1], color='blue', linewidth=1.3)
    plt.scatter(path1[ :, 0], path1[:, 1], color='red', s=20)
    plt.scatter(path2[ :, 0], path2[:, 1], color='blue', s=20)
    plt.scatter(path1[0, 0], path1[0, 1], color='red', s=20, marker = 's')
    plt.scatter(path2[0, 0], path2[0, 1], color='blue', s=20, marker = 's')
    

    plt.xlabel('x/m', size = 24)
    plt.ylabel('y/m', size = 24)
    plt.axis([0, 10, 0, 10])
    plt.xticks(size = 24)
    plt.yticks(size = 24)
    

    plt.savefig('test.pdf')
    plt.show()

