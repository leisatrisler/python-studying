# 3 types of data in Python, (Numbers, Booleans, and Strings)
1  # Numbers can be intergers
1.1  # Numbers can be floats
True or False  # (Boolenans)
'a'  # strings
# In Python there can be complex lists such as list of numbers, objects, or names

names = ["John", "Bob", "Mosh", "Sam", "Mary"]  # Example
print(names)

names = ["John", "Bob", "Mosh", "Sam", "Mary"]  # Example
print(names[0])

# Example -1 would represent the end of the list
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[-1])

# Example -2 would represent the second from the end of the list
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[-2])

# Example say John is misspelled
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"  # We then set it to a new value of "Jon" without an h
print(names)  # After running then we have our updated list

# Example we can also set a range of values, example if we are only interested in the first 3 values
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0]
# In between brackets, we need 2 indexes, a start and an end index
print(names[0:3])
# Python will return all elements between the start index up to the end index, but excluding the end index
# This does not modify our original list it returns a new list
