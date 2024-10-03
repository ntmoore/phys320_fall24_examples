# how do you run a (python) program from within a python program?  
#   https://docs.python.org/3/library/os.html
# for context, I'm running in Ubuntu Windows-Linux-Subsystem (WSL)
# this code should work on Linux, not sure about Mac/Windows
#
import os

for i in range(5):
    shell_command = "python3 ntm_sqrt.py %.4e"%(i) 
    os.system(shell_command)
    if(i==4):
        print("running: ",shell_command)

#gives: 
#   nmoore@sj5947pw242:10-07_file_IO$ python3 run_external_command-3.py
#   sqrt(0.0000e+00) = 0.0000e+00
#   sqrt(1.0000e+00) = 1.0000e+00
#   sqrt(2.0000e+00) = 1.4142e+00
#   sqrt(3.0000e+00) = 1.7321e+00
#   sqrt(4.0000e+00) = 2.0000e+00
#   running:  python3 ntm_sqrt.py 4.0000e+00
