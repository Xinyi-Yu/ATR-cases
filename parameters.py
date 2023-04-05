
Tc = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
theta = [-3,-2,-1,0,1,2,3]
# theta = [-2,-1,0,1,2]
# theta = [-1,0,1]
# theta = [0]

T = 20
num = 4
theta1 = theta[0]
theta2 = theta[-1]
T_x = T+1+theta2-theta1
t_start = 0-theta1
Theta = len(theta)*len(theta)

umax = 2.5
vmax = 2.5

mu1x = [3.5, 6.5]
mu1y = [3, 6]
mu2x = [0, 3]
mu2y = [7, 10]
mu3x = [7, 10]
mu3y = [7, 10]

# mode: 1 means constraint functions and 2 means STL tasks
mode = 1
M = 10000

f1_t = [6, 9]
f2_t = [17,20]

FG_t = [15,17,0,3]
G1_t = [6, 9]
G2_t = [6, 9]
G1_len = G1_t[1] - G1_t[0] + 1
G2_len = G2_t[1] - G2_t[0] + 1
FG_Flen = FG_t[1]- FG_t[0] + 1
FG_Glen = FG_t[3]- FG_t[2] + 1
FG_len = FG_t[1] + FG_t[3] - FG_t[0] + 1

shiftlist = []
for kappa1 in theta:
    for kappa2 in theta:
        shiftlist.append((kappa1, kappa2))

D = 1