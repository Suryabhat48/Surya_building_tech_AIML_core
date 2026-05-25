# # IN THIS PARTICULAR FILE WE WILL LEARN ABOUT STRINGS AND OTHER THINGS 
# # String is a data type which is used to store sequence of characters 
# str1="Surya A Bhat"
# str2="is a good guy "
# print(str1+str2)
# # Here this is used to concatenate two strings 
# # To check the length of the string we use len() function 
# print(len(str1))
# # Escape sequences are used in formatting the output 
# # Indexing is used to access individual characters in a string
# print(str1[0]) # This will print the first character of the string
# # Slicing is used to access a range of characters in a string
# #Note:Here remember always the first index is inclusive and the second index is exclusive 
# print(str1[0:5]) # This will print the first five characters of the string
# # we can also do the negative indexing in python I mean to access the characters from the end of the string 
# print(str1[-5:-2])
# # WAP to inputs user name and print its length 
# name=input("Enter your name:")
# print("My name is ",name ,"and I am",len(name),"characters long")
# # for the string functions which are there refer the notes part 
# # Let us take the grade of the student as input and check whether he has passed or not using the conditional statements 
# marks=int(input("Enter your marks"))
# if(marks<=100 and marks>90):
#     print("You got an S grade ")
# elif(marks<=90 and marks>80):
#     print("You got an A grade ")
# elif(marks<=80 and marks>70):
#     print("You got a B grade ")
# elif(marks<=70 and marks>60):
#     print("You got a C grade ")
# elif(marks<=60 and marks>50):
#     print("You got a D grade ")
# elif(marks<=50 and marks>40):
#     print("You got an E grade ")
# else:
#     print("Sorry boss you have failed and you have got the backlog clear the subject in the coming semester and try to score better marks   ")
# # Nesting in the conditional statements basically here we have to write if inside other if condition for example 
# age=int(input("Enter your age:"))
# if(age>=18):
#     if(age>=80):
#         print("You cant drive because you are too old to drive")
#     else:
#         print("You can drive but drive safely")
# else:
#     print("You cant drive because you are underage")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1>num2 and num1>num3):
    print(num1,"is the greatest number")
elif(num2>num1 and num2>num3):
    print(num2,"is the greatest number")
elif(num3>num1 and num3>num2):  
    print(num3,"is the greatest number")
else:    print("All numbers are equal")