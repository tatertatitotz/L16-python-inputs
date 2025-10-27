#the starting number for range will always be 0. 
#range(5) means 5 numbers total will be printed, when the variable is printed.
for count in range(5):
    #prints out 5 numbers total including count's value
    print(count)
    #count starts at 0
    #count variable increments of 1
    #count stops at 4
#nothing happens if n is value -5 range only accepts positive integars
#count in range(n) n equals the number of values shown when adding 1 to count

for count in range(2, 6):  
    print(count)
    #calculating the range is the difference between value1 and value 2.
    #It only prints 4 counts, starting at 2.
#when -2 is placed, the count starts at -2
#value1 = inital value
#value2 = ending

for count in range(0, 10, 2):  
    print(count)
#counts to 8 using 2s.
#n - z, z being the 3rd digit in the range
#the count will try to get as close to 10 as possible.
#value1 = start
#value2 = asymptote
#value3 = increase by