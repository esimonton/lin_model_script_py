#!/usr/bin/env python
# coding: utf-8

# In[4]:

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
from scipy import stats


# In[5]:

print (sys.argv[1])
regrex1 = pd.read_csv(sys.argv[1])
print (regrex1)


# In[10]:


x = regrex1.x
y = regrex1.y


# In[11]:


plt.plot(x, y, 'o')
plt.savefig("scatter.png")

# In[16]:


reg = stats.linregress(x, y)
print(reg)


# In[18]:


# plt.plot(x, reg.intercept + reg.slope*x, 'r', label='lin fit')
# plt.savefig("line.png")


# In[21]:


plt.plot(x, y, 'o', label='scatter') 
plt.plot(x, reg.intercept + reg.slope*x, 'r', label='lin fit') 
plt.legend() 
plt.savefig("fit.png")

# In[ ]:




