from gurobipy import *
import time
from print import *
from parameters import *
from constraints import *
from compute_p import *



ATR = Model("case2")
ATR.setParam('OutputFlag', 0)   # close log information
ATR.setParam('DualReductions', 0)
if mode == 2:
    ATR.setParam('NonConvex', 2)

# create variables
x1 = ATR.addVars(T_x, num, lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="state1") 
u1 = ATR.addVars(T, 2, lb=-umax, ub=umax, vtype=GRB.CONTINUOUS, name="control input1")  
x2 = ATR.addVars(T_x, num, lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="state2") 
u2 = ATR.addVars(T, 2, lb=-umax, ub=umax, vtype=GRB.CONTINUOUS, name="control input2")  

# add specification constraints
Pdict = ComputeP()
addConstr(ATR, x1, u1, x2, u2, Pdict)

# set objective
ATR.setObjective(sum(sum(0.1*(x1[t_start+i, 1]*x1[t_start+i, 1] + x1[t_start+i, 3]*x1[t_start+i, 3] + x2[t_start+i, 1]*x2[t_start+i, 1] + x2[t_start+i, 3]*x2[t_start+i, 3]) + 0.9*(u1[i, n]*u1[i, n] + u2[i, n]*u2[i, n]) for n in range(2)) for i in range(0, T)), GRB.MINIMIZE)

# optimize
time_start = time.time()
ATR.optimize()
print("Time cost:", time.time() - time_start)
if ATR.status == GRB.OPTIMAL:
    stater = ATR.getAttr('x', x1)
    stateb = ATR.getAttr('x', x2)
    PrintSol(stater, stateb)
else:
    print('Optimization was stopped with status' + str(ATR.status))
    sys.exit(0)







