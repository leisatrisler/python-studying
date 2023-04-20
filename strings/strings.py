course = 'Python for Beginners'  # This string is technically an object
print(course.upper())  # This will print our string in upper case
print(course.lower())  # This is for converting a a string to lower case
# This to see if our string contains a character or squence of characters
print(course.find('Y'))
print(course.find('y'))  # This will return the first index of the character "y"
print(course)  # Our course variable is not effected
# Python is case sensitive
course = 'Python for Beginners'
# This will replace the index of the word "for"
# Replacing string # This does not replace the original string we end up with a new string
print(course.replace('for', '4'))

course = 'Python for Beginners'
print('Python' in course)  # in for in operator, after that type our variable
# When we run this we see the Boolean value
