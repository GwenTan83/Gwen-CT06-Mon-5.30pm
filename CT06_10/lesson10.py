# print("Hello from lesson 10")
# num = int(input("What number do you want to check?"))
# if num>0:
#     print(str(num) + "number is positive")
# else:
#     print(str(num) + "number is negative")

# num = int(input("What number do you want to check?"))
# ans = num % 2
# if ans==0:
#     print("This number is even.")
# else:
#     print("This number is odd.")

# age = int(input("What is your age?"))
# if age<13:
#     print("You are a child.")
# else:
#     if age<19:
#         print("You are a teen.")
#     else:
#         print("You are an adult.")

score = int(input("What is your score?"))

if score < 60:
    print("F")
elif score <= 69:
    print("D")
elif score <= 79:
    print("C")
elif score <= 89:
    print("B")
elif score <= 100:
    print("A")