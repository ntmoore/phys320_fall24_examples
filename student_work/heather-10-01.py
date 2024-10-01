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
#F_earth=(-G*m_earth*m_ranger)/(r**2)
#F_moon=(G*m_moon*m_ranger)/((r_moon_earth-r)**2)
#F_net=F_earth+F_moon
# I think these are only needed for Verlet
#a=F/m_ranger
#v2 = v2 + a*dt
#r= r + v2*dt
#U_earth=-(G*m_earth*m_ranger)/(R_1)
#U_moon=(-G*m_moon*m_ranger)/(R_2)
#U_net=U_earth+U_moon


import math
import numpy as np
from scipy.integrate import solve_ivp

def dstate_dt(t, state, m_earth, m_moon, m_ranger, G, R_earth_moon): 
    r, v = state

    dr_dt = v
    dv_dt = ((-G*m_earth)/r**2) + (G*m_moon)/((R_earth_moon-r)**2)
    # note that the ranger/rocket's mass has divided out
        
    return [dr_dt, dv_dt]
 
    
tspan = [0,24*3600]
r0 = R_1
v0 = 13.0e3

solution = solve_ivp(
    dstate_dt, # derivative as function
    tspan,  # time interval to solve for
    [R_1, v0], # initial values
    args=(m_earth,m_moon,m_ranger,G,r_moon_earth,)
    #, method="RK45"
)

print(solution)
print("time = ",solution.t)
print("radius from earth = ",solution.y[0])
print("velocity = ",solution.y[1])

#  message: The solver successfully reached the end of the integration interval.
#  success: True
#   status: 0
#        t: [ 0.000e+00  3.661e-01 ...  7.285e+04  8.640e+04]
#        y: [[ 6.438e+06  6.443e+06 ...  5.454e+08  6.514e+08]
#            [ 1.300e+04  1.300e+04 ...  7.834e+03  7.820e+03]]
#      sol: None
# t_events: None
# y_events: None
#     nfev: 98
#     njev: 0
#      nlu: 0
#time =  [0.00000000e+00 3.66090267e-01 4.02699294e+00 4.06360197e+01
# 4.06726287e+02 1.11260559e+03 2.50757208e+03 5.31154453e+03
# 1.10962134e+04 2.34435629e+04 3.72235187e+04 4.93641107e+04
# 6.15047028e+04 7.28539648e+04 8.64000000e+04]
#radius from earth =  [6.43800000e+06 6.44275853e+06 6.49027330e+06 6.95872964e+06
# 1.11931282e+07 1.82481891e+07 3.05870550e+07 5.31087169e+07
# 9.64056128e+07 1.84541142e+08 2.80603687e+08 3.64477899e+08
# 4.56422598e+08 5.45410956e+08 6.51435161e+08]
#velocity =  [13000.         12996.47960975 12961.55935784 12638.3431066
# 10787.01535095  9423.61061539  8436.12485356  7752.91927086
#  7305.06322311  7030.29040263  6927.51508605  6911.11021212
#  7847.48656669  7834.1060684   7820.4443073 ]
