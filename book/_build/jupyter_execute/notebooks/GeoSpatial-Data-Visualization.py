#!/usr/bin/env python
# coding: utf-8

# In[5]:


import geopandas as gpd  
import matplotlib.pyplot as plt 


# In[6]:


# read data 
data = gpd.read_file("zip://../data/ne_110m_admin_0_countries.zip")
data.head()


# In[7]:


data.plot() 


# In[8]:


data['area'] = data['geometry'].area
data.head() 


# In[9]:


data[data['name'] != 'India'].plot() 


# In[11]:


# https://epsg.io/4326
data.geometry.crs


# In[12]:


data.to_crs(epsg=3857, inplace=True)


# In[13]:


data.head() 


# In[16]:


data.plot(figsize=(12,8))


# In[ ]:




