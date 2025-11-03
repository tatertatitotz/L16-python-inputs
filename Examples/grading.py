# Get user input for the grade
grade = float(input("Enter your grade: "))

# Determine the letter grade using multi-way if
if grade >= 90:
   letter_grade = "A"
# elif, is else if. So if it isn't >= 
# it moves down the line until it finds a grade that matches
elif grade >= 80:
   letter_grade = "B"
elif grade >= 70:
   letter_grade = "C"
elif grade >= 60:
   letter_grade = "D"
else:
   letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")