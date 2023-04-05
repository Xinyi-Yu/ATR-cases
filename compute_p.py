from parameters import *


def ComputeP():
    pairlist = []

    for i in Tc:
        for kappa1 in theta:
            for kappa2 in theta:
                temp = (i, (kappa1, kappa2))
                pairlist.append(temp)

    P = [[pairlist.pop()]] # set of pair set

    while len(pairlist) != 0:
        temp = pairlist.pop()
        flag = 0
        for pairset in P: 
            if (temp[0]+temp[1][0] == pairset[0][0]+pairset[0][1][0]) and (temp[0]+temp[1][1] == pairset[0][0]+pairset[0][1][1]):
                P[P.index(pairset)].append(temp)
                flag = 1
                break
        if flag == 0:
            P.append([temp])

    Pdict={}
    for i in range(0, len(P)):
        Pdict[i] = P[i]

    return Pdict


def isin(timenum, pairsetlist):
    flag = 0
    for pairset in pairsetlist:
        if timenum == pairset[0]:
            return True
    if flag == 0:
        return False
    

def findindex(pair, Pdict):
    for i in range(len(Pdict)):
        if pair in Pdict[i]:
            return i




