MINIMUM_PASSWORD_LENGTH = 8

password = input("Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print(f"Password must contain at least {MINIMUM_PASSWORD_LENGTH} characters.")
    password = input("Password: ")

for characters in password:
    print('*', end="")
