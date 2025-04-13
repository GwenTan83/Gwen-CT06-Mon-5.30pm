# print("Hello from lesson 13")
groceries=[
"Apples",
"Bread",
"Carrots",
"Dates",
"Eggs",
"Flour",
"Grapes",
"Honey"]
groceries[7]="Herbs"
print (groceries)
groceries.append("Ice")
groceries.insert(1,"Bananas")
del(groceries[2])
print(groceries)
# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
# 3. If grocery == "Carrots", print "<grocery name>: I need 3 of
#    these"
# 4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
#    brand"
for grocery in groceries:
    if grocery=="Apples":
        print("Apples, I need 5 of these.")
    elif grocery=="Carrots":
        print("Carrots, I need 3 of these.")
    else:
        grocery=="Grapes":
        print("Grapes, get the FarmFresh brand.")