# Write a program to display "hello"if a number entered by a user is a 
# multiple of five or not..

'''
Number=int(input("Enter the Number"))
if Number%5==0:
    print("hello")
else:
    print("bye")
'''
# for loop examples
'''
text = " pythonprogramming"
for i in text:
    print(i)

    # for loop with else

fruits = ["apple","banana","grapes"]
for index in range(len(fruits)):
    print(fruits[index])
else:
    print("inside Else Blocks")
    print(len(fruits))

    # while loop
    count = 0
    while (count <3 ):
       count = count +1
       print("Hello Programmers")
    else:
        print("in Else Block")
'''

# nested for loop

#adj = ["red","big","tasty"]
#fruits = ["apple","grapes","cherry"]
#for x in adj:
 #   for y in fruits:
 #       print(x,'\t',y, '\n')



        # nested for loop

for i in range(1, 5):
    for j in range(i):
     print(i,  end='')
    print()


    # for while loop 

    i=1
    while i < 10:
       j = i
       while j < 10:
          print (f"{j}", end="")
          j = j + 1
          print ("")
          print("completed")

     