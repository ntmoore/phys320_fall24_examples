# for context, I'm running in Ubuntu Windows-Linux-Subsystem (WSL)
# this code should work on Linux, not sure about Mac/Windows
#
filename = "multiple_runs.csv" 
file_in = open(filename,'r')

# this isn't how you read a file.  
# print(file_in)
# instead:
for x in file_in: 
    print(x)
    print(x.split(","))
# this gives 
# nmoore@sj5947pw242:10-07_file_IO$ python3 read_in_csv_file-1.py
#v0(m/s),1.0000e+04,t2(s),2.0400e+04,dt(s),6.0000e+01,fell_to_earth,
#
#['v0(m/s)', '1.0000e+04', 't2(s)', '2.0400e+04', 'dt(s)', '6.0000e+01', 'fell_to_earth', '\n']
#v0(m/s),1.1000e+04,t2(s),4.3206e+05,dt(s),6.0000e+01,ran_out_of_time,
#
#['v0(m/s)', '1.1000e+04', 't2(s)', '4.3206e+05', 'dt(s)', '6.0000e+01', 'ran_out_of_time', '\n']

