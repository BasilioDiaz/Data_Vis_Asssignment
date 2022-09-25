#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import scipy as sp
import plotly.figure_factory as ff
import chart_studio.plotly as py
from datetime import datetime
from plotly.offline import iplot
import streamlit as st


# In[68]:


df  = pd.read_excel("Cierre 12-12-19.xlsx", header = [3] )
df.drop('UTILIDAD', inplace=True, axis=1)
df['IS_EMERGING_MARKET'] = df['IS_EMERGING_MARKET'].replace({'Y': 'Emerging Market', 'N': 'Developed Market'})


# In[69]:


header = st.container()
dataset = st.container()
visualizations = st.container()
focus = st.container()
modelTraining = st.container()


# In[70]:


with header:
    st.title("Amazing Bond Portfolio Managment APP")
    st.text("With this app you can manage yours bond portafolio in a simple and easy way. Take faster and better decisions today!")


# In[71]:


with dataset:
    st.header("Take a look of the dataset")
    st.text("This dataset was directly download from Bloomberg. It update automaticly daily. Amazing, right?")
    st.write(df.head())


# In[72]:


with visualizations:
    st.header("Now some visualizations")
    st.text("This visualizations will help you take better decisions")
    fig = px.pie ( df , values = 'MONTO' , names = 'INDUSTRY_SECTOR' , color = "INDUSTRY_SECTOR", title='Percentage of investment by Industry')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
    fig_2 = px.bar(df, x='RTG_FITCH', y='MONTO', title = "USD Investment per Rating and Country of Risk", color = "CNTRY_OF_RISK")
    st.plotly_chart(fig_2, use_container_width=True)
    fig_4 = px.pie(df, names ="IS_EMERGING_MARKET", values="MONTO", title ="Percentage of developed Market")
    fig_4.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_4, use_container_width=True)
    fig_5 = px.bar(df, x='RTG_FITCH', y='MONTO', title = "USD Investment per Rating and Type of Market", color = "IS_EMERGING_MARKET")
    st.plotly_chart(fig_5, use_container_width=True)
    
    
    


# In[73]:


with focus:
    st.header("Lets zoom in into the ratings")
    st.text("A worst rating should pay more! Lets check if this happens!")
    data_1=df.groupby('RTG_FITCH').agg({'CPN':'mean', 'MONTO':'sum'})
    data_1=data_1.reset_index()
    data_1
    fig_3 = px.line(data_1, x="RTG_FITCH", y="CPN", title ="CPN Avg per Rating")
    st.plotly_chart(fig_3, use_container_width=True)
    


# In[74]:


#guardar  Fig 1
#fig = px.pie ( df , values = 'MONTO' , names = 'INDUSTRY_SECTOR' , color = "INDUSTRY_SECTOR", title='Percentage of investment by Industry')
#fig.update_traces(textposition='inside', textinfo='percent+label')
#fig.show()


# In[75]:


#Guardar Fig 2
#fig_2 = px.bar(df, x='RTG_FITCH', y='MONTO', title = "USD Investment per Rating and Country of Risk", color = "CNTRY_OF_RISK")
#fig_2.show()


# In[76]:


#data_1=df.groupby('RTG_FITCH').agg({'CPN':'mean', 'MONTO':'sum'})
#data_1=data_1.reset_index()
#data_1


# In[77]:


#fig_3 = px.line(data_1, x="RTG_FITCH", y="CPN", title ="CPN Avg per Rating")

#fig_3.show()


# In[78]:


#df['IS_EMERGING_MARKET'] = df['IS_EMERGING_MARKET'].replace({'Y': 'Emerging Market', 'N': 'Developed Market'})


# In[79]:


#fig_4 = px.pie(df, names ="IS_EMERGING_MARKET", values="MONTO", title ="Percentage of developed Market")
#fig_4.update_traces(textposition='inside', textinfo='percent+label')
#fig_4.show()


# In[80]:


#fig_5 = px.bar(df, x='RTG_FITCH', y='MONTO', title = "USD Investment per Rating and Type of Market", color = "IS_EMERGING_MARKET")
#fig_5.show()


# In[ ]:





# In[ ]:




