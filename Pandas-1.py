#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df =pd.read_csv("imdb_top_1000.csv")


# In[8]:


df.head(5) #İlk beş satırı görüntüler


# In[9]:


df.tail(5) #son 5 satırı görüntüler


# In[12]:


df.shape # dataframein boyutlarını gösterir


# In[14]:


len(df) #dataframein uzunluğunu verir


# In[15]:


df.columns #dataframe deki başlıkları gösterir


# In[17]:


df.dtypes #dataframedeki veri tiplerini gösterir


# In[18]:


df.isnull() #Eksik verileri gösterir eksik verilerin olduğu yerlerde true döndürür


# In[20]:


df["Series_Title"][:5] #tek bir sutuna ait verileri getirir


# In[25]:



dr2=df[["Series_Title", "Released_Year"]] #birden çok başlık yazıp değişkene atarsa o değişken dataframe olur


# In[26]:


dr2


# In[29]:


df.sort_values("Released_Year") #dataframede sıralama yapmak için kullanılır


# In[32]:


df["Released_Year"].value_counts() #yıla ait verileri sayar.2014 yılı 14 kez kullanılmış.


# # Verileri Filtreleme

# In[33]:


df["IMDB_Rating"][1] # 1. indexdeki verileri getir.


# In[36]:


df.loc[df["Series_Title"]=="The Godfather"]["IMDB_Rating"] #loc fonksiyonu kullanarak the good father filmine ait raytingi getirdik


# In[38]:


#IMDB_rayting oranı 8 in üstünde olan ve no_of_votes 100000 den çok olan filmleri görelim
df.loc[(df["IMDB_Rating"]>8)&(df["No_of_Votes"]>=100000)]


# In[41]:



#Gross sutunundaki string rakam değerlerini numeric hale getirip aşağıdaki işlemi gerçekleştirdik
df["Gross"]=df["Gross"].str.replace(",","")
df["Gross"]=pd.to_numeric(df["Gross"])



#IMDB_Ratinn değeri 8 in üstünde ve Gross değeri 30000000 dolardan fazla olan filmleri getirelim
df.loc[(df["IMDB_Rating"]>8)&(df["Gross"]>=30000000)]


# # Manuel dataframe oluşturma

# In[46]:


import random
randomlist1=random.sample(range(15,25),2)
randomlist2 =random.sample(range(15,25),2)
randomlist1


# In[47]:


randomlistoflist=[randomlist1,randomlist2]


# In[48]:


randomlistoflist


# In[52]:


columns=["Sıcaklık 1. gün","Sıcaklık 2. gün"]
mydataframe=pd.DataFrame(randomlistoflist,index=["ist","Ankara"],columns=columns)
mydataframe


# In[53]:


type(mydataframe)


# In[54]:


type(df)


# In[ ]:




