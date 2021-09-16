#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import plotly.express as px 


# In[2]:


data = pd.read_csv('../data/life-expectancy.csv')
data.head() 


# In[3]:


data = data.sort_values(by='Life expectancy', ascending=False)
data.head()


# In[ ]:





# In[4]:


fig = px.line(data, x='Year', y='Life expectancy', color='Entity')
fig.show() 


# In[5]:


asia = data[data['Entity'] == 'Asia']


# In[6]:


asia


# In[7]:


import plotly.express as px
fig = px.choropleth(asia, locations="Entity",
                    color="Life expectancy", # lifeExp is a column of gapminder
                    hover_name="Entity",
                     animation_frame='Year', # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            width=800,
        #     height=400,
    )

for k in range(len(fig.frames)):
    fig.frames[k]['layout'].update(title_text=f'My title {k}')

fig.show()


# In[ ]:





# In[8]:


data.columns


# In[9]:


fig = px.bar(data, y='Life expectancy', x='Year', text='Life expectancy')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()


# In[10]:


data.Year.unique() 


# In[11]:


import plotly.express as px
fig = px.choropleth(data, locations="Code",
                    color="Life expectancy", # lifeExp is a column of gapminder
                    hover_name="Entity",
                     animation_frame='Year', # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            width=800,
        #     height=400,
    )

for k in range(len(fig.frames)):
    fig.frames[k]['layout'].update(title_text=f'My title {k}')

fig.show()


# In[12]:


import plotly.express as px

df = px.data.gapminder().query("year==2007")
fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()


# In[13]:


df.head() 


# In[ ]:




