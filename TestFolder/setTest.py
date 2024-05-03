# Testing Sets in Python (Unordered, Unchangeable, No duplicates)
fruitSet = {"Apple", "Cherry", "Banana", "Watermelon", "Dragon Fruit", "Cherry" } # Duplicates are ignored
print(fruitSet)
# Get length of set
print(len(fruitSet))
newSet = set(("Kiwi", "Pineapple", "Grape"))    # Set constructor can also be used to create a set
# Work with items in set
for x in fruitSet:  # Looping through set
    print(x)
print("Dragon Fruit" in fruitSet)   # Check if item exists in set
print("Blueberry" not in fruitSet)  # Opposite of above
# Add items
fruitSet.add("Blueberry")
print(fruitSet)
fruitSet.update(newSet)
print(fruitSet)     # Add set to another set but any iterable can be used
berryList = ["Strawberry, Blackberry"]
fruitSet.update(berryList) # Add List to set
print(fruitSet)
# Remove item
fruitSet.remove("Banana")   # Will raise error if item does not exist in set
print(fruitSet)
fruitSet.discard("Apple")   # Will not raise error if item doesn't exist in set
print(fruitSet)
remItem = fruitSet.pop()    # Discard random item
print(remItem)
#fruitSet.clear()    # Empty entire set
print(fruitSet)
#del fruitSet        # Delete set
print(fruitSet)     # Error on this line - set deleted
# Set interactions
veggieSet = {"Cucumber", "Tomato", "Carrot"}
#unionSet = fruitSet.union(veggieSet)    # Combine sets into one
unionSet = fruitSet | veggieSet         # Same as union just cleaner (Only works with sets)
print(f"UnionSet: {unionSet}")
nums = (1, 7, 8, 4, 2)
unionSet = fruitSet.union(nums)         # Union can be used on other structures
print(f"UnionSet after nums union: {unionSet}")
# Other interactions
carSet = {"Camaro", "Mustang", "Charger"}
carSet2 = {"Ferrari", "Buick", "Mustang", "Chevy"}
interSet = carSet.intersection(carSet2)     # Combine duplicates between sets into one set
print(interSet)     # Contains only Mustang
# interSet = carSet & carSet2   Does same as intersection but can only be done with two sets like union
carSet.intersection_update(carSet2)    # Keeps only duplicates but changes original set rather than returning a set
print(carSet)
# Difference
partSet = {"GPU", "CPU", "RAM", "Motherboard"}
partSet2 = {"PSU", "Fan", "GPU", "SSD"}
diffSet = partSet.difference(partSet2)  # Returns a set that contains only original items from both sets
print(diffSet)
#diffSet = partSet - partSet2    # Same as difference but only with sets
partSet.difference_update(partSet2) # Keep only original items in original set (remove duplicates)
print(partSet)
symDiff = partSet.symmetric_difference(partSet2)    # Stores all items that are not duplicates in a new set
print(symDiff)
#symDiff = partSet ^ partSet2 - Shorthand, only works on sets
partSet.symmetric_difference_update(partSet2)   # Keeps all items that are NOT duplicates in original set
print(partSet)