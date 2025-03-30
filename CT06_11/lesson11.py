# print("Hello from lesson 11")
# number=int(input("What number do you want to check?"))
# if number % 3 ==0 and number % 7 ==0:
#     print("The number is divisible by 3 and 7!")
# else:
#     print("The number is not divisible by 3 and 7!")

# age=int(input("What is your age?"))
# if age<12 or age>65:
#     print("Ticket price: $15")
# else:
#     print("Ticket price: $20")

# colour=str(input("What colour do you want to check?"))
# if not colour == "green":
#     print("Try again.")
# else:
#     print("Correct!")

day=str(input("What day of the week is it?"))
if not day=="Saturday":
    print("It's not the weekend yet!")
else:
    print("It's finally the weekend!")

# There is an order of precedance for Logical AND, OR, NOT.
#     not----> and ----> or

burger=input("Do you want a burger?")
fries=input("Do you want fries?")
drink=input("Do you want a drink?")

burger = burger == "yes"
fries =