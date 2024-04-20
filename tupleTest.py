# Testing Python Tuples
countryTuple = ("United States", "Canada", "France", "England", "Spain")
print(len(countryTuple))    # Get length of tuple
falseTuple = ("Germany")    # Needs at least one comma else it is just a string
print(type(falseTuple))
print(countryTuple[1])      # Get from index (same as lists)
print(countryTuple[-3:-1])  # Negative index
if "Canada" in countryTuple:    # Check for element
    print("Canada exists in the tuple")
# Tuples are unchangeable so changing a tuple to a list is a workaround
workList = list(countryTuple)
workList.append("Sweeden")
countryTuple = tuple(workList)
print(countryTuple)
# Unpacking a Tuple to variables
(red, orange, yellow, green, blue, indigo) = countryTuple
print(f"{red} {orange} {yellow} {green} {blue} {indigo} ")
(red, *orange, violet) = countryTuple   # Use asterisk when number of vars < number of items (put into list)
print(f"{red} {orange} {violet}")
# Join tuples
joinTuple = (1, 3, 5)
finalTuple = countryTuple + joinTuple   # Add tuples
print(finalTuple)
finalTuple = joinTuple * 2  # Duplicate tuple
print(finalTuple) 
# Tuple Methods
print(countryTuple.count("Spain"))   # Count instances in tuple
print(countryTuple.index("France"))  # Get index of instance
