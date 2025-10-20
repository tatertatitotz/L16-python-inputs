#ALWAYS import random when implementing it.
import random
# 1. Generate two random single-digit integers (0–9)
number1 = random.randint(0, 9)
#random is a module
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
   #storing number1 as temp
   temp = number1
   #number1 is now number2
   number1 = number2
   #number2 is now temp, which was number1
   number2 = temp
   #successful swap!

# 3. Prompt the student to answer "What is number1 - number2?"
answer = int(input(f"What is {number1} - {number2}? "))
#type in your answer

# 4. Grade the answer and display the result
if number1 - number2 == answer:
   #lets you know your answer is correct
   print("You are correct!")
else:
   #lets you know your answer is wrong
   print("Your answer is wrong.")
   #gives the correct answer to the problem
   print(f"{number1} - {number2} should be {number1 - number2}.")