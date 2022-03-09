import numpy as np
print("Exercise 1: Addition of array")
print("-----------------------------")
array1 = np.array(list(map(int,input("Enter elements of Fisrt array seperated by a blank space  : ").split())))
array2 = np.array(list(map(int,input("Enter elements of Second array seperated by a blank space : ").split())))
print("Added array =",np.add(array1,array2))
print("-----------------------------")
print("Exercise 2: Getting the positions (indexes) where elements of 2 numpy arrays match ")
print("-----------------------------")
arr1 = np.array(list(map(int,input("Enter elements of Fisrt array seperated by a blank space  : ").split())))
arr2 = np.array(list(map(int,input("Enter elements of Second array seperated by a blank space : ").split())))
print("Indexes of elements where 2 elements of arrays match :",end=" ")
for i in range(len(arr1)):
    if(arr1[i]==arr2[i]):
        print(i+1,end=" ")

