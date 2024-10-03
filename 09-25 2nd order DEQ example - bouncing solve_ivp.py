#!/usr/bin/env python
# coding: utf-8


# working with mg spring system  with following knowns
# down is + 
# F_net = +mg - k (x-x0)
m = 2 # kg
k = 100 # N/m
g = 9.8 # N/kg
L = 0.50 # meters relaxed spring length from mount point
x_eq = m*g / k # equilibrium stretch from mount point/relaxed length
omega = (k/m)**0.5 # natural oscillation frequency

import math
import numpy as np
from scipy.integrate import solve_ivp

# for solve_ivp, this needs to be of the form:
# name(time, variables, args)
def dstate_dt(t, state, k, m, g, L): 
    x, v = state

    dx_dt = v
    dv_dt = (m*g - k*(x-L))/m # reminder, a = F/m
    
    return [dx_dt, dv_dt]
    
period = 2.0*math.pi/omega
tspan = [0,2*period]
x0 = L + 1.1*x_eq 
v0 = 0.0

solution = solve_ivp(
    dstate_dt, # derivative as function
    tspan,  # time interval to solve for
    [1.1*x_eq, 0], # initial values
    args=(k,m,g,L,) # why does this have to have a comma?  needs to be a "tuple"????
    , method="RK45"
)

# this was helpful for syntax 
# https://simulationbased.com/2021/02/16/differential-equations-with-scipy-odeint-or-solve_ivp/comment-page-1/

print(solution)

print(solution.t)
print(solution.y[0])
print(solution.y[1])

import matplotlib.pyplot as plt
plt.plot(solution.t,solution.y[0],label="x solve_ivp", linestyle='--', marker='o', color='b')
tvals=np.arange(0,period,period/30)
plt.plot(tvals,L+(x0-L)*np.cos(omega*tvals), label="L+A*sin(omega t)")
plt.grid()
plt.legend()
plt.title("using solve_ivp (RK45)")
plt.ylabel("position")
plt.xlabel("time (seconds)")
