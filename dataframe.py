# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:22:43 2021

@author: HP
"""

#make a dataframe file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

course= pd.Series(['Btech','Mtech','ME','MBA'])
strength= pd.Series([100,25,26,50])
fees= pd.Series([18,12,15,10])

pd1= pd.DataFrame([course,strength,fees])
pd1 #not the correct method

#better way to ,ake a dataframe
pd2= pd.DataFrame({'course':course,'strength':strength,'fees':fees})
pd2
pd2.index
pd2.columns
