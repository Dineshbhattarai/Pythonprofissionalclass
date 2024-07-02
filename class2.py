# using operators
'''

first_Number=4
second_Number=7
print("the addition is",(first_Number+second_Number))
print("the substraction is",(first_Number-second_Number))
print("the multiplication is",(first_Number*second_Number))
print("the division is",(first_Number/second_Number))
print("the modulus is",(first_Number%second_Number))
print("the floor division is",(first_Number//second_Number))
print("the exponentiatial is",(first_Number**second_Number)) 



#assignment operator 

num1= 55
num2= 200

print(num1>num2)
print(num1!=num2)
print(num1==num2)
print(num1<num2)
print(num1<=num2)
print(num1>=num2)

'''

#identity operators
'''

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)

# membership operators
fruit ="banana"
print("a" in fruit)
print("v"in fruit)


'''

# ternary operators

#  syntax: [on_true] if [expression] else [on_false]
a,b =10,20

firstValue= a if a<b else b

print(firstValue)

secondValue = a if a>b else b
print(secondValue)



# if else statement
#if syntax  if< conditions
# <statemet>


# if statement
'''
i= 10
if(i>12):
    print("10 is less then 12")


    # if-else condition
    if (10>5):
        print("wrong")
    else:
        print("10 is greater than 5")



# Nested if  statement

x = 41
if x> 10:
    print ("above 10")

    if x>20:
        print("and also above 20")
    else:
        print("but not above 20")
'''
        # if elif ladder statement
'''
 i = 25
   if(i==10):
 print("i is 10")
 elif(i==15):
print("i is 15")
 elif(i == 20):
 print("i is 20")
else:
 print("i is not present")
        ;'''     


               # Gets user inputs
name = input("what is your name?")
print("welcome", name)
