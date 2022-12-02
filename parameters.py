
# system parameters
# 0 means linear system x_{k+1} = x_k + u_k
# 1 means nonlinear system x_{k+1} = 0.94*x_k + 0.08*(55-x_k)u_k
SysMode = 0 

if SysMode == 0:
    umax = 2
    umin = -2
else:
    umax = 1
    umin = 0
xmax = 10





# specification parameters
theta = 5                     # required temporal robustness
c_start = 1 + theta           # starting time of specifications
c_span = 11                    # time span of specifications
c_end = c_start + c_span -1   # ending time of specifications
T = c_end + theta             # terminate time






# agent number
# currently, this project can only support num=2,3,4
num = 2                






# others
shift = 2*theta + 1
M = 100000000 