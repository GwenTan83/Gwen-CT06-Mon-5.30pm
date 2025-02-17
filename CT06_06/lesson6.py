# print("Hello from lesson 6")

sumScore=0
numStud=int(input("How many students do you have?"))
for i in range(numStud):
    score=int(input("How much did this student score?"))
    sumScore=sumScore + score

print(sumScore/numStud)


