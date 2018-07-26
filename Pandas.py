#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:13:13 2017

@author: Narges
"""

import pandas as pd
import matplotlib as plt
from matplotlib import style
style.use('ggplot')


#%%


web_data={"posts":[1,2,3,4,5,6],
          "shares":[3,2,5,7,3,9],
          "likes":[6,7,6,4,8,8]}
wd=pd.DataFrame(web_data)
print(wd)

#%%
# Creating new cols
col_1 = pd.Series([1,2,3,4])
col_2 = pd.Series(['a','b','c','d'])
