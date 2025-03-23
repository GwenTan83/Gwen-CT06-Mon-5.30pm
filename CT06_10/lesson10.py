# print("Hello from lesson 10")
# num = int(input("What number do you want to check?"))
# if num>0:
#     print(str(num) + "number is positive")
# else:
#     print(str(num) + "number is negative")

num = int(input("What number do you want to check?"))
ans = num % 2
if ans==0:
    print("This number is even.")
else:
    print("This number is odd.")

age = int(input("What is your age?"))
if age<13:
    print("You are a child.")
if age<19:
    print("You are a teen.")
else:
    print