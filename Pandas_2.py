#!/usr/bin/env python
# coding: utf-8

# <H1>Pandas Modülü Bölüm 2 - Detay Bilgiler</H1>

# In[1]:


import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

df.head(5)


# In[2]:



# Dataframeimizin bir kopyasını copy() kullanarak oluşturabiliriz:

df_kopya = df.copy()
df_kopya.head()


# ### Column Drop

# In[3]:



# Dataframeimizin bazı sütunları işimize yaramayabilir,
# bu sütunlardan nasıl kurtulabiliriz?

df_yeni = df.drop(['Overview', 'Meta_score'], axis = 1)  # axis=1 ise column drop, 0 ise row drop eder. Default=0
df_yeni.head()


# In[4]:


# Yukardaki aynı işlemi şu şekilde de yapabilirsiniz:
df_yeni2 = df.drop(columns = ['Overview', 'Meta_score'])
df_yeni2.head()


# ### Row Drop
# 

# In[5]:


df_yeni3 = df.drop([1])
df_yeni3.head()


# In[ ]:





# ### Filtreleme

# In[6]:


df_filtered = df[df['IMDB_Rating'] >= 8]

df_filtered


# In[ ]:





# In[7]:


# veya...

df_filtered = df.query('IMDB_Rating >= 9')
df_filtered


# In[8]:


df.head()


# In[9]:


df.dtypes


# In[10]:



f = lambda x: (x["Runtime"].split())[0] 
df["RuntimeYeni"] = df.apply(f, axis=1)


# In[11]:


df.head()


# In[12]:


df.dtypes


# In[13]:



df['RuntimeYeni2'] = df['RuntimeYeni'].astype('int') 

df_filtered = df.query('RuntimeYeni2 >= 140')
df_filtered


# In[14]:


df.dtypes


# In[15]:


df = df.drop(['RuntimeYeni'], axis = 1)


# In[16]:


df.head()


# In[ ]:




