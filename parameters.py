
# parameters
xmax = 10
umax = 1
M = 1000000000 

theta = 5                     # required temporal robustness
c_start = 1 + theta           # starting time of specifications
c_span = 10                 # time span of specifications
c_end = c_start + c_span -1   # ending time of specifications
T = c_end + theta             # terminate time

shift = 2*theta + 1