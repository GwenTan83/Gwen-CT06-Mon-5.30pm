# # Lesson 15 - Functions

# ## Recap 1: Turtle drawing
# **Recap 1a**:
# Using the 'turtle' library, create a 200x200 window


# 1. Import 'turtle' library
# 2. Using '.setup()', create a window 200 in width and 200 in height
# 3. Add a '.mainloop()' function to keep the window open

# **Recap 1b**:
# Modify your previous code to create a blue arrow as your turtle.

# 1. Create a turtle called "artist" using 'turtle.Turtle()'
# 2. Using '.shape()', change the turtle shape to "arrow"
# 3. Using '.color()', change the turtle color to "blue"

# **Recap 1c**:
# Modify your previous code to draw the shape of a compass rose (shown
# on screen)

# 1. Use '.penup()' and position turtle to (0, 0) using '.goto()'
# 2. Point turtle towards North ("90") using '.seth()'
# 3. Use '.pendown()' and draw "60" towards North
# 4. Using '.right()', turn turtle 90 degrees to the right 
# 5. Using a 'for' loop, draw a circle by moving 1 step each time
#    before turning 1 degree to the right for 360 times.

# import turtle
# window=turtle.Screen()
# window.setup(200,200)
# artist=turtle.Turtle()
# artist.shape("arrow")
# artist.color("blue")
# artist.penup()
# artist.goto(0,0)
# artist.seth(90)
# artist.pendown()
# artist.forward(60)
# artist.right(90)
# for _ in range(360):
#     artist.forward(1)
#     artist.right(1)
# window.mainloop()

# 1. Import 'turtle' library
# **Recap 1d**:
# Modify your previous code to print the position of your turtle at the
# end of the drawing.

# 1. Using '.xcor()' and 'ycor()' and '.write(text)', print your turtle's
#    last coordinates in the following format:

#    "Current turtle position: <x>, <y>"


# ## Task 1: Self-introduction
# You are at a party, and you expect to see your friend Ethan and 3 of
# his friends you have never met before. They are Ben, Gracie, and
# Javior.

# Write a program (with or without functions) that will ask the user
# for their name and print 1 of 3 ways to greet the person:
# 1. If the person is Ethan, greet him by saying:
#         "Hi Ethan. How are you?"
# 2. If the person is either Ben, Gracie, or Javior, greet them by
#    saying:
#         "Hi there!"
#         "My name is Freddo"
#         "I like to swim and eat chicken wings!"
#         "Nice to meet you!"
# 3. If the person is none of the above, say:
#         "I don't think you belong here..."

# def greet():
#     print("Hi there!")
#     print("My name is Freddo")
#     print("I like to swim and eat chicken wings!")
#     print("Nice to meet you!")

# person=input("What is your name?")

# if person=="Ethan":
#     print("Hi Ethan. How are you?")
# elif person=="Ben" or person=="Gracie" or person=="Javior":
#     greet()
# else:
#     print("I don't think you belong here...Get out")

## Task 2: Square
# Using the 'turtle' library, create a function that draws a square.
# Use the function you have created to draw the pattern shown on the
# screen.

# 1. Import the 'turtle' library
# 2. Set up the screen using 'turtle.Screen()'
# 3. Create a function, "draw_square" that will draw a 20x20 square
# 4. Using 'for' loops and the "draw_square" function you have created,
#    draw the pattern shown on the screen.
# 5. You will have to reposition your turtle before calling the
#    "draw_square" function each time.

import turtle
window=turtle.Screen()
window.setup(500,500)
t=turtle.Turtle()
def draw_square():
    t.pendown()
    for _ in range(4):
        t.forward(20)
        t.right(90)
t.penup()
t.goto(0,0)
num_squares=6
for _ in range(3):
    for _ in range(num_squares):
            draw_square()
            t.forward(20)
    t.backward(num_squares * 20)

# Task 6: Greetings III
# Create a function that takes in a name and returns a greeting

# 1. Create a function named 'greet()'
# 2. The function should return a greeting
#     Example: "Hello there !"
# 3. Ask the user for their name
# 4. Using the 'greet()' function, print the greeting
