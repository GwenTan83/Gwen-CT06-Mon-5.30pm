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

# Existing code to create create_ball function

# Move ball by 'dx' and 'dy'
def move_ball(ball,dx,dy):
    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)




# Existing code to create move_ball function

# Checking for border (x-axis)
def check_x(ball,screenWidth):
    if ball.xcor() > (screenWidth/2) or ball.xcor() < (-screenWidth/2):
        return True
    
# Exisiting code to create 'ball' turtle object
dx=2
dy=2
# Main loop


while True:
    move_ball(ball,dx,dy)
    if check_x(ball,screenWidth):
        dx*=-1
screen.mainloop()

