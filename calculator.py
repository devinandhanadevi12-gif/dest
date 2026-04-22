
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

print("Select operation")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice(1/2/3/4):")

if choice==1:
    print("Result:", num1+num2)
elif choice==2:
    print("Result:", num1-num2)
else:
    print(num1*num2)