# Asynchronous Temporal Robustness (ATR)

The aim of this project is to explore how complex situations can be handled by our encoding methods. Given ATR bound $\theta$, number of agents $num$, time span of specifications $c_{span}$, our encoding method will introduce at most $(2\theta +1)^{num} (c_{span}+1)+1$ binary variables.

## Case 1: 

- Two agents
- System model: $x_{k+1} = x_k +u_k, x\in [-10,10], u \in [-2,2]$, with initial state $x^{\{1\}}_0=x^{\{2\}}_0=0$. (one-dimensional motion planning and the control input is its speed.)
- Specification: the distance between two agents should be larger than 1m
```math
c(x(t), t) = \left\{ \begin{array}{ll} 1  &\text{for all} \ t < c_{start} \  \text{and all} \ t > c_{end} \\ x^{\{2\}} - x^{\{1\}}-1 & \text{for all} \ t \in [c_{start}, c_{end}] \end{array} \right.
```
- Required temporal robustness: $\theta$

- objective: minimize its energy.

- When $c_{span} = 10$ and $\theta=5$, here is the final results:  

![image](http://xinyi-yu.test.upcdn.net/case1.png!/scale/50)

- Some comparison results of computation time:

| Computation time (number of binary variables) | $c_{span} = 10$ | $c_{span} = 100$ |    $c_{span} = 1000$     |    $c_{span} = 10000$     |
| :-------------------------------------------: | :-------------: | :--------------: | :----------------------: | :-----------------------: |
|                 $\theta = 5$                  |  0.12s (1332)   |  1.05s (12222)   |      11.2s (121122)      |      117s (1210122)       |
|                 $\theta = 10$                 |  0.66s (4852)   |   4.4s (44542)   |       46s (441442)       |  out of memory (4410442)  |
|                 $\theta = 50$                 | 12.2s (112212)  | 91.5s (1030302)  | out of memory (10211202) | out of memory (102020202) |

### Remark: 

- For simplicity, we directly set $c_{start} = 1+\theta$, control horizon $T=c_{end}+\theta$. (I didn't realize that I should fix $T$ to compare different cases until I finished all the cases. Anyways, it isn't a very important factor.)
- In this case, we need to introduce $(2 \theta +1)^2 (c_{span}+1)+1$ binary variables, where $c_{span} = c_{end}-c_{start} + 1$. 
- Out of memory: It implies that it needs to introduce too many variables which has already been out of memory allocated to this program (less than 2GB)



## Case 2:

We consider the case with more agents (correspondingly more complex specifications), where the system model and the other problem setting are the same as case 1. Specifically, we did the cases with 2, 3, 4 agents respectively.

- when $num=2$, the specification is that the distance between two agents should be larger than 1m,

```math
 c(x(t), t) = \left\{ \begin{array}{ll} 1  &\text{for all} \ t < c_{start} \  \text{and all} \ t > c_{end} \\ x^{\{2\}} - x^{\{1\}}-1 & \text{for all} \ t \in [c_{start}, c_{end}] \end{array} \right.
```

- when $num=3$, the specification is that three agent should be placed in turn with an interval of more than 1m,

```math
 c(x(t), t) = \left\{ \begin{array}{ll} 1  &\text{for all} \ t < c_{start} \  \text{and all} \ t > c_{end} \\ min(x^{\{2\}} - x^{\{1\}}-1, x^{\{3\}} - x^{\{2\}}-1) & \text{for all} \ t \in [c_{start}, c_{end}] \end{array} \right.
```

- when $num=4$, the specification is that four agent should be placed in turn with an interval of more than 1m,

```math
c(x(t), t) = \left\{ \begin{array}{ll} 1  &\text{for all} \ t < c_{start} \  \text{and all} \ t > c_{end} \\ min(x^{\{2\}} - x^{\{1\}}-1, x^{\{3\}} - x^{\{2\}}-1, x^{\{4\}} - x^{\{3\}}-1) & \text{for all} \ t \in [c_{start}, c_{end}] \end{array} \right.
```

- When $num = 4, c_{span} = 10$ and $\theta=5$, here is the final results:  

![image](http://xinyi-yu.test.upcdn.net/case3.png!/scale/50)

- Some comparison results of computation time:

| Computation time (number of binary variables) | $\theta = 5, c_{span} = 10$ | $\theta = 5, c_{span} = 100$ | $\theta = 10, c_{span} = 100$ |
| :-------------------------------------------: | :-------------------------: | :--------------------------: | :---------------------------: |
|                    $num=2$                    |        0.12s (1332)         |        1.05s (12222)         |         4.4s (44542)          |
|                    $num=3$                    |        2.81s (41262)        |       27.97s (400632)        |        199s (2787562)         |
|                    $num=4$                    |        42s (600282)         |   out of memory (5871042)    |   out of memory (77986882)    |



## Case 3:

We consider a case with nonlinear system model with 2 agents.

