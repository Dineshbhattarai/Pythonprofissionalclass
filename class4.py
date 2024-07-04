'''
StringVariables = ("pythonProgramming")
print(StringVariables[0:1])
print(StringVariables[-11::])
print(StringVariables[::-1])
'''

#password= "answer   "
#newPassword= password.count()
#print(newPassword)
###

'''
String1 = "Hello, I'm a Geek" 
print("Initial String: ")
print(String1)


list1= list(String1)
list1[2] = 'p'
String2 ="".join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)


String3 = String1 [0:2] + 'p' + String1 [3:]

print(String3)

'''


#deleting a character
'''
string1="im a greek"
print("initial  string: ")
print(string1)

del string1
print("\ndeleting entire string:")

print(string1)

'''
'''
#Using slice operator
StudentData=['josh', 'Brown', 10, 70.8 ]
Fruits=["Apple","banana","Cherry","orange","kiwi","milon","mango"]

#accessig list data using index
print(StudentData[1])
print(StudentData[-2])

#Accessing list data using slicing

print(StudentData[0:2])
print(StudentData[1:])
print(StudentData[-4:-1]) 

#related operation in python list

thislist = ["apple","cherry", "banana"]
thislist[1]="blackcurrent"
print(thislist)

#add list item
#using append() method

thislist = ["apple","cherry", "banana"]
thislist.append("orange")
print(thislist)

#using insert() method
thislist = ["apple","cherry", "banana"]
thislist.insert(2,"orange")
print(thislist)


#remove list item 
thislist = ["apple","cherry", "banana"]
thislist.remove("banana")
print(thislist)

#using  pop() method
thislist = ["apple","cherry", "banana"]
thislist.pop(1)
print(thislist)

#if you dont specify the index, then it pop LAst item
thislist = ["apple","cherry", "banana"]
thislist.pop()
print(thislist)

# delete item from list

thislist = ["apple","cherry", "banana"]
del thislist[0]
print(thislist)
'''



#loop  through the list
thislist = ["apple","cherry", "banana"]
for fruits in thislist:
 print(thislist)

 #loop through the index number
  
thislist = ["apple","cherry", "banana"]
for fruits in range(len(thislist)):
 print(thislist)
 





