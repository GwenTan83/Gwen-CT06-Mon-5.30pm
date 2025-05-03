# print("Hello from lesson 14")

# import turtle
# window=turtle.Screen()
# window.setup(width=600,height=400)
# t=turtle.Turtle()
# t.fillcolor("orange")
# t.shape("turtle")
# t.speed(50)

## Task 3: Drawing
# Given the number of sides and each interior angle, draw each of the
# following shapes using a loop and the following functions:
#     .seth()
#     .up()
#     .down()
#     .forward()
#     .backward()
#     .left()
#     .right()

# **Task 3a**: Draw a line
# Number of sides: 1
# Interior angle: NA

# **Task 3b**: Draw a triangle
# Number of sides: 3
# Interior angle: 120

# **Task 3c**: Draw a square
# Number of sides: 4
# Interior angle: 90

# **Task 3d**: Draw a pentagon
# Number of sides: 5
# Interior angle: 72

# **Task 3e**: Draw a hexagon
# Number of sides: 6
# Interior angle: 60

# **Task 3f**: Draw a circle
# Number of sides: 360
# Interior angle: 1

# import turtle
# window=turtle.Screen()
# window.setup(width=600, height=400)
# t=turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("orange")
# t.down()
# t.speed(10)
# for _ in range(3):
#     t.forward(100)
#     t.left(360/3)

# import turtle
# window=turtle.Screen()
# window.setup(width=600, height=400)
# t=turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("orange")


# window.mainloop()

import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
t.seth(0)
t.pendown()
t.foward(100)
window.mainloop()

# TEST REVISION

# PART 1

# Create a list
# students=[
#     "yuli",
#     "kaius",
#     "zirui",
#     "lucien"
# ]
# print(students)

# Access list items and change value ; what is the first item?

# print(students[1])

# students[1]="Gwen"

# print(students)

# Size of list

# print(len(students))
# Delete items - 2 ways

# del(students[3])

# print(students)

# students.pop(2)
# print(students)

# deleted_student = students.pop(2)
# print(students)
# print(deleted_student + " was removed!")

# Add items - 2 ways

# students.append("zirui")
# students.insert(1,"kaius")
# print(students)

# Print out all the items in the list using a for loop

# access the values in the list

# counter = 1

# for item in students:
#     print(str(counter)+". "+ item)
#     counter += 1

#using range

# for i in range(len(students)):
#     print(str(i + 1) + ". " + students[i])

# PART 2

# Print numbers from 1 - 10 using a while loop 
# Next, print in multiples of 2

# i=1
# while i <=10:
#     print(i)
#     i += 2

# PART 3

# What is str?
# str="hi!"
# str="hi-"
# str=str * 3
# print(str)

# What's going to be printed here?
# a=10
# b=5
# if a>b:
#     print("BIGGER!")
# else:
#     print("SMALLER!")

# If no tab: indentation error

# What are the possible outputs? Will my code run without errors?

# import random
# print(random.randint(1,2))

# What will be printed?
# num=5
# if num>4:
#     print("Num is bigger than 4")
# elif num>2:
#     print("Num is bigger than 2")
# else:
#     print("Num is 2 or smaller")

# What happens when I run this code?
# num_students=20
# print("There are " + str(num_students) + " in this class.")

# How do you compare values?
# Is equal to... ==
# Is not equal to... !=
# More than... >
# Less than... <
# More than or equal to... >=
# Less than or equal to... <=

# How do you write Boolean values? (Capital letters)
# True
# False

# What is break statement for?
# To break a forever loop.
# Can you use break to exit for loop? YES
# Cannot use for if else as if else is not a loop.
# In a loop where we retrieve each student's score, when should we sum up the scores to get the average score? Inside the loop? Outside the loop.

# How do we print "Hi there!" into the terminal shell output?
# print("Hi there!")

# What index do we start with in a list? 0

# How to check if a number, i, is even?
# if 1 % 2 == 0: