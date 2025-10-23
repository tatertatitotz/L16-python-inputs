#must always import random
import random
#where randit will go
computer = 3

if computer == 1:
    computer = "r"
if computer == 2:
    computer = "p"
if computer == 3:
    computer = "s"

player = input("rock (r), paper (p) or scissors (s)? Enter: ")

print(f"{player} vs. {computer}")

if player == computer:
    print("Tie!")
if player == "r" and computer == "p":
    print("Computer Wins!")
if player == "r" and computer == "s":
    print("You Win!")
if player == "p" and computer == "r":
    print("You Win!")
if player == "p" and computer == "s":
    print("Computer Wins!")