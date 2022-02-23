# Question-4,program to check if the given number is a palindrome number.

a=str(input("Enter the Number to be checked: "))
b=a[::-1]
if b==a:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
