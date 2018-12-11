# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:37:50 2018

@author: as
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("exams.csv")
X = dataset.iloc[:,[5,6,7]]
group = dataset['race/ethnicity'].unique()
group.sort()
pos = np.arange(len(group))
X.groupby('math score').size()

Y = X['math score'].value_counts()

df = Y.to_frame().reset_index()

plt.bar(df['index'],df['math score'])
plt.show()

# Grouping the gander based on groups 

gender_sep = dataset.iloc[:,[0,1]]
Male = gender_sep[(gender_sep['gender'] == 'male')].groupby(['race/ethnicity'],as_index=False).agg('count')
plt.bar(group,Male['gender'],align='center', alpha=0.5,label='male')
Female = gender_sep[(gender_sep['gender'] == 'female')].groupby(['race/ethnicity'],as_index=False).agg('count')
plt.bar(group,Female['gender'],align='center', alpha=0.5,color='r',label='female')
plt.xticks(pos,group)
plt.legend()
plt.xlabel('Groups')
plt.ylabel('Count')   
plt.show()

#Classiflying the people with possible test preparation course
gen = dataset['test preparation course'].unique()
gen_pos = np.arange(len(gen))
bar_width = 0.35
data = dataset.iloc[:,[0,4]]

Male_prep = data[(data['gender'] == 'male')].groupby(['test preparation course'],as_index=False).agg('count')
Female_prep = data[(data['gender'] == 'female')].groupby(['test preparation course'],as_index=False).agg('count')
plt.bar(gen_pos,Male_prep['gender'],bar_width,label='Male')
plt.bar(gen_pos+bar_width,Female_prep['gender'],bar_width,label='Female')
plt.xlabel('test preparation course')
plt.ylabel('Count')
plt.title('Scores by person')
plt.xticks(gen_pos+bar_width,gen)
plt.legend()
 
plt.tight_layout()
plt.show()

#
