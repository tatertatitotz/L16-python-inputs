import random

number = 4
char = "abcdefghijklmnopqrstuvwxyz"
currentLength = 0

length = 4

#password must be defined as a string before adding characters
password = ""
#if the currentLength is shorter than the given length, it repeasts

for password in range(number):
    password = ""
    for count in range(length):
        password += random.choice(char)
    print(password)




