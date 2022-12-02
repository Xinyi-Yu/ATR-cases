from parameters import *
from gurobipy import *

def addConstr(ATR, x, u):
    # system model constraints
    for n in range(0, num):
        ATR.addConstr(x[0, n] == 0, 'initial state')
        if SysMode == 0:
            ATR.addConstrs((x[i, n] == x[i-1, n] + u[i-1, n] for i in range(1, T+1)), 'state of agent n')
        else:
            ATR.setParam('NonConvex', 2)
            ATR.addConstrs((x[i, n] == 0.94*x[i-1, n] + 4.4*u[i-1, n] - 0.08*x[i-1, n]*u[i-1, n] for i in range(1, T+1)), 'state of agent n')


    if num == 2:
        # ATR constraints in step 1
        z1 = ATR.addVars(c_span, shift, shift, vtype=GRB.BINARY, name="binary variables in step 1")
        ATR.addConstrs(x[k+j-theta, 1] - x[k+i-theta, 0] - 1 <= M * z1[k-c_start, i, j] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift))
        ATR.addConstrs(-(x[k+j-theta, 1] - x[k+i-theta, 0] - 1) <= M * (1 - z1[k-c_start, i, j]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift))

        # ATR constraints in step 2
        z2 = ATR.addVars(shift, shift, vtype=GRB.BINARY, name="binary variables in step 2")
        ATR.addConstrs(z2[i, j] <= z1[k-c_start, i, j] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift))
        ATR.addConstrs(z2[i, j] >= 1 - c_span + sum(z1[k-c_start, i, j] for k in range(c_start, c_end+1)) for i in range(0, shift) for j in range(0, shift))

        # ATR constraints in step 3
        z3 = ATR.addVars(1, 1, vtype=GRB.BINARY, name="binary variables in step 3")
        ATR.addConstrs(z3[0, 0] <= z2[i, j] for i in range(0, shift) for j in range(0, shift))
        ATR.addConstr(z3[0, 0] >= 1 - shift*shift + sum(z2[i, j] for i in range(0, shift) for j in range(0, shift)))

        # ATR constraints
        ATR.addConstr(z3[0, 0] == 1, name="specification constraint")


    if num == 3:
        # ATR constraints in step 1
        z1_2 = ATR.addVars(c_span, shift, shift, shift, 2, vtype=GRB.BINARY)
        ATR.addConstrs(x[k+j-theta, 1] - x[k+i-theta, 0] - 1 <= M * z1_2[k-c_start, i, j, p, 0] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))
        ATR.addConstrs(-(x[k+j-theta, 1] - x[k+i-theta, 0] - 1) <= M * (1 - z1_2[k-c_start, i, j, p, 0]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))
        ATR.addConstrs(x[k+p-theta, 2] - x[k+j-theta, 1] - 1 <= M * z1_2[k-c_start, i, j, p, 1] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))
        ATR.addConstrs(-(x[k+p-theta, 2] - x[k+j-theta, 1] - 1) <= M * (1 - z1_2[k-c_start, i, j, p, 1]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))

        z1 = ATR.addVars(c_span, shift, shift, shift, vtype=GRB.BINARY, name="binary variables in step 1")
        ATR.addConstrs(z1[k, i, j, p] <= z1_2[k, i, j, p, n] for k in range(0, c_span) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for n in range(0, 2))
        ATR.addConstrs(z1[k, i, j, p] >= -1 + sum(z1_2[k, i, j, p, n] for n in range(0, 2)) for k in range(0, c_span) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))

        # ATR constraints in step 2
        z2 = ATR.addVars(shift, shift, shift, vtype=GRB.BINARY, name="binary variables in step 2")
        ATR.addConstrs(z2[i, j, p] <= z1[k-c_start, i, j, p] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))
        ATR.addConstrs(z2[i, j, p] >= 1 - c_span + sum(z1[k-c_start, i, j, p] for k in range(c_start, c_end+1)) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))

        # ATR constraints in step 3
        z3 = ATR.addVars(1, 1, vtype=GRB.BINARY, name="binary variables in step 3")
        ATR.addConstrs(z3[0, 0] <= z2[i, j, p] for i in range(0, shift) for j in range(0, shift) for p in range(0, shift))
        ATR.addConstr(z3[0, 0] >= 1 - shift*shift*shift + sum(z2[i, j, p] for i in range(0, shift) for j in range(0, shift) for p in range(0, shift)))

        # ATR constraints
        ATR.addConstr(z3[0, 0] == 1, name="specification constraint")

    if num == 4:
        # ATR constraints in step 1
        z1_3 = ATR.addVars(c_span, shift, shift, shift, shift, 3, vtype=GRB.BINARY)
        ATR.addConstrs(x[k+j-theta, 1] - x[k+i-theta, 0] - 1 <= M * z1_3[k-c_start, i, j, p, q, 0] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstrs(-(x[k+j-theta, 1] - x[k+i-theta, 0] - 1) <= M * (1 - z1_3[k-c_start, i, j, p, q, 0]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstrs(x[k+p-theta, 2] - x[k+j-theta, 1] - 1 <= M * z1_3[k-c_start, i, j, p, q, 1] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstrs(-(x[k+p-theta, 2] - x[k+j-theta, 1] - 1) <= M * (1 - z1_3[k-c_start, i, j, p, q, 1]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstrs(x[k+q-theta, 3] - x[k+p-theta, 2] - 1 <= M * z1_3[k-c_start, i, j, p, q, 2] for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstrs(-(x[k+q-theta, 3] - x[k+p-theta, 2] - 1) <= M * (1 - z1_3[k-c_start, i, j, p, q, 2]) for k in range(c_start, c_end+1) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))


        z1 = ATR.addVars(c_span, shift, shift, shift, shift, vtype=GRB.BINARY, name="binary variables in step 1")
        ATR.addConstrs(z1[k, i, j, p, q] <= z1_3[k, i, j, p, q, n] for k in range(0, c_span) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift) for n in range(0, 3))
        ATR.addConstrs(z1[k, i, j, p, q] >= 1 - 3 + sum(z1_3[k, i, j, p, q, n] for n in range(0, 3)) for k in range(0, c_span) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))

        # ATR constraints in step 2
        z2 = ATR.addVars(shift, shift, shift, shift, vtype=GRB.BINARY, name="binary variables in step 2")
        ATR.addConstrs(z2[i, j, p, q] <= z1[k, i, j, p, q] for k in range(0, c_span) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstrs(z2[i, j, p, q] >= 1 - c_span + sum(z1[k, i, j, p, q] for k in range(0, c_span)) for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))

        # ATR constraints in step 3
        z3 = ATR.addVars(1, 1, vtype=GRB.BINARY, name="binary variables in step 3")
        ATR.addConstrs(z3[0, 0] <= z2[i, j, p, q] for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift))
        ATR.addConstr(z3[0, 0] >= 1 - shift*shift*shift*shift + sum(z2[i, j, p, q] for i in range(0, shift) for j in range(0, shift) for p in range(0, shift) for q in range(0, shift)))

        # ATR constraints
        ATR.addConstr(z3[0, 0] == 1, name="specification constraint")
