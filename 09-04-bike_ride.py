#!/usr/bin/env python
# coding: utf-8

# In[63]:


# if you want to convert this into a python script that you can run from the shell,
# open the Anaconda Prompt and run this command: 
#      jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb
#
from math import *


# In[65]:


N=10
dt=5.0
a=1.0
v0=10
x0=20
dx=175


# In[67]:


print("regular time sampling")
print("time (s)       v (m/s)       x (m)")
v_sum=0;

# add these lines to collect data for plotting
# _ts refers to data that is regularly time-sampeled
t_ts=[]
x_ts=[]
v_ts=[]

# note, has to be N+1 instead of N
for i in range(1,N+1):
    #print(i)
    t=dt*i
    v=v0+a*t
    x = x0 + v0*t + 0.5*a*t**2
    print(t,v,x)
    v_sum = v_sum + v
    
    # add these lines to collect data to plot
    t_ts.append(t)
    v_ts.append(v)
    x_ts.append(x)

print("V_AVG = ",v_sum/N)


# In[69]:


print("regular distance sampling")
print("time (s)       v (m/s)       x (m)")
v_sum=0.0
one_over_v_sum = 0.0

# add these lines to collect data for plotting
# _xs refers to data that is regularly distance-sampeled
t_xs=[]
x_xs=[]
v_xs=[]

# Note that N+1 shows up again
for i in range(1,N+1):
    x = x0 + dx*float(i)
    t = (-v0+sqrt(v0**2-4.0*(a/2.0)*(x0-x)))/(2.0*(a/2.0))
    v = v0 + a*t
    print(t,v,x)
    v_sum = v_sum + v
    one_over_v_sum = one_over_v_sum + 1.0/v

    # add these lines to collect data to plot
    t_xs.append(t)
    v_xs.append(v)
    x_xs.append(x)

print("V_AVG = ",v_sum/N)
print("one_over_V_AVG = ",one_over_v_sum/N)
print("V_AVG = ",1.0/(one_over_v_sum/N))


# In[71]:


print("<v> over time integral gives ",v0+(a/2.0)*(N*dt))


# In[77]:


import matplotlib.pyplot as plt
plt.plot(t_ts,v_ts,"o",label="regular time sampling")
plt.plot(t_xs,v_xs,"x",label="regular distance sampling")
plt.legend()
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")


# In[ ]:




