# Python variables tutorial
x = 6
y = 7
z = x+y
str = "Hello"
str2 = "Python"
str3 = "Programming"
a, b, c = 1, 4, 5
d = e = f = "Combination"
print("The value of x is", x, "The value of y is", y )
print("The value of x is", b, "The value of y is", c )
print("Type of var x:" ,type(x), "type of var y:", type(y))
print(str + " " + str2 + " " + str3)
print("x + y equals: ", x+y)
print("x + y = ", z)
print(d)

def varFunc():
    global x
    x = "Fantastic"
varFunc()
print(x)