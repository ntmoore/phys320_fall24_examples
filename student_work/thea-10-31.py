import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sys

#Constants
m = 55 #kg
L = 4 #m
g = 9.8 #m/s^2

def dstate_dt(t, state, m, g, L):
    theta, omega = state
    dtheta_dt = omega
    domega_dt = (-m*g*L*math.sin(theta))/(m*L**2)
    return [dtheta_dt, domega_dt]

nat_f = math.sqrt(g/L)/(2.0*math.pi)
nat_p = 1.0/nat_f
tspan = [0,10*nat_p]
#theta_0 = 90.0*(math.pi/180.0)
omega_0 = 0.0
verbose_output = 1


def find_period(t, state, m, g, L):
    theta, omega = state
    return omega

for i in range(len(sys.argv)):
    if(sys.argv[i] == "theta"):
        theta_i = float(sys.argv[i+1])*(math.pi/180.0)
        theta_f = float(sys.argv[i+2])*(math.pi/180.0)
        theta_0 = theta_i
    if(sys.argv[i] == "quiet_output") :
        verbose_output = 0

thet=[]
per=[]
# iterate, 200 steps from 1 to 179 degrees
for theta_0 in np.linspace(1,90+88,90): 
#while (theta_0<(90*(math.pi/180.0))):
    #deg0 = theta_0*(180.0/math.pi)
    #deg1 = deg0 + 1
    #theta_1 = deg1*(math.pi/180.0)
    #theta_0 = theta_1

    solution = solve_ivp(
        dstate_dt,
        tspan,
        #[theta_0, omega_0],
        [theta_0*(math.pi/180.0), omega_0],
        args=(m,g,L),
        method="RK45",
        dense_output=True,
        events=(find_period)
    )
    
    print(solution.t_events)
    print("theta_0=",theta_0," (deg)\tperiod = ",solution.t_events[0][2],"(s)")
    #print(solution.t_events[0])
    #print(solution.t_events[0][2])
    #thet.append(theta_0)
    #per.append(solution.t_events[0][2])

#thetaa = np.array(thet)
#periodd = np.array(per)

#print(thetaa*(180.0/math.pi))
#print(periodd)

#import csv
#
#data = [
#    ["degree","period"],
#    [(thetaa)*(180.0/math.pi),periodd]
#]
#
#with open("output.csv", "a", newline="") as file:
#    writer = csv.writer(file)
#    writer.writerows(data)
