# นายชิษณุพงศ์ เพ็งชัย - 6410742040

num1 = int(input("Enter integer #1: "))
num2 = int(input("Enter integer #2: "))
num3 = int(input("Enter integer #3: "))


if num1>num2:
    max = num1
else:
    max = num2

if max<num3:
    max = num3

print(f"The maximum number is {max}")

