# Lesson 12 - While Loops

# Recap 1: Multiples of 3 and 5
# Create a program to check if a number is both divisible by 3
# and 5.

# 1. Ask the user to input a number
# 2. Using the '%' operator, check if the number is both a
#    multiple of 3 and 5:
#     If true, print "The number is divisible by 3 and 5!"
# 3. Else, print "The number is not divisible by 3 and 5"

# num=int(input("What number do you want to check?"))
# if num%3==0 and num%5==0:
#     print("The number is divisible by 3 and 5!")
# else:
#     print("The number is not divisible by 3 and 5!")
    

# Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# visitors=0
# while visitors<=50:
#     visitors=visitors+1
#     print("The number of visitors is "+str(visitors))

# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30


# visitors=13
# while visitors<30:
#     visitors=visitors+1
#     print("The number of visitors is "+str(visitors))

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25
# visitors=4
# while visitors<25:
#     visitors=visitors+1
#     print("The number of visitors is "+str(visitors))

# Task 2: while... break
# A restaurant used to have a max capacity of 50. However, due to
# the worsening of the pandemic, the government has restricted the
# max capacity of the restaurant to 30.

# Using an 'if' condition and 'break' within the 'while' loop,
# modify your answer for Task 1a to terminate the 'while' loop when
# number of visitors is 30.

# capacity=0
# while True:
#     capacity=capacity+1
#     print(capacity)
#     if capacity==30:
#         break

# Task 3: Order taking using while loop
# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# **Bonus**
# 1. Modify your code to remove the comma (",") that appears
#    either at the start or end of your sentence

# order=""
# while True:
#     user=(input("What would you like to order?"))
#     if user=="end":
#         break
#     order=order+user+","
#     print(order)
# print(order)


# Task 4: while... else
# The else condition will run when the loop exits normally.
# i.e. when the while condition is no longer true.

# Using 'else', create a program that will count from 10 to 1,
# before printing "Happy New Year!"

# **Task 4a**:
# Using a 'while' loop:
# 1. Print the numbers from 10 to 1
# 2. Once count reaches 1, use 'else' to print
#    "Happy New Year!"

# **Task 4b**:
# Now, modify your 'while' loop from Task 4a such that:
# 1. If the number is 5, 'break' out of the loop
# 2. Ensure your code has an 'else'

# Observe that "Happy New Year!" is no longer printed

# num=11
# while num>1:
#     num=num-1
#     print(num)
# else:
#     print("Happy New Year!")

# num=11
# while num>5:
#     num=num-1
#     print(num)
#     break
# else:
#     print("Happy New Year!")

# Task 5: Math Question
# **Task 5a**:
# Create a program to test the user on their math skills! The
# program will continue generating new questions until the user
# get the wrong answer.

# 1. Using a 'while' loop, 
# 2. Generate 2 random numbers between 1 and 10 (import 'random'
#    and use 'random.randint()')
# 3. Ask the user to add the 2 numbers together in the following
#    format:
#     "What is 3 + 5?"
# 4. If the user gets the correct answer:
#     Print "That's correct!
# 5. Else:
#     print "Wrong! Try again"
#     End the 'while' loop
    

import random
num=input(int("Input 2 numbers."))
while num>1 and num<10:
    input(int("What is the total of the 2 numbers?"))

