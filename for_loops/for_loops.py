# In Python there are times you want to iterate over a list & access each item individually
numbers = [1, 2, 3, 4, 5]
print(numbers)  # This comes out exactly the same

# If we can to print each item on a seperate line, that is where we use the for loop
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)  # After running then we have each item on a new line

numbers = [1, 2, 3, 4, 5]
for item in numbers:  # We can do the same thing but with a while loop
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
