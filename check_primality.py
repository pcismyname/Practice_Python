def isPrime(num):
    c=0
    if num == 2:
        return 1
    if num == 1:
        return 0
    for i in range(3,num):
        if(num % i == 0):
            return 0
    return 1


num = int(input("Input number : "))
if isPrime(num):
    print(f"{num} is Prime number")
else:
     print(f"{num} is not Prime number")
