# what is the square-root of a number?
import math
import sys

in_x = float(sys.argv[1])
out_x = math.sqrt(in_x)
print("sqrt(%.4e) = %.4e"%(in_x,out_x))

# usage
#   nmoore@sj5947pw242:10-07_file_IO$ python3 ntm_sqrt.py 9
#   sqrt(9.0000e+00) = 3.0000e+00
