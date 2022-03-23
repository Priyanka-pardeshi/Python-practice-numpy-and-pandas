import pandas as pd
import numpy as np

s=pd.Series([1,2,3,4,5,6,np.nan,7,8,9])
print("Pandas Series:",s)


data_dates=pd.date_range('20220301',periods=10)
print(data_dates)
data_frame=pd.DataFrame(np.random.randn(10,4),index=data_dates,columns=['a','b','c','d'])
print("Pandas data frame is:")
print(data_frame)
print("fisrt 5 records:")
print(data_frame.head(5))
print("last 5 records:")
print(data_frame.tail(5))
print("###############################################################################################################################################################################")
print("example of dataframe:")
df=pd.DataFrame({'A':[1,2,3,4],
                 'B':pd.Series(1,index=list(range(4)),dtype='float'),
                 'C': pd.Timestamp('20220301'),
                 'D':np.array([5]*4,dtype='int32'),
                 'E':pd.Categorical(['true','true','false','false']),
                 'F':'Pandas'
                 })
print("data frame is:")
print(df)
print("Data types of df:",df.dtypes)
print("get index:",df.index)
print("get column:",df.columns)
print("Converst to numpy array:",df.to_numpy())
print("description data frame:")
print(data_frame.describe())
print("###########################################################################################################################################")
print("Sored one column:")
print(df.sort_values(by='C'))
print("get column:",df['A'])
print("get row i.e slicing", df[0:2])
print(df)
print(df.mean())
# merge,join,operations on pd