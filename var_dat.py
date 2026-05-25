print("Hello, World!")
# We will start from the first thing and this is the chappter 1  Variables and Data types 
print("Hey my name is Surya","and I am 19 years old  and I am a student of computer science engineering and AIML")
# Variables are used to store data in a program. In Python, you can create a variable by simply assigning a value to it. For example:``
name = "Surya"
age = 20
print(name)
print(age)
# So basically in python we have five data types Sring,,Integer,Float,Boolean and None 
# a=None
# print(a)
# basically by none we mean we cant assign any value for that variable specifically use the capital T and F for boolean types
# Program to find sum of two numbers 
a=10
b=20
sum=a+b
print("The sum of a and b is :",sum)
# There are two types of comments which we write single line comment and multi line comment for single line comment we use # and for multi line comment we use """ on both sides """
# Input taking functionn in user is used to take input from the user input() function 
name=input("Enter your name:")

# By default input function takes input as a string if we want to take the input in other forms we basically have to typecast things
age=int(input("Enter your age:"))

# We can also take input in float form
height=float(input("Enter your height in cm:"))
print("Hello this is ",name)
print("Your age is ",age,"years")
print("Your height is ",height,"cm")    
# Next we are here to learn about the conditional statements in python which are used to make decisions 
# Syntax 
# if(condition):
#     # code to be executed if condition is true
# elif(condition):
#     # code to be executed if the above condition is false and this condition is true
# else:
#     # code to be executed if all the above conditions are false
light_color=input("Enter the traffic light color (red, yellow, green):")

if light_color=="red":
    print("Stop")
elif light_color=="yellow":
    print("Get ready to move")
elif light_color=="green":
    print("Go")
else:
    print("Invalid traffic light color")
# ternary operator helps take decisions in a single line of code 
# syntax : <statement1> if <condition> else <statement2>
food=input("Enter your favorite food:")
print("I like ",food)if food=="burger" else print("I don't like ",food)
# clever if condition syntax : val=(false_value, true_value)[condition]
age=int(input("Enter your age:"))
status=("Voter", "Non-Voter")[age<18]
print("You are a ",status)
# For the operator part pleased do refer the notes part 
# Question:Write a program to take two numbers as input from the user and print their sum 
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
sum=num1+num2
print("The sum of ",num1,"and",num2,"is",sum)
# WAP to take the side of a square as input and calculate its area 
side=float(input("Enter the side of the square:"))
area=side*side
print("The area of the square is:",area)
# WAP to take two floating point numbers as input and print their average 
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
average=(num1+num2)/2
print("The average of ",num1,"and",num2,"is",average)
# WAP to take two integers and check whether they are greater than or not 
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    print(num1,"is greater than",num2)
elif num2>num1:
    print(num2,"is greater than",num1)
else:
    print("Both numbers are equal")