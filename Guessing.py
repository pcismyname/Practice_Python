import random

a = random.randint(0,9)
print("Guessing Game")


while(1):
    num = int(input("Input number 0 - 9 : "))
    if(num>a):
        print("Too high!")
    elif(num<a):
        print("Too Low!")
    else:
        print("You Win")
        break
