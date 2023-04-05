from parameters import *
from gurobipy import *
from compute_p import *

def addConstr(ATR, x1, u1, x2, u2, Pdict):
    # system model constraints
    # initial state
    ATR.addConstr((x1[t_start, 0] == 1), '1')
    ATR.addConstr(x1[t_start, 2] == 1)
    ATR.addConstrs(x1[t_start, n] == 0 for n in [1,3])
    ATR.addConstr(x2[t_start, 0] == 9)
    ATR.addConstr(x2[t_start, 2] == 1)
    ATR.addConstrs(x2[t_start, n] == 0 for n in [1,3])
    # model [1,T]
    ATR.addConstrs(x1[t_start+i+1, 0] == x1[t_start+i, 0] + x1[t_start+i, 1] + 0.5*u1[i, 0] for i in range(0, T))
    ATR.addConstrs(x1[t_start+i+1, 1] == x1[t_start+i, 1] + u1[i, 0] for i in range(0, T))
    ATR.addConstrs(x1[t_start+i+1, 2] == x1[t_start+i, 2] + x1[t_start+i, 3] + 0.5*u1[i, 1] for i in range(0, T))
    ATR.addConstrs(x1[t_start+i+1, 3] == x1[t_start+i, 3] + u1[i, 1] for i in range(0, T))
    ATR.addConstrs(x2[t_start+i+1, 0] == x2[t_start+i, 0] + x2[t_start+i, 1] + 0.5*u2[i, 0] for i in range(0, T))
    ATR.addConstrs(x2[t_start+i+1, 1] == x2[t_start+i, 1] + u2[i, 0] for i in range(0, T))
    ATR.addConstrs(x2[t_start+i+1, 2] == x2[t_start+i, 2] + x2[t_start+i, 3] + 0.5*u2[i, 1] for i in range(0, T))
    ATR.addConstrs(x2[t_start+i+1, 3] == x2[t_start+i, 3] + u2[i, 1] for i in range(0, T))
    # state shift
    ATR.addConstrs(x1[k, n] == x1[t_start, n] for n in range(num) for k in range(0, -theta1))
    ATR.addConstrs(x2[k, n] == x2[t_start, n] for n in range(num) for k in range(0, -theta1))
    ATR.addConstrs(x1[t_start+i+1, n] == x1[t_start+i, n] for n in range(num) for i in range(T, T+theta2))
    ATR.addConstrs(x2[t_start+i+1, n] == x2[t_start+i, n] for n in range(num) for i in range(T, T+theta2))

    # physical constraints
    ATR.addConstrs(x1[k, 0] >= 0 for k in range(0, T_x))
    ATR.addConstrs(x1[k, 0] <= 10 for k in range(0, T_x))
    ATR.addConstrs(x1[k, 1] >= -vmax for k in range(0, T_x))
    ATR.addConstrs(x1[k, 1] <= vmax for k in range(0, T_x))
    ATR.addConstrs(x1[k, 2] >= 0 for k in range(0, T_x))
    ATR.addConstrs(x1[k, 2] <= 10 for k in range(0, T_x))
    ATR.addConstrs(x1[k, 3] >= -vmax for k in range(0, T_x))
    ATR.addConstrs(x1[k, 3] <= vmax for k in range(0, T_x))
    ATR.addConstrs(x2[k, 0] >= 0 for k in range(0, T_x))
    ATR.addConstrs(x2[k, 0] <= 10 for k in range(0, T_x))
    ATR.addConstrs(x2[k, 1] >= -vmax for k in range(0, T_x))
    ATR.addConstrs(x2[k, 1] <= vmax for k in range(0, T_x))
    ATR.addConstrs(x2[k, 2] >= 0 for k in range(0, T_x))
    ATR.addConstrs(x2[k, 2] <= 10 for k in range(0, T_x))
    ATR.addConstrs(x2[k, 3] >= -vmax for k in range(0, T_x))
    ATR.addConstrs(x2[k, 3] <= vmax for k in range(0, T_x))
    
    # function constraints
    if mode == 1:
        f1_count = 0
        f1_list = []
        f1_dict = {}
        for i in range(len(Pdict)):
            for k in range(f1_t[0], f1_t[1]+1):
                if (isin(k, Pdict[i]) == True):
                    f1_dict[f1_count] = Pdict[i]
                    f1_list.append(f1_count)
                    f1_count = f1_count + 1
                    break

        for i in f1_list:
            time = f1_dict[i][0][0]
            shift1 = f1_dict[i][0][1][0]
            shift2 = f1_dict[i][0][1][1]
            ATR.addConstr(x1[t_start+time+shift1, 0] - mu1x[0] >= 0)
            ATR.addConstr(- x1[t_start+time+shift1, 0] + mu1x[1] >= 0)
            ATR.addConstr(x1[t_start+time+shift1, 2] - mu1y[0] >= 0)
            ATR.addConstr(- x1[t_start+time+shift1, 2] + mu1y[1] >= 0) 
            ATR.addConstr(D-((x2[t_start+time+shift2, 0]-x1[t_start+time+shift1, 0])*(x2[t_start+time+shift2, 0]-x1[t_start+time+shift1, 0]) + (x2[t_start+time+shift2, 2]-x1[t_start+time+shift1, 2])*(x2[t_start+time+shift2, 2]-x1[t_start+time+shift1, 2])) >= 0)
            

        f2_count = 0
        f2_list = []
        f2_dict = {}
        for i in range(len(Pdict)):
            for k in range(f2_t[0], f2_t[1]+1):
                if (isin(k, Pdict[i]) == True):
                    f2_dict[f2_count] = Pdict[i]
                    f2_list.append(f2_count)
                    f2_count = f2_count + 1
                    break
    
        for i in f2_list:
            time = f2_dict[i][0][0]
            shift1 = f2_dict[i][0][1][0]
            shift2 = f2_dict[i][0][1][1]
            ATR.addConstr(x1[t_start+time+shift1, 0] - mu2x[0] >= 0)
            ATR.addConstr(- x1[t_start+time+shift1, 0] + mu2x[1] >= 0)
            ATR.addConstr(x1[t_start+time+shift1, 2] - mu2y[0] >= 0)
            ATR.addConstr(- x1[t_start+time+shift1, 2] + mu2y[1] >= 0)
            ATR.addConstr(x2[t_start+time+shift1, 0] - mu3x[0] >= 0)
            ATR.addConstr(- x2[t_start+time+shift1, 0] + mu3x[1] >= 0)
            ATR.addConstr(x2[t_start+time+shift1, 2] - mu3y[0] >= 0)
            ATR.addConstr(- x2[t_start+time+shift1, 2] + mu3y[1] >= 0)


    # STL tasks
    else:
        G1_count = 0
        G1_list = []
        G1_dict = {}
        for i in range(len(Pdict)):
            for k in range(G1_t[0], G1_t[1]+1):
                if (isin(k, Pdict[i]) == True):
                    G1_dict[G1_count] = Pdict[i]
                    G1_list.append(G1_count)
                    G1_count = G1_count + 1
                    break

        G1 = ATR.addVars(Theta, vtype=GRB.BINARY)
        G1_mu = ATR.addVars(G1_count, vtype=GRB.BINARY) 
        G1_4 = ATR.addVars(G1_count, 4, vtype=GRB.BINARY)   
        
        for i in range(Theta):
            ATR.addConstrs(G1[i] <= G1_mu[findindex((k,shiftlist[i]), G1_dict)] for k in range(G1_t[0], G1_t[1]+1))
            ATR.addConstr(G1[i] >= 1- G1_len +sum(G1_mu[findindex((k,shiftlist[i]), G1_dict)] for k in range(G1_t[0], G1_t[1]+1)))
        for i in G1_list:
            ATR.addConstrs(G1_mu[i] <= G1_4[i, p] for p in range(4))
            ATR.addConstr(G1_mu[i] >=- 3 + sum(G1_4[i, p] for p in range(4)))
            time = G1_dict[i][0][0]
            shift1 = G1_dict[i][0][1][0]
            shift2 = G1_dict[i][0][1][1]
            ATR.addConstr(x1[t_start+time+shift1, 0] - mu2x[0] <= M * G1_4[i, 0])
            ATR.addConstr(-x1[t_start+time+shift1, 0] + mu2x[0] <= M * (1 - G1_4[i, 0]))
            ATR.addConstr(-x1[t_start+time+shift1, 0] + mu2x[1] <= M * G1_4[i, 1])
            ATR.addConstr(x1[t_start+time+shift1, 0] - mu2x[1] <= M * (1 - G1_4[i, 1]))
            ATR.addConstr(x1[t_start+time+shift1, 2] - mu2y[0] <= M * G1_4[i, 2])
            ATR.addConstr(-x1[t_start+time+shift1, 2] + mu2y[0] <= M * (1 - G1_4[i, 2]))
            ATR.addConstr(-x1[t_start+time+shift1, 2] + mu2y[1] <= M * G1_4[i, 3])
            ATR.addConstr(x1[t_start+time+shift1, 2] - mu2y[1] <= M * (1 - G1_4[i, 3]))


        G2_count = 0
        G2_list = []
        G2_dict = {}
        for i in range(len(Pdict)):
            for k in range(G2_t[0], G2_t[1]+1):
                if (isin(k, Pdict[i]) == True):
                    G2_dict[G2_count] = Pdict[i]
                    G2_list.append(G2_count)
                    G2_count = G2_count + 1
                    break

        G2 = ATR.addVars(Theta, vtype=GRB.BINARY)
        G2_mu = ATR.addVars(G2_count, vtype=GRB.BINARY)  # mu
        G2_4 = ATR.addVars(G2_count, 4, vtype=GRB.BINARY)   
        
        for i in range(Theta):
            ATR.addConstrs(G2[i] <= G2_mu[findindex((k,shiftlist[i]), G2_dict)] for k in range(G2_t[0], G2_t[1]+1))
            ATR.addConstr(G2[i] >= 1- G2_len +sum(G2_mu[findindex((k,shiftlist[i]), G2_dict)] for k in range(G2_t[0], G2_t[1]+1)))
        for i in G2_list:
            ATR.addConstrs(G2_mu[i] <= G2_4[i, p] for p in range(4))
            ATR.addConstr(G2_mu[i] >=- 3 + sum(G2_4[i, p] for p in range(4)))
            time = G2_dict[i][0][0]
            shift1 = G2_dict[i][0][1][0]
            shift2 = G2_dict[i][0][1][1]
            ATR.addConstr(x2[t_start+time+shift2, 0] - mu3x[0] <= M * G2_4[i, 0])
            ATR.addConstr(-x2[t_start+time+shift2, 0] + mu3x[0] <= M * (1 - G2_4[i, 0]))
            ATR.addConstr(-x2[t_start+time+shift2, 0] + mu3x[1] <= M * G2_4[i, 1])
            ATR.addConstr(x2[t_start+time+shift2, 0] - mu3x[1] <= M * (1 - G2_4[i, 1]))
            ATR.addConstr(x2[t_start+time+shift2, 2] - mu3y[0] <= M * G2_4[i, 2])
            ATR.addConstr(-x2[t_start+time+shift2, 2] + mu3y[0] <= M * (1 - G2_4[i, 2]))
            ATR.addConstr(-x2[t_start+time+shift2, 2] + mu3y[1] <= M * G2_4[i, 3])
            ATR.addConstr(x2[t_start+time+shift2, 2] - mu3y[1] <= M * (1 - G2_4[i, 3]))


        FG_count = 0
        FG_F_count = 0
        FG_list = []
        FG_F_list = []
        FG_dict = {}
        FG_F_dict = {}
        for i in range(len(Pdict)):
            for k in range(FG_t[0], FG_t[1]+FG_t[3]+1):
                if (isin(k, Pdict[i]) == True):
                    FG_dict[FG_count] = Pdict[i]
                    FG_list.append(FG_count)
                    FG_count = FG_count + 1
                    break
        for i in range(len(Pdict)):
            for k in range(FG_t[0], FG_t[1]+1):
                if (isin(k, Pdict[i]) == True):
                    FG_F_dict[FG_F_count] = Pdict[i]
                    FG_F_list.append(FG_F_count)
                    FG_F_count = FG_F_count + 1
                    break

        FG = ATR.addVars(Theta, vtype=GRB.BINARY, name='FG')
        G_nest = ATR.addVars(FG_F_count, vtype=GRB.BINARY, name='G_nest')
        FG_and = ATR.addVars(FG_count, vtype=GRB.BINARY, name='FG_and')  # mu
        FG_mu = ATR.addVars(FG_count, 2, vtype=GRB.BINARY, name='FG_mu')
        FG_4 = ATR.addVars(FG_count, 4, vtype=GRB.BINARY, name='FG_4')

        for i in range(Theta):
            ATR.addConstrs(FG[i] >= G_nest[findindex((k,shiftlist[i]), FG_F_dict)] for k in range(FG_t[0], FG_t[1]+1))
            ATR.addConstr(FG[i] <= sum(G_nest[findindex((k,shiftlist[i]), FG_F_dict)] for k in range(FG_t[0], FG_t[1]+1)))
        for i in FG_F_list:
            # the reason why we use "-1" is that if we use "0" and +j, it is easy to exceed 15 since it is sorted from high to low in the list of pairs. 
            ATR.addConstrs(G_nest[i] <= FG_and[findindex((FG_F_dict[i][-1][0]+j, FG_F_dict[i][-1][1]), FG_dict)] for j in range(FG_t[2], FG_t[3]+1))
            ATR.addConstr(G_nest[i] >= 1-FG_Glen + sum(FG_and[findindex((FG_F_dict[i][-1][0]+j, FG_F_dict[i][-1][1]), FG_dict)] for j in range(FG_t[2], FG_t[3]+1)))
        for i in FG_list:
            ATR.addConstrs(FG_and[i] <= FG_mu[i, p] for p in range(2))
            ATR.addConstr(FG_and[i] >= -1 + sum(FG_mu[i, p] for p in range(2)))
            ATR.addConstrs(FG_and[i] <= FG_mu[i, p] for p in range(2))
            ATR.addConstr(FG_and[i] >= -1 + sum(FG_mu[i, p] for p in range(2)))
            ATR.addConstrs(FG_mu[i, 0] <= FG_4[i, p] for p in range(4))
            ATR.addConstr(FG_mu[i, 0] >=- 3 + sum(FG_4[i, p] for p in range(4)))
            time = FG_dict[i][0][0]
            shift1 = FG_dict[i][0][1][0]
            shift2 = FG_dict[i][0][1][1]
            ATR.addConstr(D-((x2[t_start+time+shift2, 0]-x1[t_start+time+shift1, 0])*(x2[t_start+time+shift2, 0]-x1[t_start+time+shift1, 0]) + (x2[t_start+time+shift2, 2]-x1[t_start+time+shift1, 2])*(x2[t_start+time+shift2, 2]-x1[t_start+time+shift1, 2])) <= M * FG_mu[i, 1])
            ATR.addConstr(-(D-((x2[t_start+time+shift2, 0]-x1[t_start+time+shift1, 0])*(x2[t_start+time+shift2, 0]-x1[t_start+time+shift1, 0]) + (x2[t_start+time+shift2, 2]-x1[t_start+time+shift1, 2])*(x2[t_start+time+shift2, 2]-x1[t_start+time+shift1, 2]))) <= M * (1 - FG_mu[i, 1]))
            ATR.addConstr(x1[t_start+time+shift1, 0] - mu1x[0] <= M * FG_4[i, 0])
            ATR.addConstr(-x1[t_start+time+shift1, 0] + mu1x[0] <= M * (1 - FG_4[i, 0]))
            ATR.addConstr(-x1[t_start+time+shift1, 0] + mu1x[1] <= M * FG_4[i, 1])
            ATR.addConstr(x1[t_start+time+shift1, 0] - mu1x[1] <= M * (1 - FG_4[i, 1]))
            ATR.addConstr(x1[t_start+time+shift1, 2] - mu1y[0] <= M * FG_4[i, 2])
            ATR.addConstr(-x1[t_start+time+shift1, 2] + mu1y[0] <= M * (1 - FG_4[i, 2]))
            ATR.addConstr(-x1[t_start+time+shift1, 2] + mu1y[1] <= M * FG_4[i, 3])
            ATR.addConstr(x1[t_start+time+shift1, 2] - mu1y[1] <= M * (1 - FG_4[i, 3]))
        

        z_Phi = ATR.addVars(Theta, vtype=GRB.BINARY)
        ATR.addConstrs(z_Phi[i] == 1 for i in range(Theta))
        ATR.addConstrs(z_Phi[i] <= G1[i] for i in range(Theta))
        ATR.addConstrs(z_Phi[i] <= G2[i] for i in range(Theta))
        ATR.addConstrs(z_Phi[i] <= FG[i] for i in range(Theta))
        ATR.addConstrs(z_Phi[i] >= -2 + G1[i] + G2[i] + FG[i] for i in range(Theta))
