# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:48:19 2021

@author: HP
"""

import matplotlib.pyplot as plt
import pandas as pd

math=[20,50,25,35,40]
science=[25,45,22,40,35]
indexNo = ['S1','S2','S3','S4','S5']
df = pd.DataFrame({'math':math, 'science':science}, index=indexNo)
df
df.plot(kind='scatter', x='math', y='science')
plt.scatter(df['math'], df['science'], s = 20, c = 'k')

from scipy.cluster.hierarchy import dendrogram , linkage
#Linkage Matrix
Z = linkage(df, method = 'ward')
 
#plotting dendrogram
df
dendro = dendrogram(Z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()
df

from scipy.spatial import distance
import numpy as np
distance.euclidean([1, 0, 0], [0, 1, 0])
distance.euclidean([20,25],[25,22])  #closest : S1 with S2
np.sqrt(((20-25)**2 + (25-22)**2)) #sqrt(sum(x-y)^2)

distance.euclidean([20,25],[35,40]) 
distance.euclidean([20,25],[40,35])
distance.euclidean([35,40],[40,35])

#distance of all points in DF
from sklearn.neighbors import DistanceMetric
dist = DistanceMetric.get_metric('euclidean')
dist
df.to_numpy()
dist.pairwise(df.to_numpy())

#k-means clustering
from sklearn.cluster import KMeans
kmeans= KMeans(n_clusters=2).fit(df)
centeriods= kmeans.cluster_centers_
print(centeriods)
df
plt.scatter(df['math'],df['science'],c= kmeans.labels_.astype(float),s=50, alpha=0.5)
plt.scatter(centeriods[:,0],centeriods[:,1],c='red',s=50,marker='D')
plt.show()
kmeans.fit(df)
kmeans.inertia_
kmeans.cluster_centers_ #average or rep values
kmeans.n_iter_ #in n times the cluster stablised
kmeans.labels_

df.groupby(kmeans.labels_).mean()
