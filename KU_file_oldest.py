text=input("Enter age file: ")
txt=open(text).read().splitlines()
line = [x for x in txt if x != ""]

name = []
age = []

for i in range(0,len(line)):
  data = line[i].split(',')
  for j in range(0,len(data)):
      if j==0:
        name.append(data[j])
      elif(i==0 and j==1):
          max = int(data[j])
          age.append(int(data[j]))
      else:
          age.append(int(data[j]))
          if age[i]>max:
              max = age[i]
          
print(f'Oldest person(s) with the age of {max}:')
for i in range(0,len(line)):
    if(max == age[i]):
        print(f'- {name[i]}')