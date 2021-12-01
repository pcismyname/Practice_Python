#str1 = str(input(s))
def encode(word):
    result = ''
    for char in word:
        char = str(ord(char))
        if int(char) >= 0 and int(char) <= 9:
            result += '00' + char
        elif int(char) >=10 and  int(char) <= 99:
            result+= '0' + char
        else:
            result += char
    return result

print(encode("Cat"))
print(encode('101'))
print(encode('Dog'))
 