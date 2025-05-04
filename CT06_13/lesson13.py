# print("Hello from lesson 13")
# groceries=[
# "Apples",
# "Bread",
# "Carrots",
# "Dates",
# "Eggs",
# "Flour",
# "Grapes",
# "Honey"]
# groceries[7]="Herbs"
# print (groceries)
# groceries.append("Ice")
# groceries.insert(1,"Bananas")
# del(groceries[2])
# print(groceries)
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
        print("Grapes, get the FarmFresh brand.")

# Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."

# list=[]
# while True:
#     user=input("What would you like to add to the store?")
#     if user=="end":
#         break
#     else:
#         list.append(user)
# print(list)
# Thing=input("What are you looking for?")
# if Thing in list:
#     print("Yes, we sell that.")
# else:
#     print("Sorry, we don't have that.")