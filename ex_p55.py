# นายชิษณุพงศ์ เพ็งชัย - 6410742040

quantity = int(input("Enter quantity of packages: "))

total_price = quantity * 99

if quantity >= 100:
    discount = 0.4

elif quantity >= 50:
    discount = 0.3

elif quantity >= 20:
    discount = 0.2

elif quantity >= 10:
    discount = 0.1

else:
    discount = 0  


total_price = total_price - total_price*discount

print(f"the discount is {discount*100}%")
print(f"you pay {total_price}")