# We use if statements to make decisions in our programs
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")  # We type "if" then we type a condition
elif temperature > 20:  # elif stands for else if
    # We can have as many conditions as we want, there are no limitations
    print("It's a nice day")
elif temperature > 10:  # Means the temperature is greater than 10 and less than or equal to 20
    print(" It's a bit cold")
else:
    print(" It's cold")
print("Done")
