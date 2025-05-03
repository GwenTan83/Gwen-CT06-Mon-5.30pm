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


# TEST REVISION

# PART 1

# Create a list
students=[
    "yuli",
    "kaius",
    "zirui",
    "lucien"
]
print(students)

# Access list items and change value ; what is the first item?

print(students[1])

students[1]="Gwen"

print(students)

# Size of list

print(len(students))
# Delete items - 2 ways

# del(students[3])

# print(students)

# students.pop(2)
# print(students)

deleted_student = students.pop(2)
print(students)
print(deleted_student + " was removed!")

# Add items - 2 ways

students.append("zirui")
students.insert(1,"kaius")
print(students)

# Print out all the items in the list using a for loop

# access the values in the list

counter = 1

for item in students:
    print(item)