list1 = ['A','B']
list2 = [1,2]

list3 = []
for ch in list1:
    for num in list2:
        list3.append(ch+str(num))

print(list3)

list4 = [ch+str(num) for ch in list1 for num in list2 ]
print(list4)
