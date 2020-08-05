import pandas as pd
import numpy as np

# create empty Series
s=pd.Series()
print(s)

# create Series from list
data=np.array(['a','b','c','d'])

# create Series from list of Dicts
data={'a' : 0., 'b' : 1., 'c' : 2.}

s=pd.Series(np.random.rand())
print(s)

s=pd.Series(np.random.randint(5,20,5))
print(s)

# create empty DataFrame
d1=pd.DataFrame()
print(d1)

# create DataFrame from list
data=[1,2,3,4,5]
data=[['Ram',10],['Shyam',20],['Sita',30]]
d1=pd.DataFrame(data)

# create DataFrame from ndarrays/list
data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[20,25,28,30]}

# create DataFrame from Dict of series
data={'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
d1=pd.DataFrame(data)

# column Addition
d1['four']=pd.Series([10,20,30],index=['a','b','c'])
print(d1)

# column selection
d2=d1['one']
print(d2)

# column Deletion using del
del d1['four']
print(d1)

# column Deletion using pop
d1.pop('two')
print (d1)

d2=d1['two'] + d1['one']
print(d2)

# Row selection using loc function
d2=d1.loc['b']
print(d2)

# Row selection using iloc function
d2=d1.iloc[0]
print(d2)

# Slice rows
d2=d1[1:3]
print(d2)

# Addition of rows using append function
d2=pd.DataFrame(pd.Series([1,2,3,4],index=['a','b','c','d']))
print(d1)
d1=d1.append(d2)
print(d1)

# Deletion of Rows
d1=d1.drop('a')
print(d1)





















