# Get values for list
values = input("Enter 5 integer values: ") 

# Add values to list
numbers = values.split()
for i in range(5):
    numbers[i] = int(numbers[i])

# Print original list
print("Original list:", numbers)

# New sorted1 list
sorted1 = []

# Sort list 
for i in range(5):
    index = numbers.index(min(numbers))
    pop = numbers.pop(index)
    sorted1.append(pop)

# Print sorted list
print("Sorted list:", sorted1)

# New sorted2 list
sorted2 = []

# Get value to add to list
newNum = int(input("Enter a value to add to the list: "))
sorted1.append(newNum)

# Sort list again
for i in range(6):
    index = sorted1.index(min(sorted1))
    pop = sorted1.pop(index)
    sorted2.append(pop)

# Print updated list
print("Updated sorted list:", sorted2)