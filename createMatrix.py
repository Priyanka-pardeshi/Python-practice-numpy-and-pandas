import numpy as np
import random
listOfItems=[]
for i in range(0,8):
    lst=random.randint(2,9)
    listOfItems.append(lst)
print("List of items",listOfItems)
matrix=np.array(listOfItems)
print(matrix)