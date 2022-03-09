import numpy as np
A= np.array(list(map(int,input("Enter elements of Fisrt array seperated by a blank space : ").split())))
B= np.array(list(map(int,input("Enter elements of Second array seperated by a blank space: ").split())))
print(np.allclose(A,B))

