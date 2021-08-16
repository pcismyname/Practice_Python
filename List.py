list = [10,2,3,4,5,60,7,-100,0,10]
result = []
i = 0
"""while i<10:
    num = int(input())
    list.append(num)
    if list[i] < 5:
        result.append(num)
    i = i+1  """
    
print([i for i in list if i < 5])



#print(list)
#print(result)