#must always import random
import random
#play as much as you want!

#initial counts for each possible outcome
tieCount = 0
wins = 0
losses = 0

ask = input("Do you want to play? y or n: ")
#as long as the you respond with y or Y it will continue playing.
while ask == "y" or ask == "Y":
    #allows for the computer to pick a random number
    chosen = random.randint(1, 3)

    #if the random number is 1 computer plays rock
    if chosen == 1:
        computer = "r"
    #if the random number is 2 computer plays paper
    elif chosen == 2:
        computer = "p"
    #if the random number is 3 computer plays scissors
    #I chose to put an elif so I can more easily see the 3.
    elif chosen == 3:
        computer = "s"

    #asking for the player to choose from rock, paper or scissors.
    player = input("rock (r), paper (p) or scissors (s)? Enter: ")

    #display for what the computer chose and the player chose
    print(f"{player} vs. {computer}")

    #if player and computer are the same, it is a tie
    if player == computer:
        print("Tie!")
        #adds one to the tieCount variable each time this is the result
        tieCount += 1
    #if the player chooses rock and the computer chooses paper, you lose
    elif player == "r" and computer == "p":
        print("You Lost!")
        losses += 1
    #if the player chooses rock and the computer chooses scissors, you win
    elif player == "r" and computer == "s":
        print("You Win!")
        #adds one to the wins variable each time you win
        wins += 1
    #if the player chooses paper and the computer chooses rock, you win
    elif player == "p" and computer == "r":
        print("You Win!")
        wins += 1
    #if the player chooses paper and the computer chooses scissors, you lose
    elif player == "p" and computer == "s":
        print("You Lost!")
        #adds one to the losses variable each time you lose
        losses += 1
    #if the player chooses scissors and the computer chooses rock, you win
    elif player == "s" and computer == "r":
        print("You Lost!")
        losses += 1
    #if the player chooses scissors and the computer chooses paper, you win
    elif player == "s" and computer == "p":
        print("You Win!")
        wins += 1

    #play as much as you want!
    ask = input("Do you want to play again? y or n: ")
#after the loop ends, it provides you with your number of wins losses and ties.
print(f"Wins: {wins}!")
print(f"Losses: {losses} :(")
print(f"Ties: {tieCount}.")
        