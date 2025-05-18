# print("Hello from lesson 16")

import turtle
# returns a window that is screenWidth x screenHeight
def setup_screen(screenWidth,screenHeight):
    screen=turtle.Screen()
    screen.setup(width=screenWidth,height=screenHeight)
    return screen

# Setup code
def create_blue_ball():
    ball=turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball
screenWidth=300
screenHeight=500
screen=setup_screen(screenWidth,screenHeight)
ball=create_blue_ball()

# Keeps window open
screen.mainloop()

# Existing code to create create_ball function

# Move ball by 'dx' and 'dy'
def move_ball(ball,dx,dy):
    ball.setx(ball.xcor()+dx)
    

