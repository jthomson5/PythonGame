# Testing lambda functions in Python
x = lambda a : a + 10       # Simple addition lambda
print(x(5))
y = lambda a, b : a * b     # Simple multiplication lambda
print(y(7, 10))
# Lambda function in another function
def lam_function(num):
    return lambda a : a * num
double_it = lam_function(2)     # Double number 
print(double_it(50))
quintuple_it = lam_function(5)
print(quintuple_it(20))         # Quintuple number   