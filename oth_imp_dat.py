# # So basically in this file we are going to learn about the other important data types in python which are lists,tuples,dictonaries and sets and along with those things we want to learn about the loops in python 
# # Lists are used to store multiple items in a single variable and they are ordered and mutable unlinke strings 
# my_list=[1,2,3,4,5]
# print(my_list)
# # We can also store different data types in a list
# my_list=[1,"Surya",3.14,True]
# print(my_list)
# # We can also have nested lists in python
# my_list=[1,2,[3,4],5]
# print(my_list)
# # We can access the elements of a list using indexing and slicing just like strings
# print(my_list[0]) # This will print the first element of the list
# print(my_list[2][0]) # This will print the first element of the nested list
# # We can also modify the elements of a list using indexing
# my_list[0]=10
# print(my_list)
# # We can also do the slicing in the list 
# print(my_list[0:3]) # This will print the first three elements of the list
# # Note:Here in slicing remember one thing that the first index is inclusive and the second index is exclusive 
# # Here we can also do the negative indexing in python to access the elements from the end of the list 
# print(my_list[-1]) # This will print the last element of the list
# print(my_list[-3:-1]) # This will print the third and second last element of the list 
# # LIST METHODS 
# # We can also add elements to the list using append() method
# my_list.append(6)
# print(my_list)
# # We can also insert elements at a specific position using insert() method
# my_list.insert(0,0)
# print(my_list)
# # We can also remove elements from the list using remove() method
# my_list.remove(3.14)
# print(my_list)
# # We can also pop elements from the list using pop() method which removes the last element of the list by default
# my_list.pop()
# print(my_list)
# # We can also clear the list using clear() method which removes all the elements from the list
# my_list.clear()
# print(my_list)
# # Note: If we try to print the list.sort we would get the none type because whatever the changes we make in the list happens in the original list only thats why 
# my_list=[5,2,3,1,4]
# my_list.sort()
# print(my_list)  
# # for reversing the list we can use the reverse() method
# my_list.reverse()
# print(my_list)
# These are the practice programs given 
# mov1=input("Enter the first favorite movie name:")
# mov2=input("Enter the second favorite movie name:")
# mov3=input("Enter the third favorite movie name:")
# list1=[mov1,mov2,mov3]
# print("My favorite movies are:",list1)
# # Program to check whether a given list contains a palindrome or not 
# list2=[1,2,3,2,1]
# # list3=list2.reverse() here basically it will reverse the list but it will return none type because the changes happens in the original list only
# list3=list2.copy() # here we are copying the list to another list and then we will reverse the second list and then we will compare both the lists
# list3.reverse()
# print(list2==list3)
# # TUPLES are used to store multiple items in a single variable and they are ordered and immutable unlike lists
# my_tuple=(1,2,3,4,5)
# print(my_tuple)
# # We can also store different data types in a tuple
# my_tuple=(1,"Surya",3.14,True)
# print(my_tuple)
# # We can also have nested tuples in python
# my_tuple=(1,2,(3,4),5)
# print(my_tuple)
# # We can access the elements of a tuple using indexing and slicing just like lists
# print(my_tuple[0]) # This will print the first element of the tuple
# print(my_tuple[2][0]) # This will print the first element of the nested tuple
# # We can also do the slicing in the tuple
# print(my_tuple[0:3]) # This will print the first three elements of the tuple
# # Note:Here in slicing remember one thing that the first index is inclusive and the second index is exclusive
# # Here we can also do the negative indexing in python to access the elements from the end of the tuple
# print(my_tuple[-1]) # This will print the last element of the tuple
# print(my_tuple[-3:-1]) # This will print the third and second last element of the tuple
# Now we will solve somem things related to the tuples 
# WAF to count the number of students with A grade for this tuple 
tup=('C','D','A','B','A','C','D','A')
print(tup.count('A'))
# STORE ALL OF THEM IN THE LIST AND THEN SORT IT 
list1=list(tup)
list1.sort()
print(list1)
# Now we will learn about the dictionaries in python which are used to store dat in key value pairs and they are unordered and mutable unlike lists and tuples 
my_dict={"name":"Surya","age":20,"city":"Bangalore"}    
print(my_dict)
# We can also store different data types in a dictionary
my_dict={"name":"Surya","age":20,"city":"Bangalore","is_student":True}
print(my_dict)
# We can also have nested dictionaries in python
my_dict={"name":"Surya","age":20,"city":"Bangalore","is_student":True,"marks":{"maths":90,"science":95}}
print(my_dict)
# We can access the elements of a dictionary using keys
print(my_dict["name"]) # This will print the value of the key "name"    
print(my_dict["marks"]["maths"]) # This will print the value of the key "maths" in the nested dictionary "marks"
# We can also modify the elements of a dictionary using keys
my_dict["age"]=21
print(my_dict)
# We can also add new key value pairs to the dictionary
my_dict ["country"]="India"
print(my_dict)
# We can also remove key value pairs from the dictionary using del keyword
del my_dict["is_student"]   
print(my_dict)  
# We can also clear the dictionary using clear() method which removes all the key value pairs from the dictionary   
my_dict.clear()
print(my_dict)  
# Dictionary methods 
# .keys() method is used to get all the keys of the dictionary
my_dict={"name":"Surya","age":20,"city":"Bangalore"}
print(my_dict.keys())
# .values() method is used to get all the values of the dictionary
print(my_dict.values())
# .items() method is used to get all the key value pairs of the dictionary as a list of tuples
print(my_dict.items())
# .get() method is used to get the value of the key entered 
# Note :We have two methods to get the value of the key in a dictionary one is using the square brackets and the other one is using the get() method but the difference between them is that if we try to access a key which is not present in the dictionary using square brackets then it will raise an error but if we try to access a key which is not present in the dictionary using gett() method then it will return None instead of raising an error 
print(my_dict.get("name")) # This will print the value of the key "name"
print(my_dict.get("country")) # This will print None because the key "country" is