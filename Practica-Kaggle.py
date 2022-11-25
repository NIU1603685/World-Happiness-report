#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import KNNImputer

import math
import numpy as np
import pandas as pd
import random
import seaborn as sns
import scipy.stats

# Comanda per ignorar els warnings
np.warnings.filterwarnings('ignore')


# In[2]:


dt_2015 = '2015.csv'

def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset

dt_2015 = load_dataset(dt_2015)
dt_2015.columns


# In[3]:


dt_2015.drop(['Country','Region','Happiness Rank','Dystopia Residual','Standard Error'],axis=1,inplace=True)
dt_2015.columns


# In[4]:


dt_2016 = '2016.csv'
dt_2016 = load_dataset(dt_2016)
dt_2016.columns


# In[5]:


dt_2016.drop(['Country','Region','Happiness Rank','Dystopia Residual',
              'Lower Confidence Interval','Upper Confidence Interval'],axis=1,inplace=True)
dt_2016.columns


# In[6]:


dt_2017 = '2017.csv'
dt_2017 = load_dataset(dt_2017)
dt_2017.drop(['Country','Happiness.Rank','Dystopia.Residual','Whisker.high','Whisker.low'],axis=1,inplace=True)
dt_2017 = dt_2017.rename(columns={'Happiness.Score':'Happiness Score',
                                  'Economy..GDP.per.Capita.':'Economy (GDP per Capita)',
                                  'Health..Life.Expectancy.':'Health (Life Expectancy)',
                                  'Trust..Government.Corruption.':'Trust (Government Corruption)'})

dt_2017.columns


# In[7]:


dt_2018 = '2018.csv'
dt_2018 = load_dataset(dt_2018)
dt_2018.columns


# In[8]:


dt_2018.drop(['Country or region','Overall rank','Social support'],axis=1,inplace=True)
dt_2018 = dt_2018.rename(columns={'Score':'Happiness Score',
                                  'GDP per capita':'Economy (GDP per Capita)',
                                  'Healthy life expectancy':'Health (Life Expectancy)',
                                  'Freedom to make life choices':'Freedom',
                                  'Perceptions of corruption':'Trust (Government Corruption)'})
dt_2018.head()


# In[9]:


dt_2019 = '2019.csv'
dt_2019 = load_dataset(dt_2019)
dt_2019.columns


# In[10]:


dt_2019.drop(['Country or region','Overall rank','Social support'],axis=1,inplace=True)
dt_2019 = dt_2019.rename(columns={'Score':'Happiness Score',
                                  'GDP per capita':'Economy (GDP per Capita)',
                                  'Healthy life expectancy':'Health (Life Expectancy)',
                                  'Freedom to make life choices':'Freedom',
                                  'Perceptions of corruption':'Trust (Government Corruption)'})
dt_2019.head()


# In[11]:


dataset = pd.concat([dt_2015, dt_2016, dt_2017, dt_2018, dt_2019])
dataset


# In[17]:


imputer = KNNImputer()
dataset = pd.DataFrame(imputer.fit_transform(dataset), columns=dataset.columns.values.tolist())
dataset


# In[23]:


data = dataset

dimensio_x = data.values[:, 1:]
dimensio_y = data.values[:, 0]

print("Dimensionalitat de la BBDD:", data.shape)
print("Dimensionalitat de les entrades X", dimensio_x.shape)
print("Dimensionalitat de l'atribut Y", dimensio_y.shape)


# In[ ]:





# In[ ]:





# In[ ]:




