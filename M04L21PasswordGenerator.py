import random

char = 'abcdefghijklmnopqrstuvwxyz'
currentLength = 0

length = 4

password = ""

while length > currentLength:
    currentLength += 1
    character = random.choice(char)
    password += character
print (currentLength)

print(password)
