w = input("Enter one or more words of equal length: ")
ori = w.split( )
print(f"Input list:\n{ori}")

tl = []
n = len(ori)
m = len(ori[0])
for j in range(0,m):
  a = ""
  #a = []
  for i in range(0,n):
      a += ori[i][j]
      #d a.append[i][j] 
  tl.append(a)

print(f"Output list:\n{tl}")