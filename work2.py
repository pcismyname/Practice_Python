# นายชิษณุพงศ์ เพ็งชัย - 6410742040

second = float(input("Enter seconds : "))

hour = second//3600
minute = (second-hour*3600)//60
second = (second-hour*3600-minute*60)

print(f"{hour} hour")
print(f"{minute} minute")
print(f"{second} second")
