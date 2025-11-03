#variables declared
name = input("Enter Name: ")
hobby = input("Enter hobby: ")
#yearOfBirth can only accept a whole number because of the int()
yearOfBirth = int(input("Enter year of birth: "))

#Comma between each string and variable when not writing in f-string.
print(f"Hello {name}. I know you like {hobby} and are born in the year {yearOfBirth}.")
 
currentYear = int(input("Enter the current year: "))
#Subtracting the variables in order to get the age of the person.
age = (currentYear - yearOfBirth)
print(f"{name}, you are {age} years old.")