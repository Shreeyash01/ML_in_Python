import pandas as pd
import numpy as np

l1=[1,2,3,4,5]
l2=['Pune','Mumbai','Nasik','Delhi','Hyderabad']
d={'p':300,'q':400,'r':500,'s':600,'t':700,}
arr=np.arange(1000,1005)

p1=pd.Series(l2)
# print(p1)

p2=pd.Series(l2,arr)
# print(p2)
p3=pd.Series(arr,l2)
# print(p3)

p4=pd.Series(data=arr,index=l2)
# print(p4)

p5=pd.Series(d)
# print(p5)

p6=pd.Series(arr,d)
# print(p6)

s1=pd.Series({'Pune':1,'Mumbai':2,'Nasik':8,'Delhi':3,'Hyderabad':5})
s2=pd.Series({'Pune':1,'Mumbai':2,'Nasik':8,'Chennai':3,'Hyderabad':5})
# print(s1+s2)

p7=pd.DataFrame(np.random.randn(20).reshape(5,4),index=['A','B','C','D','E'],columns=['W','X','Y','Z'])
# print(p7)
# print(type(p7))
# print(p7['W'])
# print(type(p7['W']))
# print(p7[['W','X']])
# print(type(p7[['W','X']]))

# print(p7.loc['D'])
# print(p7.iloc[3])
# print(p7['W']>0)
# print(p7[p7['W']>0])
# print(p7[p7['W']>0]['Y'])

# a=['a','b','c']
# r=[]
# for v in a:
#     r.append(v.upper())
# print(r)

# n=input() #******************************************************************************************
# r=str(n)[::-1]
#
# s=int(n)+int(r)
# q=str(s)
#
# while(True):
#     if q==q[::-1] :
#         break
#     else:
#         q=str(int(q)+int(q[::-1]))

# print(q) #*******************************************************************************************

# print(p7['W'].apply(lambda x:x>0))

p7['new']=p7['W']+p7['Y']
# # print(p7)
p7.drop('new',axis=1,inplace=True)
# print(p7)
# print(p7.drop('E',axis=0))
# print(p7.loc[['A','B'],['W','Y']])

newind='CA NY WY OR CO'.split()
p7['States']=newind
# print(p7)

# print(p7.set_index('States'))

p8=pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]})
print(p8)

# print(p8.dropna())
# print(p8.dropna(axis=1))

# print(p8.dropna(thresh=2)) # at least 2 non na

# print(p8.fillna(value='fill'))
# print(p8['A'].fillna(value=p8['A'].mean()))

data={'Company':['Goog','Goog','Msft','Msft','Fb','Fb',],
      'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
      'Sales':[200,120,340,124,243,350]}
p9=pd.DataFrame(data)
print(p9)
# print(p9.sum())

by_comp=p9.groupby('Company')
# print(by_comp.mean())
# print(by_comp.std())
# print(by_comp.min())
# print(by_comp.count())
print(by_comp.describe())



