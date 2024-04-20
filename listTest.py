# Testing Python Lists
pokeList = ["Pikachu", "Charizard", "Umbreon", "Rayquaza", "Squirtle"]
print(pokeList)
str = pokeList[1];
print(str)
print(pokeList[1:3])    # List indexing (Also allows negative indexing)
if "Charizard" in pokeList:     # Check if item exists in list
    print("Charizard is in the pokeList")

# Changing List Items
pokeList[2] = "Mewtwo"      # Change items from index
pokeList[3:] = ["Groudon", "Eevee"]
pokeList[1:3] = ["Charmeleon"]
print(pokeList)

# List methods
pokeList.insert(2, "Vaporeon")  # Insert item at index
print(pokeList)
pokeList.append("Blastoise")    # Add item to end of list
print(pokeList)
carList = ["Ford", "Kia", "Honda", "Lamborghini", "Ferrari"]
pokeList.extend(carList)    # Add elements to list from another list
print(pokeList)
pokeList.remove("Kia")  # Remove element
print(pokeList)
pokeList.pop(3)     # Remove index from list
print(pokeList) 
#pokeList.clear()   # Clear list contents
#print(pokeList) 

# Looping through lists
for i in range(len(pokeList)):  # Loop through index numbers
   print(pokeList[i])
print("")
i = 0
while i < len(pokeList):        # While loop version
    print(pokeList[i])
    i += 1
print("")
[print(x) for x in pokeList]    # Shorthand for loop (comprehension)
print("")
emptyList = [x for x in pokeList if "a" in x]   # One line initialization
print(emptyList)
print("")
newList = [x for x in range(10)]    # One line initialization
print(newList)
newlist = [x if x != "Blastoise" else "Ferrari" for x in pokeList]
print(pokeList)
# List sorting
pokeList.sort()     # General sorting
print(pokeList)
pokeList.sort(reverse=True)     # Sort descending
print(pokeList)
