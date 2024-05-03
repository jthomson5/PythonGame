# Testing iterators in Python
fruitTuple = ("Apple", "Cherry", "Cantaloupe")      # Lists, tuples, dictionaries, and sets all have iter() method
testIterator = iter(fruitTuple)     # Gets iterator for fruitTuple
print(next(testIterator))
print(next(testIterator))           # Get next element
print(next(testIterator))
str = "Hello World"     # Also iterable
strIterator = iter(str)
print(next(strIterator))
print(next(strIterator))
print(next(strIterator))            # Get next element
print(next(strIterator))
print(next(strIterator))
for x in str:           # Does same thing as above, calls the next method for each loop
    print(x)
class iterNumbers:      # Custom iterator
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration     # Stop iteration (would loop forever if not stopped)
testClass = iterNumbers()
myiter = iter(testClass)

for x in myiter:        # Calls next() repeatedly
    print(x)