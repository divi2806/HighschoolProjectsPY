#lottery system in python using random
import random
print("Welcome to ABC Lottery game")
a = int(input("Enter your ticket number that you have been alloted"))
b = random.randint(1,600)
if a == b:
    print("Congratulations you are our lucky winner you get Iphone 100 Pro ultra double max x")
else:
    print("Better luck next time")