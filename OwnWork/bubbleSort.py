numbers = [8, 2, 5, 3, 1, 7, 4, 6]
sorted = [1, 2, 3, 4, 5, 6, 7, 8]
temp = 0

while numbers != sorted:
    for count in range(0, len(numbers)-1):
        
        if numbers[count] > numbers[count+1]:
            temp = numbers[count+1]
            numbers[count + 1] = numbers[count]
            numbers[count] = temp

print(numbers)