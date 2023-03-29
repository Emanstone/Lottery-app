#list of Objects; range, if, else, sys

import sys

winning_number = 30

# Display;
print("Welcome to the lottery game!")
print("Numbers available: 0 - 50")

# Getting user input
user_input = input("Enter number: ")

# Converting the input to integers
user_num = int(user_input)
if int(user_num) > 50:
    print("Disqualified! Chosen number beyond specified samples")
    sys.exit() 

 # Printing the user's input   
print("Your chosen number is:", user_num)

# Checking if the user won
if winning_number is user_num:
    print("Congratulations! You won!")
else:
    print("Sorry, you did not win. Better luck next time!")
