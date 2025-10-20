import random 
#define die values
die = random.randint(0, 6)
die2 = random.randint(0, 6)
#define total
total = die + die2

#Display for dice values just to see if its working with random
print(f"You rolled {die}")
print(f"You rolled {die2}")
#If the dice total is 7 OR 11 then you win.
if total == 7 or total == 11:
    print("You win!")
#dice have the same number
elif die == die2:
    #This is a nested
    if die == 6:
        print("Jackpot! You win!")
    else:
        print("Doubles! You win!")
#Indicates loss! Important, nothing shows up if you lose otherwise!
else:
    print("You lose")

    