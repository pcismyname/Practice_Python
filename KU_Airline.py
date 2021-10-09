import numpy as np

seat_f = np.zeros((5,2))
seat_b = np.zeros((5,5))
seat_e = np.zeros((5,10))

flag = int(input('Enter 1 to start programe : '))


while flag == 1 :
    print('First class \t\t Business class \t\t Economy class')
    #column
    for i in range (0,len(seat_f[0])):
        print(f'   {i+1} ',end = ' ')
    print('\t',end='')
    for i in range (0,len(seat_b[0])):
        print(f'  {i+1} ',end = ' ')
    print('    ',end='')
    for i in range (0,len(seat_e[0])):
        print(f' {i+1}  ',end = ' ')
    print()


    char = 65
    for i in range(0,len(seat_f)):

        print(chr(char),end = ' ')
        for j in range(0,len(seat_f[0])):

            print(f' |{int(seat_f[i][j])}| ',end = '')


        print("   ",end = '')
        print(chr(char),end = '')
        for j in range(0,len(seat_b[0])):

            print(f' |{int(seat_b[i][j])}| ',end = '')

        print("   ",end = '')
        print(chr(char),end = '')
        for j in range(0,len(seat_e[0])):

            print(f' |{int(seat_e[i][j])}| ',end = '')
        print()
        char+=1

    clss = input('First class enter F\nBusinees class enter B\nEconomy class enter E\nEnter class : ')
    row = input('Enter row(A-E): ')
    seat_no = int(input('Enter seat no. '))

    if clss == 'F':
        seat_f[ord(row)-65][seat_no-1] = 1
    elif clss == 'B':
        seat_b[ord(row)-65][seat_no-1] = 1
    else:
        seat_e[ord(row)-65][seat_no-1] = 1
    
    flag = int(input('Enter 1 to continue or other to exit : '))