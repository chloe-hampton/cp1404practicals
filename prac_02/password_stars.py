MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_password()
    print_password_as_asterisks(password)


def print_password_as_asterisks(password):
    for characters in password:
        print('*', end="")


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must contain at least {MINIMUM_PASSWORD_LENGTH} characters.")
        password = input("Password: ")
    return password


main()
