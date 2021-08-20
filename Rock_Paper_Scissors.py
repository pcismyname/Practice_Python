print("Rock Paper Scissors Game")
print("Press 1 to start")
print("Press 0 to exit")
n = int(input())
if(n == 1):
    while(1):
        print("Rock == 1")
        print("Paper == 2")
        print("Scissors == 3")
        p1 = int(input("player 1: "))
        p2 = int(input("player 2: "))
        if(p1 == 1):
            if(p2 == 1):
                print("draw")
            elif(p2 == 2):
                print("player 2 win!")
            else:
                print("player 1 win!")
        elif(p1 == 2):
            if(p2 == 1):
                print("player 2 win!")
            elif(p2 == 2):
                print("draw!")
            else:
                print("player 1 win!")
        else:
            if(p2 == 2):
                print("player 1 win!")
            elif(p2 == 2):
                print("player 2 win!")
            else:
                print("draw!")

        print("continue press 1 ||| exit press 2")
        c = int(input())
        if(c==2):
            break
        
print("Exit Game!")