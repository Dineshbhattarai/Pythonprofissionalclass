#Write a program to print multiplication table of a given number(accept number from user)
#eg. if user input 3
#3 x 1 = 3
#3 x 2 = 6 and so on
  
user_input=int(input("Enter the number for multiplication"))
for i in range(1,11):
     print(user_input, 'x', i, '=', user_input*i)



     '''
      Accept 10 numbers from user and display average of it.
      '''

# Initialize an empty list to store the numbers
numbers = 0

# Get 10 numbers from the user
for i in range(10):
    num = float(input("Enter number : "))
    average = numbers + num



# Display the average
print("The average of the entered numbers is:",average/2,)


#Write a program to display numbers which is divisible by only 11 from 100 to 300.
