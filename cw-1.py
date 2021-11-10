# นายชิษณุพงศ์ เพ็งชัย - 6410742040

num = []
num = input('Enter Some numbers: ').split()

sum = 0
for i in range(0,len(num)):
    sum += eval(num[i])
print(f'total : {sum}')