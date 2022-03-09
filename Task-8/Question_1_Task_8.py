import numpy as np
f=int(input("First Number: "))
l=int(input("Last Number: "))
z=np.zeros(((l-f)*5)+(l-f+1))
for i in range(0,len(z),6):
    z[i]=f
    f=f+1
print(z)
