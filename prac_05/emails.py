"""
Emails
Estimate: 30 minutes
Actual: 56 minutes
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        # Get correct name from email
        name = extract_email(email)
        choice = input(f"Is your name {name}? (Y/n): ").lower()

        if choice == "y" or choice == "yes":
            name_to_email[name] = email
        else:
            name = input("Enter name: ")
            name_to_email[name] = email

        email = input("Email: ")

    longest_name = max(len(name) for name in name_to_email)
    for name, email in name_to_email.items():
        print(f"{name:{longest_name}} ({email})")


def extract_email(email):
    name = email.split("@")[0]  # Split after @ sign
    # Split depending on email separator
    if "." in name:
        name = name.split(".")
        name = " ".join(name)
    elif "-" in name:
        name = name.split("-")
        name = " ".join(name)
    elif "_" in name:
        name = name.split("_")
        name = " ".join(name)

    name = name.title()
    return name


main()
