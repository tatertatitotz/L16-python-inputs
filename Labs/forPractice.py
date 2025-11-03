#the user inputs only whole numbers
number = int(input("Enter number you want multiplied: "))
#mult will have a value within the range of (1, 11)
#mult will be assigned a new value each loop, which is its previous +1
#mult will end when 11 values have been presented.
for mult in range(1, 11):
    #calculating the total based on the number given, and the set multiplied values
    total = number * mult
    #displays the multiplication and the answer
    print(f"{number} x {mult} = {total}")