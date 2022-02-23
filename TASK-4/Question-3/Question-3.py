# Question-3, program that make a 2-dimensional list that contains represents a table of records.

l=[]
b=int(input("Enter the number of entries : "))
print("Enter the Roll Number, Name and Marks one by one \n")
for i in range(b):
    for i in range(3):
        c=input()
        l.append(c)
l1=["Roll","Name","Marks"]
for i in l1:
    print(i,end="   ")
print()
ln=[l[i:i+3] for i in range(0,len(l),3)]
for i in ln:
    for j in i:
        print(j,end="     ")
    print()
print("The second entry : ")
for i in ln[1]:
    print(i,end="     ")
