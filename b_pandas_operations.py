import pandas as pd
df=pd.DataFrame([2,44,5,6,77787,45,67])
replace=df.replace(44,23)
print(replace)
print("###########################################################################################################################")

df1=pd.DataFrame({'A':[1,3],'B':[4,5]})
df1=df1.T
print("Transpose of dayaframe")
print(df1)
print("##########################################################################################################################3")

df3=pd.DataFrame({'col1':[2,4,6,8,10],
                  'col2':[3,6,9,12,15],
                  'col3':[4,8,12,16,20]})
print(df3)
print(df.shift(periods=1,axis="columns"))
