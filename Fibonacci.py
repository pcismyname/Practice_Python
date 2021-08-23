def fibo(n):
    list = []

    if n == 1:
        list.append(1)
        return list
    if n == 2:
        list.append(1)
        list.append(1)
        return list
    list = [1,1]
    for i in range(2,n+1):
        list.append(list[i-1]+list[i-2])
    
    return list

"""def fibo_recur(n):
    if n==1:
        return 1
    else :
        return (fibo(n-1)+fibo(n-2))"""

print(fibo(9))


"""for i in range(10):
    print(fibo_recur(i)) """

