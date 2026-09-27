MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input("> ").upper()
    score = ""
    while choice != "Q":
        if choice == "G":
            score = get_valid_input("Score: ", 1, 100)
        elif choice == "P":
            result = determine_result(score)
            print(f"User score {score} is {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input("> ").upper()
    print("Farewell.")


def get_valid_input(prompt, low, high):
    """Get valid input"""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input.")
        number = float(input(prompt))
    return number


def determine_result(score):
    """Determine score state"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(number):
    """Print stars for number"""
    for i in range(int(number)):
        print('*')


main()
