# read some command line inputs and echo them back
# Using basic sys.argv tool
# https://swcarpentry.github.io/python-novice-inflammation/12-cmdline.html
import sys
print(sys.argv)

for i in range(len(sys.argv)): 
    print("i=",i," sys.argv[i] = ",sys.argv[i])

# typical output
# > python3 sys-argv-example-2.py N 2
# ['sys-argv-example-2.py', 'N', '2']
# i= 0  sys.argv[i] =  sys-argv-example-2.py
# i= 1  sys.argv[i] =  N
# i= 2  sys.argv[i] =  2
