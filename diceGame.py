#import random last
#define die values
die = 6
die2 = 6
#define total
total = die + die2

#If the dice total is 7 OR 11 then you win.
if total == 7 or total == 11:
    print("You win!")
#dice have the same number
elif die == die2:
    print("Doubles! You win!")
#Indicates loss! Important, nothing shows up if you lose otherwise!
else:
    print("You lose")

    