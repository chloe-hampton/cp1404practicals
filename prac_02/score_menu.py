MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input("> ")
    while choice != "Q":
        if choice == "G":
            # TODO: get_valid_score function
            ...
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
