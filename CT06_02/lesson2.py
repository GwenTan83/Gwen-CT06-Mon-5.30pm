print("Hello from lesson 2")

######## Write the pseudocode in comments for task 2 here
# Using comments, translate the code shown on screen into pseudocode.

######## Write the pseudocode in comments for task 3 here
# Using comments, translate the code shown on screen into pseudocode.
#repeat 10 times:
#say "Hey!"
#move 10 steps
#assign 0 to "counter"
#while "counter" is not 50:
#move 10 steps
#turn 15 degrees
#increase "counter" by 10
#ask the user for their age and assign to "answer"
#if answer is less than 18,
#say "Access Denied!"
#otherwise,
#say "Welcome!"
#look at the material of the item
#if the item's material is plastic 
#put into the plastic bin
#save the secret phrase as "let me pass"
#ask the user for the secret phrase
#if reply not equal to "let me pass"
#say error message
#save the error message as "access denied"
#otherwise say "congratualations"
#get the student's test1 score
#get the student's test2 score
#get the student's test3 score
#take 20% of test1
#take 40% of test2
#take 40% of test3
#add up the 3 numbers, and print the final score
test1 = input(99)
test1 = int(test1) # conversion function
test2 = input(98)
test2 = int(test2) # conversion function
test3 = input(95)
test3 = int(test3) # conversation function
test4 = input(96)
test4 = int(test4) # conversion function
test1 = 0.25 * test1 # 25%
test2 = 0.25 * test2
test3 = 0.25 * test3
test4 = 0.25 * test4

final = test1 + test2 + test3 + test4

print("your final score is", final)