#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv(r"C:\Users\HP\Documents\IMDB-Movie-Data.csv")
df


# In[5]:


df.shape


# In[7]:


df.info()


# In[13]:


df.describe()


# In[27]:


#df.describe(include='all')


# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[12]:


sns.heatmap(df.isnull())


# In[14]:


#To get missing value percentage
per_missing = df.isnull().sum()*100/len(df)
per_missing


# In[21]:


#drop the missing values
df2 = df.dropna()
df2


# In[22]:


df2.isnull().sum()


# In[24]:


#check for duplicated
duplicate_data = df2.duplicated().any()
duplicate_data


# In[25]:


#if duplicate data is found
#df = df2.drop_duplicates()
#df


# In[30]:


plt.figure(figsize=(15,8))
sns.heatmap(df2.corr(),annot=True)


# In[39]:


#displaying title of movies having runtime >= 180 minutes
movie_duration = df2[df2['Runtime (Minutes)'] >= 180]
movie_duration


# In[44]:


#In which year was the highest average voting
df2.groupby('Year')['Votes'].mean()


# In[45]:


df2.groupby('Year')['Votes'].mean().max()


# In[46]:


df2.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[50]:


sns.barplot(x='Year',y='Votes',data=df2)
plt.title('Average votes by year')
plt.show()


# In[52]:


#In which year was the highest average revenue
df2.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[55]:


sns.barplot(x='Year',y='Revenue (Millions)',data=df2)
plt.title('Highest Average Revenue by Year')
plt.show()


# In[56]:


df2.columns


# In[59]:


#to get the average rating for each director
df2.groupby('Director')['Rating'].mean().sort_values()


# In[62]:


df2.groupby('Director')['Rating'].mean().sort_values().head(10)


# In[63]:


#to get number of movies per year
df2['Year'].value_counts()


# In[65]:


sns.countplot(x='Year',data=df2)
plt.show()


# In[66]:


df2['Revenue (Millions)'].max()


# In[79]:


df2[df2['Revenue (Millions)'].max()==df2['Revenue (Millions)']]['Title']


# In[ ]:




