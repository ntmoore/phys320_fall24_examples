# how do you run a (python) program from within a python program?  
#   https://docs.python.org/3/library/os.html
# for context, I'm running in Ubuntu Windows-Linux-Subsystem (WSL)
# this code should work on Linux, not sure about Mac/Windows
#
import os

os.system("ansiweather -l Winona -d true")
for i in range(5):
    shell_command = "ansiweather -l Winona -f %d"%(i+1) 
    os.system(shell_command)
    if(i==4):
        print("running: ",shell_command)

#gives: 
# nmoore@sj5947pw242:10-07_file_IO$ python3 run_external_command-2.py
#   Weather in Winona: 18 °C - UVI: 3.95 - Wind: 2.94 m/s NE - Humidity: 50% - Pressure: 1018 hPa - Sunrise: Oct 03 07:07:31 AM - Sunset: Oct 03 06:44:06 PM
#   Winona forecast: Thu Oct 03: 21/8 °C
#   Winona forecast: Thu Oct 03: 21/8 °C - Fri Oct 04: 20/6 °C
#   Winona forecast: Thu Oct 03: 21/8 °C - Fri Oct 04: 20/6 °C - Sat Oct 05: 32/11 °C
#   Winona forecast: Thu Oct 03: 21/8 °C - Fri Oct 04: 20/6 °C - Sat Oct 05: 32/11 °C - Sun Oct 06: 19/9 °C
#   Winona forecast: Thu Oct 03: 21/8 °C - Fri Oct 04: 20/6 °C - Sat Oct 05: 32/11 °C - Sun Oct 06: 19/9 °C - Mon Oct 07: 21/6 °C
#   running:  ansiweather -l Winona -f 5
