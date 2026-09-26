MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Name: ")
print(MENU)
choice = input("Choice: ")
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Choice: ")
print("Finished!")