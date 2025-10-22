#assigning enter
enter = input("Do you want to continue? Enter y or n: ")
#assigning loopCount
loopCount = 0
#when input response is y, it asks again.
#ALWAYS DEFINE enter == "y" and enter == "Y" SEPERATELY
while enter == "y" or enter == "Y":
    #adding one to loop count every time y is entered
    loopCount += 1
    #asks again for the input
    enter = input("Do you want to continue? Enter y or n: ")
#gives the total number of times the loop has occured
print(f"The loop ran {loopCount} times")