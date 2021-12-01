import random

def question():
    all_num = random.randint(2, 5)
    num_list = []
    sum = 0

    for i in range(all_num):
        num = random.randint(1,10)
        num_list.append(str(num))
        sum += num
    equation =  ' + '.join(num_list)
    print(f'{equation} = ',end = '')
    ans = int(input())
    if ans != sum:
        print(f'Wrong! The answer was {sum}')
        return False
    else:
        return True

def play():
    wrong = 0
    score = 0
    while wrong != 3: 
        check = question()
        if check == False:
            wrong += 1
        if check == True:
            score += 1
    print(f'You earned {score} total points')        
    
play()
        


    

        