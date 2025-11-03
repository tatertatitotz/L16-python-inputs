# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

#missing end quote 
print("Welcome to the Debugging Lab!")

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")

#"88" is not an int, it is a string
scores = [85, 90, 78, 88, 92]

total = 0
#no end : at the end of the condition
for score in scores:
    total = total + score

average = total / len(scores)
#syntax error, no , before average
print("Your average score is: ", average)

highest = 0
for s in scores:
    if s > highest:
        highest = s
#highest is an int, not a string
print("Your highest score was:" + str(highest))