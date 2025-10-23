#must always import random
import random
#where randit will go
chosen = random.randint(1, 3)

if chosen == 1:
    computer = "r"
if chosen == 2:
    computer = "p"
if chosen == 3:
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
if player == "s" and computer == "r":
    print("Computer Wins!")
if player == "s" and computer == "p":
    print("You Win!")