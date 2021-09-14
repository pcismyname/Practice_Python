def modify(string):
  
  new = ''
  for c in string:
    if c != ' ':
      new=new+c
    if c==" ":
      new=new+"$"
  return new


s = input('Enter something (or <ENTER> to quit): ')
while  s!='':
    print(modify(s))
    s = input('Enter something (or <ENTER> to quit): ')