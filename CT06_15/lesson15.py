# # Lesson 15 - Functions

# ## Recap 1: Turtle drawing
# **Recap 1a**:
# Using the 'turtle' library, create a 200x200 window
import turtle
window=turtle.Screen()
window.setup(200,200)
artist=turtle.Turtle()
artist.shape("arrow")
artist.color("blue")
window.mainloop()
artist.penup()
artist.goto(0,0)
artist.seth(90)
artist.pendown(60)
artist.right(90)
for _ in range(360):
    artist.forward(1)
    artist.right(1)
window.mainloop()

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

# **Recap 1d**:
# Modify your previous code to print the position of your turtle at the
# end of the drawing.

# 1. Using '.xcor()' and 'ycor()' and '.write(text)', print your turtle's
#    last coordinates in the following format:

#    "Current turtle position: <x>, <y>"

