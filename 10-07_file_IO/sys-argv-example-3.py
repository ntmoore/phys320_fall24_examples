# read some command line inputs and echo them back
# Using basic sys.argv tool
# https://swcarpentry.github.io/python-novice-inflammation/12-cmdline.html
import sys
print(sys.argv)

# default values
v0=12.0e3
t_limit = 2*24*3600
print("default values:")
print("v0 = ",v0)
print("t_limit = ",t_limit)

for i in range(len(sys.argv)): 
    # look for keywords and set simulation variables if 
    # they are supplied.
    if(sys.argv[i] == "v0") :
        v0 = float(sys.argv[i+1])
    if(sys.argv[i] == "t_limit_seconds") :
        t_limit = float(sys.argv[i+1])
    if(sys.argv[i] == "t_limit_hours") :
        t_limit = float(sys.argv[i+1])*3600
    if(sys.argv[i] == "t_limit_days") :
        t_limit = float(sys.argv[i+1])*24*3600

print("via command-line-arguments defaults changed to:")
print("v0 = ",v0)
print("t_limit = ",t_limit)
