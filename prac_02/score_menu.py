MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input("> ")
    while choice != "Q":
        if choice == "G":
            score = get_valid_input("Score: ", 1, 100)
        elif choice == "P":
            # TODO: determine_result function
            ...
        elif choice == "S":
            # TODO: print_stars function
            ...
        else:
            print("Invalid input")
        print(MENU)
        choice = input("> ")


def get_valid_input(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input.")
        number = float(input(prompt))
    return number


main()
