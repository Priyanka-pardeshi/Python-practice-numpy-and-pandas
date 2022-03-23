import pandas as pd
import numpy as np
df=pd.DataFrame({'A':[1,2,3,4],
                 'B':pd.Series(1,index=list(range(4)),dtype='float'),
                 'C': [ '2022-03-01',' 2022-03-04', '2022-03-03',' 2022-03-02'],
                 'D':np.array([5]*4,dtype='int32'),
                 'E':pd.Categorical(['true','true','false','false']),
                 'F':'Pandas'
                 })
print(df)
df1=pd.pivot_table(df,index=['C','F'])
print(df1)

# df2=pd.pivot_table(df,index="C",values='A',columns='type')