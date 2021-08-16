#import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list = []

for i in a:
    if i in b:
       if i not in list:  #don't add duplicate num
           list.append(i)
print(list)

#c = range(1,random.randint(1,10))










