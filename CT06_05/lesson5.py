# print("Hello from lesson 5")
# yourname=input("what is his/her name?")
# yourage=input("how old is him/her?")
# yourage=int(10)
# yourmessage=input("What is the message for him/her?")
# print("Happy" + str(yourage) + "th Birthday" + yourname + "!" + yourmessage)


# for count in range(100):
#     print("I will not sling mud at my friend ever!")
#     print("Teacher!")
     

# for abc in "I will not sling mud at my friend ever!":
#     print(abc)


# yourname=input("What is your name?")
# for abc in yourname:
#     print("give me a " + abc)
# print("What do we have?")
# print("Dave is the best!")

# for count in range(100):
#     print("I like chicken rice.")

# for count in range(100):
#     print("I like cake.")
#     print("Give me more")
##Task 4
# for number in range(1,6):
#     print(number)
# for number in range(51,101):
#     print(number)
# for number in range(18,30):
#     print(number)
##Task 5
# for number in range(2,5,2):
#     print(number)


# ## Task 6: range(start, stop, step)

# **Task 6a**:
# Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.
# for number in range(2,25,2):
#      print (number)

# **Task 6b**:
# Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.
# for number in range (8,97,8):
#      print(number)
# **Task 6c**:
# Use a 'for' loop to print numbers from 5 to 1 in descending order.
# for number in range (5,0,-1):
#     print(number)
## Task 7: Countdown timer

# **Task 7a**:
# Imagine you are the race official and to start the race, you
# must say the following:

#     Ready!
#     3
#     2
#     1

# Using a 'for' loop, recreate the above sequence.
# print("Ready!")
# for number in range(3,0,-1):
#     print(number)
# **Task 7b**:
# Create a countdown timer that counts from 10 to 1.
# When the timer hits 1, print "Boo!"
# for number in range(10,0,-1):
#     print(number)
# print("Boo!")
## Task 8: User-Defined Range Counter

# Using input(), ask the user for 2 numbers and store them in the
# variables:
# 1. start
# 2. stop

# Write a 'for' loop to count from **start** to **stop**
# start = int(input("What is the starting number? "))
# stop = int(input("What is the stopping number? "))
# for i in range(start, stop + 1):
#     print(i)

## Task 9: Accumulative Sum in Loop
# Note:
# What happens if the user inputs a higher start number than stop?
# Modify your code to be able to handle that scenario.
## Task 9: Accumulative Sum in Loop

# 1. Create a variable 'num' and assign the integer "0" to it
# 2. Create a 'for' loop that repeats 10 times
# 3. Add the sum of 'num' and the loop's parameter and print out
#    the value.
# 4. Observe what happens.

# Example:
# 1st iteration
#     num = num + i
#     print(num)

# 2nd iteration
#     num = num + i
#     print(num)

# ...

# 10th iteration
#     num = num + i
#     print(num)

# Output:
#     0
#     1
#     3
#     6
#     10
#     15
#     21
#     28
#     36
#     45
x=0 
sum=0
for num in range (10):
    sum=sum+x
    x=x+1
print(sum)
 