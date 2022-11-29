# Asynchronous Temporal Robustness (ATR)

The aim of this project is to explore how complex situations can be handled by our encoding methods. Given ATR bound $\theta$, number of agents $m$, time span of specifications $c_{span}$, our encoding method will introduce at most $(2\theta +1)^m (c_{span}+1)+1$ binary variables.

## Case 1: 

- Two agents
- System model: $x_{k+1} = x_k +u_k, x\in [-10,10], u \in [-1,1]$, with initial state $x^{\{1\}}_0=x^{\{2\}}_0=0$. (one-dimensional motion planning and the control input is its speed.)
- Specification:  
```math
c(x(t), t) = \left\{ \begin{array}{ll} 1  &\text{for all} \ t < c_{start} \  \text{and all} \ t > c_{end} \\ x^{\{1\}} - x^{\{2\}}-1 & \text{for all} \ t \in [c_{start}, c_{end}] \end{array} \right.
```
which implies that the distance between two vehicles should be larger than 1m.

- Required temporal robustness: $\theta$

- objective: minimize its energy.

- When $c_{span} = 10$ and $\theta=5$, here is the final results:  

![image](http://xinyi-yu.test.upcdn.net/case1.jpg!/scale/66)

- Results:

| Computation time | $c_{span} = 10$ | $c_{span} = 100$ | $c_{span} = 1000$ | $c_{span} = 10000$ |
| :--------------: | :-------------: | :--------------: | :---------------: | :----------------: |
|   $\theta = 5$   |      0.12s      |      1.05s       |       11.2s       |        117s        |
|  $\theta = 10$   |        -        |       4.4s       |        46s        |    memory error    |
|  $\theta = 50$   |        -        |      91.5s       |   memory error    |    memory error    |

### Remark: 

- For simplicity, we directly set $c_{start} = 1+\theta$, control horizon $T=c_{end}+\theta$.
- In this case, we need to introduce $(2 \theta +1)^2 (c_{span}+1)+1$ binary variables, where $c_{span} = c_{end}-c_{start} + 1$.



## Case 2:

We consider a case with more agents (correspondingly more complex specifications), where the system model is the same as case 1.





## Case 3:

We consider a case with nonlinear system model with 2 agents.

