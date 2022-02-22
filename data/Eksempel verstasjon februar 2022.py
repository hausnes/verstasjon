#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/hausnes/verstasjon/main/data/hausnes-verstasjon-inne-varmepumpe.csv')
df.head()


# In[2]:


df.tail()


# In[3]:


df.dtypes


# In[4]:


df['created_at'] = pd.to_datetime(df['created_at'])


# In[6]:


df.dtypes


# In[7]:


df['temperatur']


# In[8]:


df['created_at']


# In[9]:


df[df.temperatur > 30]


# In[10]:


df[df['created_at'].dt.strftime('%Y-%m-%d') == '2022-02-21'] 
# https://strftime.org/


# In[13]:


df[df['created_at'].dt.strftime('%Y-%m-%d') == '2022-02-21']


# In[20]:


import matplotlib.pyplot as plt
df[df['created_at'].dt.strftime('%Y-%m-%d') == '2022-02-21'].pm1.plot(label="pm1")
#df[df['created_at'].dt.strftime('%Y-%m-%d') == '2022-02-21'].pm25.plot(label="pm2.5")
#df[df['created_at'].dt.strftime('%Y-%m-%d') == '2022-02-21'].pm10.plot(label="pm10")
plt.legend()
plt.show()


# In[22]:


df[df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S') == '2022-02-21 15:00:12']


# In[27]:


df[df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S') > '2022-02-21 15:00:00']


# In[ ]:


df[df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S') > '2022-02-21 15:00:00']
and df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S') < '2022-02-21 16:00:00'

