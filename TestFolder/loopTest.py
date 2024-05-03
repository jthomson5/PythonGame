# Testing loops in Python
i = 0
n = 0
# While loops
while i < 10:
    print(i)
    if i == 4:
        print(f"i is equal to 4")
        break       # Stop loop
    i +=1
while n < 8:
    n += 1
    if n == 5:
        continue    # Skip to next iteration
    print(n)
else:               # else with while loop
    print("n is no longer less than 8")
# For loops
foodList = ["Chicken", "Beef", "Hamburger", "Hotdog", "Pasta"]
for x in foodList:
    if x == "Beef":
        continue        # Skip to next iteration
    elif x == "Pasta":
        break           # Break from loop
    print(x)
for x in "Helicopter":  # Loop through string
    print(x)
for x in range(8):      # Loop through number 0-7 
    print(x)
for x in range(1,8):    # Range with start index  
    print(x)
for x in range(1, 10, 2):   # Increment range by 2
    print(x)
fruitList = ["Apple", "Peach", "Banana", "Orange", "Cherry"]
for x in foodList:      # Nested For Loop
    for y in fruitList:
        print(x, y)
for x in fruitList:
    pass                # Allows for loop to be empty w/o error