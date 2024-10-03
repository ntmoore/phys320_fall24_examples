#!/usr/bin/env python
# coding: utf-8

# In[51]:


# working with radioactive decay CHAIN with following knowns
# Na -> Nb -> stable
# N(t) = N0 Exp[-t/tau]
# dN/dt = -(1/tau) N(t)
# tau = t_half / ln(2)

import math
import numpy as np
from scipy.integrate import solve_ivp

# for solve_ivp, this needs to be of the form:
# name(time, variables, args)
def dN_dt(t, state, tau_a, tau_b): 
    Na, Nb, Nstable = state

    dNa = -Na/tau_a
    dNb = Na/tau_a + -Nb/tau_b
    dNstable = Nb/tau_b

    return [dNa, dNb, dNstable]
    
ta_half = 10 # seconds
tau_a = ta_half/math.log(2.0)
tb_half = 15 # seconds
tau_b = tb_half/math.log(2.0)
N0a = 100 # number of intial atoms
N0b = 0 # number of intial atoms
N0stable = 0 # number of stable atoms at the end of the decay chain

tspan = [0,5*ta_half]
solution = solve_ivp(
    dN_dt, # derivative as function
    tspan,  # time interval to solve for
    [N0a, N0b, N0stable], # initial values
    args=(tau_a,tau_b,) # why does this have to have a comma?  needs to be a "tuple"????
    , method="RK45"
)

# this was helpful for syntax 
# https://simulationbased.com/2021/02/16/differential-equations-with-scipy-odeint-or-solve_ivp/comment-page-1/


# In[53]:


print(solution)


# In[55]:


print(solution.t)
print(solution.y[0])
print(solution.y[1])
print(solution.y[2])


# In[61]:


import matplotlib.pyplot as plt
plt.plot(solution.t,solution.y[0],label="Na solve_ivp t_half=%.1f"%ta_half, linestyle='--', marker='o', color='b')
plt.plot(solution.t,solution.y[1],label="Nb solve_ivp t_half=%.1f"%tb_half, linestyle='--', marker='o', color='r')
plt.plot(solution.t,solution.y[2],label="Nstable solve_ivp ", linestyle='--', marker='o', color='violet')
tvals=np.arange(0,3*ta_half)
plt.plot(tvals,N0a*np.exp(-tvals/tau_a), label="N0a*Exp(-t/tau)")
plt.grid()
plt.legend()
plt.title("solve_ivp using solve_ivp (RK45)")
plt.ylabel("number of atoms")
plt.xlabel("time (seconds), ta_1/2 = %.2f"%ta_half)


# In[ ]:




