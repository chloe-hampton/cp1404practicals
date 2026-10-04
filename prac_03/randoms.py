import random

# Line 1: Smallest possible output is 5, largest is 20

# Line 2: Smallest possible output is 3, largest is 9
# Chooses a random uneven number between 3 and 9. Possible outputs are 3, 5, 7, 9.

# Line 3: Smallest possible output is 2.5, largest is 5.5. Chooses a random float within specified range.

number = random.randint(1, 100)
print(number)