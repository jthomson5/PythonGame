# Testing Python Dictionaries (Ordered in Python 3.7, unordered in lower versions)
carDict = {     # Initialize Dictionary, can also use dict() constructor
    "brand": "Dodge",
    "model": "Challenger",
    "year": 2024,
    "colors": ["Red", "Black", "White"]     # Data can be of any type
    
}
print(carDict)
print(carDict["colors"])     # Print specific value based on key
print(len(carDict))     # Print length of dictionary
brand = carDict["brand"]    # Store value in var
print(f"Brand of car: {brand}")
# Dictionary methods
model = carDict.get("model")    # Get method does same thing as above
print(f"Model of car: {model}")
keys = carDict.keys()           # Get all keys in dictionary, stored in list
print(f"Keys of carDict: {keys}")
carDict["Price"] = 33000        # Add new pair
print(carDict["Price"])
valList = carDict.values()      # Get values of dict as list
print(f"Values of dict: {valList}")
items = carDict.items()         # Get all data from dict as list of tuples
print(f" All items: {items}")
carDict.update({"Mode": "AWD"}) # Can also add items using the update method
print(carDict.items())
carDict.pop("Mode")             # Remove item with key name
print(carDict.keys())
carDict.popitem()               # Remove last added item
print(carDict)                  
del carDict["colors"]           # Does same as above
print(carDict)
#del carDict                    # Deletes entire dictionary
#print(carDict)                 # Error as carDict no longer exists
#carDict.clear()                # Clear entire dictionary
#print(carDict)                 # Empty
# Check if key exists in dictionary
if "brand" in carDict:
    print("Yes, brand is a key in the dictionary")
# Looping through dictionaries
for x in carDict:       # Print all key names
    print(x)
for x in carDict:       # Print all values
    print(carDict[x])   
for x in carDict.values():      # Another way to do the above
    print(x)
for x in carDict.keys():        # Another way to print key names
    print(x)           
for x, y in carDict.items():
    print(x, y)                 # Print whole tuple
# Copy dictionary to another variable
copyVar = carDict.copy()        # Can also be done with dict function copyVar = dict(carDict)
print(copyVar)
# Nested Dictionaries
student1 = {
    "name": "Jackson",
    "GPA": 3.6
}
student2 = {
    "name": "Ryan",
    "GPA": 3.8
}
student3 = {
    "name": "Lisa",
    "GPA": 3.8
}
schoolDict = {
    "student1" : student1,
    "student2" : student2,
    "student3" : student3
}
print(schoolDict["student2"]["name"])       # Print element from nested dictionary
# Loop through nested dictionary
for x, obj in schoolDict.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])