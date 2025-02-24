#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


movies_ds = pd.read_csv("imdb_top_1000.csv")


# In[10]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[76]:


movies_ds


# In[77]:


movies_ds=movies_ds[['Series_Title','Released_Year','Genre','Overview','Meta_score']]


# In[78]:


movies_ds.head()


# In[79]:


movies_ds.info()


# In[80]:


movies_ds.isnull().sum()


# In[85]:


movies_ds = movies_ds.copy()
movies_ds.dropna(inplace=True)


# In[82]:


movies_ds.isnull().sum()


# In[86]:


movies_ds.duplicated().sum()


# In[117]:


movies_ds['Tags'] = movies_ds['Overview']+movies_ds['Genre']


# In[118]:


movies_ds.head()


# In[119]:


short_data = movies_ds.drop(columns=['Overview', 'Genre',])


# In[120]:


movies_ds.head()


# In[121]:


short_data


# In[122]:


from sklearn.feature_extraction.text import CountVectorizer


# In[123]:


vec=CountVectorizer(max_features=1000, stop_words='english')


# In[124]:


vec


# In[125]:


vector=vec.fit_transform(short_data['Tags'].values.astype('U')).toarray()


# In[126]:


vector.shape


# In[127]:


from sklearn.metrics.pairwise import cosine_similarity


# In[128]:


similar=cosine_similarity(vector)


# In[129]:


similar


# In[130]:


short_data[short_data['Series_Title']=="The Dark Knight"]


# In[131]:


short_data[short_data['Series_Title']=="The Dark Knight"].index[0]


# In[152]:


def recommend(movies):
    index=short_data[short_data['Series_Title']==movies].index[0]
    distance = sorted(list(enumerate(similar[index])), reverse=True, key=lambda vector:vector[1])
    for i in distance[0:5]:
        print(short_data.iloc[i[0]].Series_Title)


# In[153]:


recommend("The Dark Knight")


# In[154]:


recommend("The Godfather")


# In[155]:


import pickle


# In[156]:


pickle.dump(short_data, open('movies_list.pkl', 'wb'))


# In[157]:


pickle.dump(similar, open('similar.pkl', 'wb'))


# In[158]:


pickle.load(open('movies_list.pkl', 'rb'))


# In[159]:


pickle.load(open('similar.pkl', 'rb'))


# In[ ]:




