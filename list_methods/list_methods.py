# Strings in Python are objects
# Strings in programming are kind of like objects in the real world, they have certain capablities
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # This is to add a new element
print(numbers)

numbers = [1, 2, 3, 4, 5]
# This is to insert a new element # Then go to top to "view" and look at perameter info
numbers.insert(0, -1)
print(numbers)  # After running, -1 will be at the beginning of our list

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  # We can also remove numbers
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.clear()  # If we want to remove items in the lists we use the clear method, this method doesn't expect any values
print(numbers)

numbers = [1, 2, 3, 4, 5]
# Example sometimes we want to see if a number is in our list, we use the in operator method
print(1 in numbers)  # This is a Boolean expression, True

numbers = [1, 2, 3, 4, 5]
# If we search for something not in list then the answer would be False
print(10 in numbers)

numbers = [1, 2, 3, 4, 5]
# Sometimes you want to know how many items you have in a list to do that you can use the built in len function
print(len(numbers))
