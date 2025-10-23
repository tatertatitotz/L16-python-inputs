#must always import random
import random

computer = 1
if computer == 1:
    computer = "r"
    
player = input("rock (r), paper (p) or scissors (s)? Enter: ")

if player == computer:
    print("Tie!")
if player == "r" and computer == "p":
    print("Computer Wins!")