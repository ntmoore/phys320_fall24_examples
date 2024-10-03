# how do you run a (python) program from within a python program?  
#   https://docs.python.org/3/library/os.html
# for context, I'm running in Ubuntu Windows-Linux-Subsystem (WSL)
#
import os
os.system("pwd")
os.system("date")
os.system("ansiweather")

#gives: 
#   nmoore@sj5947pw242:10-07_file_IO$ python3 run_external_command-1.py
#   /mnt/c/Users/sj5947pw/OneDrive - Minnesota State/Class Materials - Phys320 Fa24/10-07_file_IO
#   Thu Oct  3 11:56:26 CDT 2024
#   Weather in Rzeszów: 13 °C - UVI: 2.52 - Wind: 1.54 m/s SW - Humidity: 84% - Pressure: 1012 hPa
