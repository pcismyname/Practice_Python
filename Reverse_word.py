def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])

sent = input("input your sentence :")
split_sent = sent.split(" ")

for i in range(len(split_sent)-1,-1,-1):
    print(split_sent[i], end = " ")

