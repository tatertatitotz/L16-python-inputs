numbers = [8, 2, 5, 3, 1, 7, 4, 6]
highest = 0
temp = 0
while range[]
    for count in range(numbers.len()):
    
        if numbers[count] > numbers[count+1]:
            numbers[count + 1] = temp
            numbers[count + 1] = numbers[count]
            numbers[count] = temp

print(numbers)