text=input("Enter grade file: ")
txt=open(text).read().splitlines()
line = [x for x in txt if x != ""]
subject = []
credit = []
grade = []
point = []

for i in line:
  data = i.split(',')
  for j in range(0,len(data)):
    if j==0:
        subject.append(data[j])
    elif j==1:
        credit.append(int(data[j]))
    else:
        grade.append(data[j])
        if data[j] == 'A':
            point.append(4.0)
        elif data[j] == 'B+':
            point.append(3.5)
        elif data[j] == 'B':
            point.append(3.0)
        elif data[j] == 'C+':
            point.append(2.5)
        elif data[j] == 'C':
            point.append(2.0)
        elif data[j] == 'D+':
            point.append(1.5)
        else:
            point.append(1.0)
        


sum_credit = 0
sum_point_weight = 0
for i in range(0,len(line)):
    print(f'subject: {subject[i]} credit: {credit[i]} grade: {grade[i]:2} point: {point[i]}')
    sum_credit+=credit[i]
    sum_point_weight+=credit[i]*point[i]

print(f'Total credits = {sum_credit}')
print(f'GPA = {sum_point_weight/sum_credit:.2f}')
       
