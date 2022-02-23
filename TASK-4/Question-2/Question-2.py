#Question-2,program to accept a string from the user and display characters, that are present at an even index number.

a=str(input("Enter the string: "))
for i in range(0,len(a),2):
    print(a[i],end="")
