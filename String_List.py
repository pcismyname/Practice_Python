word = input("Input your word : ")

rvs = word[::-1]

if word == rvs:
    print(word + " is palindrome")
else :
    print(word + " is not palindrome")
    #cheat