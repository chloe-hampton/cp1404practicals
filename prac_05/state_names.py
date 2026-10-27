"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

is_valid = False
while not is_valid:
    try:
        state_code = input("Enter short state: ").upper()
        print(state_code, "is", CODE_TO_NAME[state_code])
        is_valid = True

    except KeyError:
        print("Invalid short state")

for code, state in CODE_TO_NAME.items():
    print(f"{code} is {state}")
