# how do you run a (python) program from within a python program?  
#   https://docs.python.org/3/library/os.html
# for context, I'm running in Ubuntu Windows-Linux-Subsystem (WSL)
# this code should work on Linux, not sure about Mac/Windows
#
import os

for v0 in range(8,16,1):
    v0_mps = v0*1.0e3
#for v0 in range(10000,15000,100):
#    v0_mps = v0
    shell_command = "python3 ranger-verlet-w-args.py t_limit_days 5 v0 %.4e quiet_output "%(v0_mps) 
    os.system(shell_command)

print("running: ",shell_command)

#gives: 
# nmoore@sj5947pw242:10-07_file_IO$ python3 run_external_command-4.py
# v0(m/s),1.1000e+04,t2(s),4.3206e+05,dt(s),6.0000e+01,ran_out_of_time,
# v0(m/s),1.2000e+04,t2(s),7.3200e+04,dt(s),6.0000e+01,arrived_at_Luna,
# v0(m/s),1.3000e+04,t2(s),5.2140e+04,dt(s),6.0000e+01,arrived_at_Luna,
# v0(m/s),1.4000e+04,t2(s),4.2240e+04,dt(s),6.0000e+01,arrived_at_Luna,
# v0(m/s),1.5000e+04,t2(s),3.6120e+04,dt(s),6.0000e+01,arrived_at_Luna,
# running:  python3 ranger-verlet-w-args.py t_limit_days 5 v0 1.5000e+04 quiet_output
#
# send this to a datafile with the ">" operator
# 
