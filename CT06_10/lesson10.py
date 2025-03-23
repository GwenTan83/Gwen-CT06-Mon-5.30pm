# print("Hello from lesson 10")
num = input(int("What number do you want to check?"))
if num>0:
    print(str(num) + "number is positive")
else:
    print(str(num) + "number is negative")

num = input(int("What number do you want to check?"))
ans = num % 2
if ans==0:
    print(str(num) + "This number is even.")
else:
    print(str(num) + "This number is odd.")