import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6

quick_picks = int(input("How many picks: "))
numbers = []
for i in range(quick_picks):
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randrange(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    for number in numbers:
        print(f"{number:2}", end=" ")
    print()


