import pandas as pd

# df=pd.DataFrame({'col1':[1,2,3,4],
#                  'col2':[444,555,666,444],
#                  'col3':['abc','def','ghi','xyz']})
# print(df.head())

# print(df['col2'])
# print(df['col2'].unique())
# print(df['col2'].nunique())
# print(df['col2'].sort_values(ascending=False))
# print(df['col2'].value_counts())

# newdf=df[(df['col1']>2) & (df['col2']==444)]
# print(newdf)

# def times2(x):
#     return x*2
# print(df['col1'].apply(times2))

# print(df['col1'].apply(len)) #*********************
# print(df['col1'].sum())

# del df['col1']
# print(df)

# print(df.isnull())
# print(df.isnull().sum())

# **************************************************
# df=pd.read_csv('example.txt')
# print(df)

# df=pd.read_excel('example_exl.xlsx')
# print(df)

# df.to_excel('i2it.xlsx')
# df.to_csv('i2it_example.csv')

df=pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print(df[0])