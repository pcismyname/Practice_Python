
first_class = [0] * 8
economy_class = [0] * 20


flag = int(input("press 1 to start : "))


while(flag == 1):
    print("------------------------KU Airline------------------------------------------")
    print("----------------------------------------------------------------------------")
    c = 1

    for i in first_class:

        if c == 1:
            print("A ", end="")
        elif c == 3:
            print("B ", end="")
        elif c == 5:
            print("C ", end="")
        elif c == 7:
             print("D ", end="")

        if c % 2 == 0:
            print(f"|{i}| ")
        else:
            print(f"|{i}| ", end="")
        c = c + 1
    print("----------------------------------------------------------------------------")

    row = input("Enter row(A-D): ")
    no = int(input("Input number(1-2): "))

    if(row == 'A'):
        if(no == 1):
            first_class[0] = 1
        else:
            first_class[1] = 1 
    
    if(row == 'B'):
        if(no == 1):
            first_class[2] = 1
        else:
            first_class[3] = 1
    
    if(row == 'C'):
        if(no == 1):
            first_class[4] = 1
        else:
            first_class[5] = 1
    
    if(row == 'D'):
        if(no == 1):
            first_class[6] = 1
        else:
            first_class[7] = 1

    print("------------------------KU Airline------------------------------------------")
    print("----------------------------------------------------------------------------")
    c = 1

    for i in first_class:

        if c == 1:
            print("A ", end="")
        elif c == 3:
            print("B ", end="")
        elif c == 5:
            print("C ", end="")
        elif c == 7:
             print("D ", end="")

        if c % 2 == 0:
            print(f"|{i}| ")
        else:
            print(f"|{i}| ", end="")
        c = c + 1
    print("----------------------------------------------------------------------------")


    if c == 1:
        print("A ", end="")
    elif c == 3:
        print("B ", end="")
    elif c == 5:
        print("C ", end="")
    elif c == 7:
        print("D ", end="")


    flag = int(input("continue press 1 / Exit press 0 : "))

print("Programe Exit!")
