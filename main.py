from gurobipy import *
import time
from print import *
from parameters import *


time_start = time.time()

ATR = Model("simple_case")
ATR.setParam('OutputFlag', 0)   # close log information

# Create variables
x = ATR.addVars(T+1, 2, lb=-xmax, ub=xmax, vtype=GRB.CONTINUOUS, name="state") 
u = ATR.addVars(T, 2, lb=-umax, ub=umax, vtype=GRB.CONTINUOUS, name="control input")  

# system model constraints
ATR.addConstrs((x[i, 0] == x[i-1, 0] + u[i-1, 0] for i in range(1, T+1)), 'state of agent 1')
ATR.addConstrs((x[i, 1] == x[i-1, 1] + u[i-1, 1] for i in range(1, T+1)), 'state of agent 2')
ATR.addConstrs((x[0, i] == 0 for i in range(0, 2)), 'initial state of two agents')

# ATR constraints in step 1
z1 = ATR.addVars(c_span, shift, shift, vtype=GRB.BINARY, name="binary variables in step 1")
ATR.addConstrs((x[k+i-theta, 0] - x[k+j-theta, 1] - 1 <= M * z1[k-c_start, i, j] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift)))
ATR.addConstrs((-(x[k+i-theta, 0] - x[k+j-theta, 1] - 1) <= M * (1 - z1[k-c_start, i, j]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift)))

# ATR constraints in step 2
z2 = ATR.addVars(shift, shift, vtype=GRB.BINARY, name="binary variables in step 2")
ATR.addConstrs((z2[i, j] <= z1[k-c_start, i, j] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift)))
ATR.addConstrs((z2[i, j] >= 1 - c_span + sum(z1[k-c_start, i, j] for k in range(c_start, c_end+1)) for i in range(0, shift) for j in range(0, shift)))

# ATR constraints in step 3
z3 = ATR.addVars(1, 1, vtype=GRB.BINARY, name="binary variables in step 3")
ATR.addConstrs((z3[0, 0] <= z2[i, j] for i in range(0, shift) for j in range(0, shift)))
ATR.addConstr(z3[0, 0] >= 1 - shift*shift + sum(z2[i, j] for i in range(0, shift) for j in range(0, shift)))

# ATR constraints
ATR.addConstr(z3[0, 0] == 1, name="specification constraint")

# Set objective
obj = ATR.addVar(vtype=GRB.CONTINUOUS, name="obj")
ATR.addConstr(obj == sum(u[i, 0]*u[i, 0] + u[i,1]*u[i,1] for i in range(0, T)), "minimum energy")
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





