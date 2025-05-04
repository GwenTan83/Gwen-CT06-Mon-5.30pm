# Task 1
# Print numbers from 10 to 200 using the while loop
# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here
number=0
while True:
    number=number+10
    print(number)
    if number==200:
        break



planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
print(planets[2])

planets.append("neptune")
print(planets)

print(planets[3])

planets[3]="muskworld"

print(planets)

del(planets[6])
print(planets)

planet=planets
for planets in planet:
    print(planets)
   
