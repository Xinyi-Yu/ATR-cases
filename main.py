from gurobipy import *
import time
from print import *
from parameters import *
from constraints import *



time_start = time.time()

ATR = Model("simple_case")
ATR.setParam('OutputFlag', 0)   # close log information

# create variables
x = ATR.addVars(T+1, num, lb=-xmax, ub=xmax, vtype=GRB.CONTINUOUS, name="state") 
u = ATR.addVars(T, num, lb=-umax, ub=umax, vtype=GRB.CONTINUOUS, name="control input")  

# add specification constraints
addConstr(ATR, x, u)

# set objective
obj = ATR.addVar(vtype=GRB.CONTINUOUS, name="obj")
ATR.addConstr(obj == sum(sum(u[i, n]*u[i, n] for n in range(0, num)) for i in range(0, T)), "minimum energy")
ATR.setObjective(obj, GRB.MINIMIZE)

ATR.optimize()
print("Time cost:", time.time() - time_start)

if ATR.status == GRB.Status.OPTIMAL:
    state = ATR.getAttr('x', x)
else:
    print('Optimization was stopped with status ' + str(ATR.status))
    sys.exit(0)

print('Obj:', ATR.objVal)

PrintSol(state)





