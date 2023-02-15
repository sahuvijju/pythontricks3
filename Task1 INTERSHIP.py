#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\HP\\Desktop\\vk.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[10]:


sns.countplot(x="Species",data=df)


# In[11]:


sns.boxplot(df["SepalLengthCm"])


# In[12]:


sns.scatterplot(x="Species",y="PetalWidthCm",hue="Id",data=df)


# In[ ]:




