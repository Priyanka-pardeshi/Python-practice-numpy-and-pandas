import  numpy as np
orignal=np.ones((5,5))
print(orignal)
print("aa",orignal[1:2])
orignal[1:-1,1:-1]=0
print(orignal)