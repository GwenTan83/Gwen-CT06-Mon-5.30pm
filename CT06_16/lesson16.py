print("Hello from lesson 16")

import turtle
# returns a window that is screenWidth x screenHeight
def setup_screen(screenWidth,screenHeight):
    screen=turtle.Screen()
    screen.setup(width=screenWidth,height=screenHeight)
    return screen
# 
screenWidth=300
screenHeight=500
screen=setup_screen(screenWidth,screenHeight)

screen.mainloop()
