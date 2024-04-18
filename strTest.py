# Testing out Python strings
import datetime 
multi = '''Testing out multi
line strings.'''
tstStr = "Python treats strings as an array of unicode characters!"
print(multi)
print(tstStr[5])    # Get char in string
len = len(tstStr);  # Get length of string
print(len)
print("arr" in tstStr)    # Check if substring exists in string
if "arr" in tstStr:
    print("The substring arr exists in the string!")   # If statement version of the above
if "slinky" not in tstStr:  # Not version of the above
    print("Slinky is not in the string!")
# Slicing Strings
print("Characters 2-9:", tstStr[2:9])
print("First 9 characters:",tstStr[:8])
slicedStr = tstStr[3:]
print("Characters after index 3:", slicedStr)
print(tstStr[-11:-2])   # Negative index slicing!
# String functions
upperStr = tstStr.upper()   # Convert string to uppercase
print("UPPERCASE STRING:", upperStr)    
lowerStr = tstStr.lower()   # Convert string to lowercase
print("lowercase string:", lowerStr)
weirdStr = " Weirdly spaced string "
strippedStr = weirdStr.strip() # Remove leading/trailing whitespace from string
print("Stripped string:", strippedStr)
repStr = tstStr.replace("a", "z")   # Replace all a's int the string with z's
print("String with replaced characters", repStr)
splitStr = tstStr.split(" ")    # Split string into substrings by space
print("Substrings:", splitStr)
# Formatting Strings
currentTime = datetime.datetime.now()   # Just wanted to try this
formatStr = "The current date and time is:" 
print(formatStr, currentTime)
timeStr = f"The current date and time is: {currentTime}" # f string (better version of the above)
print(timeStr)
price = 73650
moneyStr = f"The price of the vehicle is ${price:.2f}"  # f string with formatting up to 2 decimal places
print(moneyStr)
shipStr = f"The price of the ship is ${25*price:.2f}"   # Arithmetic version of above
print(shipStr)
quoteStr = "A wise man once said \"Something Insightful\" "   # Escape characters
print(quoteStr)
octalStr = "\120\131\124\110\117\116"
print(f"Octal String: {octalStr}!") # Octal escape characters