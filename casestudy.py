# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 17:53:57 2021

@author: HP
"""

#import data to python
url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'

import pandas as pd
df= pd.read_csv(url)
df
df.shape #dimension of data
df.columns
df.head(n=3)
df.tail()
df.describe()
df.dtypes
len(df)
df['region']=df['region'].astype('category')
df.describe()
df.region.value_counts()
df.region.value_counts().plot(kind='bar')

df.sort_values(['custname'])
df.custname.value_counts()
df.custname.value_counts().sort_values(ascending=False)
df.custname.value_counts().sort_values(ascending=False).head(5)
df.custname.value_counts().sort_values(ascending=False).tail(5)

df.groupby('custname').size()
df.groupby('custname').size().sort_values(ascending=False)

#revenue total per customer
df.groupby('custname').revenue.sum().sort_values(ascending=False).head(5)
df.groupby('custname')['revenue'].aggregate([np.sum,max,min,'size']).sort_values(by='sum')

#partnumber brings significant portion of revenue- Maximise revenue from high part numbers or top revenue items
df.columns
df.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum',ascending=False).head(5)
df.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum',ascending=False).tail(5)

#top profit making items
df.groupby('partnum')['margin'].aggregate([np.sum]).sort_values(by='sum',ascending=False).head(5)

#most sold items
df.groupby('partnum').size().sort_values(ascending=False).head(5)

#max revenue region
df.groupby('region')['revenue'].aggregate([np.sum]).sort_values(by='sum',ascending=False).plot(kind='barh')
df[['revenue','region']].groupby('region').sum().sort_values(by='revenue',ascending=False)

