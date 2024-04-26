# Testing python functions
# Defining and calling a basic function:
def hello_function():
    print("Hello from Python!")
hello_function()
# Function with args:
def hello_name(name):
    print(f"Hello {name}")
hello_name("Jason Thomson")
# Arbitrary Arguments:
def multi_names(*names):        # Gets arguments as tuple
    numNames = len(names)
    for x in range(numNames):
        print(f"Hello {names[x]}")
multi_names("Ryan", "Howard", "Chase")
# Keyword Arguments:
def keyword_function(fruit1, fruit2, fruit3):
    print(f"The last fruit is {fruit3}")
keyword_function(fruit1="Apple", fruit2="Cherry", fruit3="Peach")   # Different way to do the above
# Arbitrary Keyword Arguments (**kwargs):
def arb_keyword(**student):     # Gets arguments as dictionary
    print("The last name of the student is " + student["lname"])
arb_keyword(fname = "Jason", lname = "Thomson")
# Default Parameter:
def country_function(country = "United States"):        # If no parameter is passed, country is default
    print(f"I am from {country}")
country_function("France")
country_function("Germany")
country_function()
# Passing List as an argument:
def list_function(cars):
    for x in cars:
        print(x)
carList = ["BMW", "Audi", "Lamborghini", "Mclaren", "Mercedes"]
list_function(carList)
# Return values:
def return_num(num):
    return num
print(f"Returned num {return_num(5)}")
# Pass function:
def pass_function():
    pass                # No error with empty function
# Positional-Only arguments
def pos_function(x, /):
    print(x)
#pos_function(x=3)       # Not allowed
pos_function(5)
# Keyword-Only arguments
def key_function(*, x):
    print(x)
key_function(x=3)
#key_function(x)         # Not allowed
# Combined positional and keyword only:
def combo_function(x, y, /, *, z, t):       # Any argument before / is positional only
    print(x + y + z + t)                    # Any argument after * are keyword only
combo_function(7, 5, t= 8, z=1)
# Recursive function:
def recursive_add(num):
    print("In function")
    if (num > 0):
        res = num + recursive_add(num - 1)
        print(res)
    else:
        res = 0
        print(res)
    return res
print("Beginning Recursion")
recursive_add(7)

