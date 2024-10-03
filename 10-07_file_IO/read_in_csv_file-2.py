# for context, I'm running in Ubuntu Windows-Linux-Subsystem (WSL)
# this code should work on Linux, not sure about Mac/Windows
#
filename = "multiple_runs.csv" 
file_in = open(filename,'r')

time=[]
initial_speed=[]
for x in file_in: 
    # the good data starts with "v0..."
    # reminder for slices, x[0:7], include 0 and the knife comes down before element 7
    if(x[0:7] == "v0(m/s)") :
        elements = x.split(",")
        #print(elements)
        # casting as float to avoid possible trouble
        time.append(float(elements[3]))
        initial_speed.append(float(elements[1]))

print(time,initial_speed)
import numpy as np
t=np.array(time)
v0=np.array(initial_speed)

# most "good" data looks like:
#   v0(m/s),1.0000e+04,t2(s),2.0400e+04,dt(s),6.0000e+01,fell_to_earth,
# but the last (non-data) line looks like: 
#   running:  python3 ranger-verlet-w-args.py t_limit_days 5 v0 1.5000e+04 quiet_output

import matplotlib.pyplot as plt
plt.plot(v0/1e3,t/3600.0)
plt.ylabel("time to Luna, (hours)")
plt.xlabel("initial speed, (km/s)")
plt.grid()
plt.tight_layout()
plt.savefig("time_to_Luna.png")
plt.close()
