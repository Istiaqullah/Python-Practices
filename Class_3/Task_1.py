import random

# Part A: List and Tuple Operations
# A.1. Create a list of 10 random integers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print("Random List:", random_list)

# A.2. Sort the list in ascending and descending order, remove duplicates, find min, max, and average
random_list_sorted_asc = sorted(random_list)
random_list_sorted_desc = sorted(random_list, reverse=True)
unique_list = list(set(random_list))
max_value = max(random_list)
min_value = min(random_list)
average = sum(random_list) / len(random_list)

print("Sorted (Asc):", random_list_sorted_asc)
print("Sorted (Desc):", random_list_sorted_desc)
print("Unique List:", unique_list)
print("Max Value:", max_value)
print("Min Value:", min_value)
print("Average:", average)


# Part B: Set Operations
# B.1. Create two sets
set_A = set(range(1, 11))  # Set A: 1 to 10
set_B = set(range(5, 16, 2))  # Set B: Even numbers from 5 to 15
print("\nSet A:", set_A)
print("Set B:", set_B)

# B.2. Perform Set operations: Union, Intersection, Difference, Symmetric Difference
union_result = set_A | set_B
intersection_result = set_A & set_B
difference_A_B = set_A - set_B
difference_B_A = set_B - set_A
symmetric_diff = set_A ^ set_B

print("Union of A and B:", union_result)
print("Intersection of A and B:", intersection_result)
print("Difference A - B:", difference_A_B)
print("Difference B - A:", difference_B_A)
print("Symmetric Difference:", symmetric_diff)


# Part C: Dictionary Manipulation
# C.1. Create a dictionary of students and their scores
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print("\nInitial Students Dictionary:", students)

# C.2. Add a new student, update Alice's score, remove Charlie, calculate average score, and print students with score > 85
students["David"] = 88
students["Alice"] = 90
del students["Charlie"]

average_score = sum(students.values()) / len(students)
students_above_85 = [name for name, score in students.items() if score > 85]

print("Updated Students Dictionary:", students)
print("Average Score:", average_score)
print("Students who scored above 85:", students_above_85)


# Part D: Applied Task - Inventory Management System
# D.1. Define inventory
inventory = {
    "apple": (50, 0.5),
    "banana": (100, 0.3),
    "orange": (75, 0.7)
}
print("\nInitial Inventory:", inventory)

# D.2. Functions for Inventory Management
# Add/Update product
def add_or_update_product(inventory, product, quantity, price):
    inventory[product] = (quantity, price)

# Remove product
def remove_product(inventory, product):
    if product in inventory:
        del inventory[product]

# Calculate total inventory value
def calculate_total_inventory_value(inventory):
    return sum(quantity * price for quantity, price in inventory.values())

# List products with low stock
def list_low_stock_products(inventory, threshold=50):
    return {product: (quantity, price) for product, (quantity, price) in inventory.items() if quantity < threshold}

# Example usage:
add_or_update_product(inventory, "grapes", 30, 1.2)  # Add new product
remove_product(inventory, "banana")  # Remove product
total_inventory_value = calculate_total_inventory_value(inventory)
low_stock_products = list_low_stock_products(inventory)

# Print inventory after changes
print("Inventory after changes:", inventory)
print("Total Inventory Value:", total_inventory_value)
print("Low Stock Products:", low_stock_products)
