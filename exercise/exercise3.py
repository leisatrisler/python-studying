# Make a dictionary that includes all the childrens names and age
# Iterate over the dictionary and print each childs age
# Except if its Audrey, print her name and age

dictionary = {"Audrey": 12, "Dustin": 10,
              "Hailey": 8, "Skylar": 8, "Kaidan": 4}

for k, v in dictionary.items():  # Example
    if k == "Audrey":
        print("Hello Audrey ", v)
    else:
        print(v)
