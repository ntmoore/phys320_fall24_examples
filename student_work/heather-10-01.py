# Franger Problem Resolved

G=6.67e-11 
m_earth=5.98e24 # kg (Earth's mass)
m_ranger= 10000 # kg (mass of rcocket)
m_moon=7.35e22 # kg (moon's mass)
r_earth=6.388e6 # m (radius of Earth)
r_moon_earth=3.844e8 # m (distance from Earth to moon)
r_moon=1740e3 #m
R_1=r_earth+50e3
R_2=r_moon_earth-r_moon


#Equations
F_earth=(-G*m_earth*m_ranger)/(r**2)
F_moon=(G*m_moon*m_ranger)/((r_moon_earth-r)**2)
F_net=F_earth+F_moon
a=F/m_ranger
v2 = v2 + a*dt
r= r + v2*dt
U_earth=-(G*m_earth*m_ranger)/(R_1)
U_moon=(-G*m_moon*m_ranger)/(R_2)
U_net=U_earth+U_moon


import math
import numpy as np
from scipy.integrate import solve_ivp

def dstate_dt(t, state, m_rocket, m-earth, m_ranger, G, R_1, R_2, v2): 
    x, v = state

    dr_dt = v
    dv_dt = ((-G*m_earth)/R_1**2)+(G*m_moon)/R_2**2)
    
    return [dx_dt, dv_dt]
 
    
tspan = [0,14*24*3600]
r0 = R_1
v0 = 0.0

solution = solve_ivp(
    dstate_dt, # derivative as function
    tspan,  # time interval to solve for
    [, 0], # initial values
    args=(m_earth,m_moon,G,R_1,R_2) # why does this have to have a comma?  needs to be a "tuple"????
    , method="RK45"
)



