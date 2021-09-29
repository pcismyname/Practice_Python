num_student = int(input('Enter number of students : '))
max_point = int(input('Enter maximum point : '))

totol_score = 0
pass_65 = 0
num_s = num_student

while num_student:

    point = int(input('Point : '))

    if num_s == num_student:
        high = point
        low = point

    if point>high:
        high = point
    else:
        low= point


    if point > 0.65*max_point:
        pass_65+=1

    if point < 0.5*max_point:
        
        temp_total = point
        cnt = 1
        revise_point = point
        while revise_point<0.5*max_point:
            revise_point = int(input('Revise point : '))
            temp_total += revise_point
            cnt+=1
        
        point = temp_total/cnt

    totol_score += point
    num_student-=1

print(f'Average {totol_score/num_s:.4f}')
print(f'Highest point : {high}')
print(f'Lowest point : {low}')
print(f'Number of student pass over 65% : {pass_65}')


