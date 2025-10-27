number=int(input("Enter number you want multiplied: "))
for mult in (0, 11):
    #this is going to break because you're multiplying an int by a set of numbers
    total = number * mult
    print(f"{number} x {mult} = {total}")