import random


s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

len = 8
p = "".join(random.sample(s,len))

print(p)