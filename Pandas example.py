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

# Reindexing
data={'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3],index=['a','b','c']),
     'three':pd.Series(np.random.randint(5,15,3),index=['a','b','c'])}
d1=pd.DataFrame(data)
print(d1)
d1_r=d1.reindex(index=[0,2,5],columns=['A','C','B'])
print(d1_r)

d1_r=d1.reindex(index=['a',2,5],columns=['one','C','B'])
print(d1_r)

d1_r=d1.reindex(index=['a',2,5],columns=['one','C','B'])
print(d1_r)

df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2=pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
# Padding NaN
print (df2.reindex_like(df1))
# DataFrame with forward fill
print (df2.reindex_like(df1,method='ffill', limit=1))
# DataFrame with back fill
print (df2.reindex_like(df1,method='bfill'))

# Renaming
df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2=pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
print(df1.rename(columns={'col1':'c1','col2':'c2'},index={0:'apple',1:'banana',2:'durian'}))

# Iteration (Iterating DataFrame)
df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2=pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
for x in df1:
	print(x)

for key,value in df1.iteritems():
	print(key)

for key,value in df1.iteritems():
	print(key,value)

for key,value in df1.iterrows():
	print(key,value)

for key in df1.itertuples():
	print(key)

# Sorting
df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2=pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
usdf=pd.DataFrame(np.random.randn(10,3),index=[1,4,6,2,3,5,9,8,0,7],columns=['col1','col2','col3'])
print(usdf)
sdf=usdf.sort_index()
print(sdf)

sdf=usdf.sort_index(ascending=True)
print(sdf)

sdf=usdf.sort_values(by='col1')
print(sdf)

sdf=usdf.sort_values(by='col1',kind='mergesort')
print(sdf)












