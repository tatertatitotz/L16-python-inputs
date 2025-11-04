import random

number = 4
char = "abcdefghijklmnopqrstuvwxyz"
currentLength = 0
currentNumber = 0
length = 4

#password must be defined as a string before adding characters
password = ""
#if the currentLength is shorter than the given length, it repeasts

for password in range(number):
    password = ""
    #this doesn't work because the while loop ends after the first password is created
    while length > currentLength:
        password += random.choice(char)
        currentLength += 1
    print(password)




