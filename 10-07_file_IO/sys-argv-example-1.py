# read some command line inputs and echo them back
# Using basic sys.argv tool
# https://swcarpentry.github.io/python-novice-inflammation/12-cmdline.html
import sys
print(sys.argv)
print("sys.argv[0] = ",sys.argv[0])
print("number of arguments supplied is ",len(sys.argv))

### example usage
# $ python3 sys-argv-example-1.py 3 4 5
# ['sys-argv-example-1.py', '3', '4', '5']
# sys.argv[0] =  sys-argv-example-1.py
# number of arguments supplied is  4
