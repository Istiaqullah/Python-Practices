# Creating a dictionary
Di = {
    "Bangladesh": "Dhaka",
    "India": "Delhi",
    "England": "London"
}

print("Original dictionary:", Di)


# 1. Accessing values
print("Capital of Bangladesh:", Di["Bangladesh"])
print("Using get():", Di.get("India"))


# 2. Adding and updating values
Di["Spain"] = "Madrid"       # add new
Di["Bangladesh"] = "Dhaka City"  # update
print("After adding/updating:", Di)


# 3. Removing items
Di.pop("England")   # removes by key
print("After pop('England'):", Di)

Di.popitem()        # removes last key-value
print("After popitem():", Di)


# 4. Check if key exists
print("Is 'India' present?", "India" in Di)


# 5. Looping through dictionary
print("Keys:")
for k in Di:
    print(k)

print("Values:")
for v in Di.values():
    print(v)

print("Key-Value pairs:")
for k, v in Di.items():
    print(k, ":", v)


# 6. Copying a dictionary
copy_dict = Di.copy()
print("Copied dictionary:", copy_dict)


# 7. Clearing dictionary
Di.clear()
print("After clear():", Di)
