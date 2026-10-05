def main():
    file_name = input("Enter filename: ")
    while file_name != "":
        print(determine_file_size(file_name))
        file_name = input("Enter filename: ")


def determine_file_size(file_name):
    try:
        number_of_lines = 0
        with open(file_name, "r") as in_file:
            for line in in_file:
                number_of_lines += 1
            return number_of_lines
    except FileNotFoundError:
        return "File not found"


main()
