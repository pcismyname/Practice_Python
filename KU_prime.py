import sys

def check_prime(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num <= 0:
        return 0

    for i in range(2,num):
        if(num%i == 0):
            return 0

    return 1



begin = int(input("Primes greater than? "))
num = int(input("How many primes? "))
begin += 1
temp = begin
count = 0


if num == 0:
    print("Nothing to do.")
    sys.exit(0)


while count < num:
    if check_prime(temp) == 1:
        count += 1
    temp +=1

print(f"{count} primes greater than {begin-1} are")

count = 0
while count < num:

    if check_prime(begin) == 1:
        print(f'{begin:>6}',end = "")
        count += 1
        if count % 10 == 0:
                print()
    
    begin +=1

    

