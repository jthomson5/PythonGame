# Testing If-Else statements in Python
a = 35
b = 56
c = 37
if a > b:
    print(f"{a} is greater than {b}")
elif a == c:
    print(f"{a} is equal to {c}")
else:
    print(f"{a} is not greater than {b} or equal to {c}")
# Short hand
if a < b: print(f"{a} is less than {b}")
d = 78
e = 102
print("D") if d > e else print("E")
f = 78
print("D") if d > f else print("Equal") if d == f else print("F")   # Conditional Expression
# Logical Operators
if b > a and c > a:     # AND
    print(f"Both {b} and {c} are greater than {a}")
if b < a or c > a:      # OR
    print(f"{b} is less than {a} or {c} is greater than {a}")
if not a > b:           # NOT
    print(f"{a} is NOT greater than {b}")
# Nested IF's
if a > 10:
    print(f"{a} is greater than 10")
    if a > 20:
        print(f"{a} is greater than 20")
        if a > 40:
            print(f"{a} is greater than 40")
        else:
            print(f"{a} is not greater than 40")
# Pass statement
if a > b:       # No error on if statement 
    pass