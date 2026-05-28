print("Hello welcome to the calculator program let us know what would you like to do ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice=int(input("Enter your choice: "))
lst1=int(input("Enter the numbers you want to perform the operation on:"))
class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            return "Cannot divide by zero"
        return a/b
calc=Calculator()
if choice==1:
    print("The sum is:",calc.add(lst1,lst1))
elif choice==2:
    print("The difference is:",calc.subtract(lst1,lst1))
elif choice==3:
    print("The product is:",calc.multiply(lst1,lst1))
elif choice==4:
    print("The quotient is:",calc.divide(lst1,lst1))
else:
    print("Invalid choice")