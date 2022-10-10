# List for 5 int values
numbers = []

# Get values for list
print("Enter 5 integer values:")
i = 0
for i in range(5):
    num = int(input())
    numbers.append(num)

# Sort list 
numbers.sort()

# Print sorted list
print("List:", numbers)

# Get new value to add to list 
print("Enter a value to add to list: ")
newNum = int(input())
numbers.append(newNum)

# Sort list again
numbers.sort()

# Print updated and sorted list
print("Updated list:", numbers)