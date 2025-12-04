# Creating a tuple (first method)
numbers = (5, 2, 9, 1, 5)

print("Original Tuple:", numbers)

# Count how many times a value appears
print("Count of 5:", numbers.count(5))

# Find the index of a value
print("Index of 9:", numbers.index(9))

# 3. Accessing elements
print("First element:", numbers[0])

# 4. Slicing
print("Slice (1 to 3):", numbers[1:4])

# 5. Length of tuple
print("Length:", len(numbers))

# 6. Checking membership
print("Is 9 in tuple?", 9 in numbers)

# 7. Looping through tuple
print("Looping:")
for n in numbers:
    print(n)

# 8. Converting tuple to list
temp_list = list(numbers)
temp_list.append(100)
numbers_modified = tuple(temp_list)
print("After conversion & modification:", numbers_modified)
