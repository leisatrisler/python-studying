# We us while_loops to repeat a block of code multiple times
i = 1
while i <= 1_000:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1
# Either of these work line 10 and 15 are the same
i = 1
while i <= 10:
    print(i * '*')
    i += 1
