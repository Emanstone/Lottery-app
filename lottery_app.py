#list of Objects; random, if, else, sys
import random
import sys

winning_number = 3

# Display;
print("Welcome to the lottery game!")
print("Numbers available: 0 - 5")
user_name = input("Enter your name: ")
print("Welcome",user_name)

# Getting user input
user_input = input("Enter number: ")
# Generate a random integer between 1 and 5(inclusive)
randnum = random.randint(1, 5)
# print(randnum

# Converting the input to integers
user_num = int(user_input)
if int(user_num) > 5:
    print("Disqualified! Chosen number beyond specified samples")
    sys.exit() 

 # Printing the user's input   
print("Your chosen number is:", user_num)

# Checking if the user won
if winning_number == user_num == randnum:
    print("Congratulations!", user_name, "You won!")
else:
    print("Sorry",user_name, "you did not win. Better luck next time!")
