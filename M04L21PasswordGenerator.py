import random


char = 'abcdefghijklmnopqrstuvwxyz'
currentLength = 0

length = 4

#password must be defined as a string before adding characters
password = ""
#if the currentLength is shorter than the given length, it repeasts
while length > currentLength:
    character = random.choice(char)
    #adds a character to the password
    password += character
    #adds one to the current length with each character added
    currentLength += 1
print (currentLength)

for count in range(4):
    print(count)

