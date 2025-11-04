import random

#allows the user to give a number of passwords and the length
number = int(input("How many passwords? "))
length = int(input("How long are they? "))
#allows random.choice to pick from this pool of characters
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[]\;'./~!@#$%^&*()_+|<>?"

#for loop for the number of passwords that will be printed
for password in range(number):
    #assigns password as a blank string
    password = ""
    #sets the limit for the number of characters in a password
    for count in range(length):
        #adds a random character to each password
        password += random.choice(char)
    #prints the given number of passwords
    print(password)




