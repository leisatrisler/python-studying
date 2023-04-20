# There is another set of operators called Logicial Operators, we use them to build complex rules and conditions
price = 25
# With "and" if the answer is true it will return with Boolean answer of True
print(price > 10 and price < 30)
price = 5
# With "or" if one of the Boolean is True than the entire expersion will be True
print(price > 10 or price < 30)

price = 5
print(price > 10)  # This result is false

price = 5
print(not price > 10)  # If the not operator is applied it will become True

# Python has 3 logical operators
and  # Which returns True if both expressions return True
or  # Which returns True if at least one  expression returns True
not  # Which inverses any value we get
