def leap_1 (start,end):
    leap_year = []
    for i in range(start,end+1):
        i-= 543
        if i%400 == 0 or(i%4==0 and i%100!=0):
            leap_year.append(i+543)
    return leap_year    

def leap (start,end):
    leap_year = [str(i) for i in range(start,end+1) if (i-543)%400 == 0 or((i-543)%4==0 and (i-543)%100 != 0) ]
    return leap_year



start = int(input('Begin Year: '))
end = int(input("End Year: "))

leap_year = leap(start,end)
print('Leap years from ' + str(start)+ ' to '+str(end)+ ': ', end = '')
if len(leap_year) != 0:
    print(', '.join(leap_year))
else:
    print('None')
