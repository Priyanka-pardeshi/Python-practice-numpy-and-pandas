import pandas as pd

s1=pd.Series([2, 4, 6, 8, 10],index=['a','b','c','d','e'])
s2=pd.Series([1, 3, 5, 7, 9],index=['a','b','c','d','e'])
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)