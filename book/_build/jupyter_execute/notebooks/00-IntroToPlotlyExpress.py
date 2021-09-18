#!/usr/bin/env python
# coding: utf-8

# # Intro to Plotly Express

# In[27]:


# import libraries 
import pandas as pd # data processing, 
import plotly.express as px # for visualization 
from plotly.figure_factory import create_table # for creating nice table 


# ## Reading and Exploring Data 

# In[2]:


# load built-in gapminder dataset from plotly 
gapminder = px.data.gapminder() 


# In[3]:


# examine first few rows 
gapminder.head() 


# In[4]:


# examine last few rows 
gapminder.tail() 


# In[5]:


# examine specific number of rows 
gapminder.head(10)


# In[6]:


# check the shape of the dataset
gapminder.shape 


# In[7]:


# column names 
gapminder.columns


# In[8]:


# data type of each column 
gapminder.dtypes


# ```{note}
# - object: categorical variable 
# - float / int: numeric variable
# ```

# In[9]:


# get information about dataset 
gapminder.info() 


# In[10]:


# summary statistics
gapminder.describe() 


# ## Creating a Publication Quality Table 

# In[4]:


# create a publication quality table 
table = create_table(gapminder.head(10))
py.iplot(table)


# ## Quick Visualizations with Bar Charts

# In[11]:


fig = px.bar(data_frame=gapminder, x='year', y='pop')
fig.show() 


# In[12]:


# height 
fig = px.bar(data_frame=gapminder, x='year', y='pop', height=400)
fig.show() 


# In[14]:


# let's add color by lifeExp and other parameters 
fig = px.bar(data_frame = gapminder, x='year', y='pop', color='lifeExp', 
             labels={'pop': 'Population of Canada'}, height=400)
fig.show() 


# ## Plot Life Expectency vs GDP Per Capita

# In[15]:


# filter 2007 data only from dataset 
gapminder2007 = gapminder.query('year == 2007')
# create scatter plot 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp')
fig.show() 


# In[16]:


# color by continent 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent')
fig.show() 


# ##  Create Interactive Bubble Charts

# In[17]:


# create a bubble chart 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60)
fig.show() 


# In[18]:


# hover name 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, 
                 hover_name='country')
fig.show() 


# ##  Create Interactive Animations and Facet Plots

# In[19]:


# create a facet plot 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, 
                hover_name='country', facet_col='continent')
fig.show() 


# In[20]:


# log scale on x-axis 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, 
                hover_name='country', facet_col='continent', log_x=True)
fig.show()


# In[21]:


# let's add animation 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=40, 
                hover_name='country', log_x=True, animation_frame='year',
                 animation_group='country', range_x=[25, 10000], range_y=[25,90])
fig.show()


# In[22]:


# customize the labels 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=40, 
                hover_name='country',log_x=True, animation_frame='year',
                 animation_group='country', range_x=[25, 10000], range_y=[25,90], 
                labels=dict(pop="Population", gdpPercap="GDP Per Capita", lifeExp="Life Expectency"))
fig.show()


# ##  Represent Geographic Data as Animated Maps

# In[23]:


# create a map using line_geo()
fig = px.line_geo(gapminder.query('year == 2007'), locations='iso_alpha', color='continent', projection='orthographic')
fig.show() 


# In[24]:


# create a map using choropleth
fig = px.choropleth(gapminder, locations='iso_alpha', color='lifeExp', hover_name='country', 
                    animation_frame='year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
fig.show() 


# ## Using Plotly Template in Any Graphs

# In[25]:


# print available themes or template 
import plotly.io as pio
pio.templates


# In[ ]:





# In[28]:


# let's use plotly_dark in our previous bar chart 
fig = px.bar(gapminder, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'},
             height=400, template='plotly_dark')
fig.show()


# In[30]:


# seaborn
fig = px.bar(gapminder, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'},
             height=400, template='seaborn')
fig.show()


# In[32]:


# ggplot2 
fig = px.bar(gapminder, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'},
             height=400, template='ggplot2')
fig.show()

