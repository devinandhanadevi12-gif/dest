#palindrome
p = input("enter a string:")
if p == p[::-1]:
    print("it is a palindrome") 
else:
    print("it is not a palindrome")
    