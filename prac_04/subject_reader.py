"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_data = load_subject_data(FILENAME)
    display_subject_details(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_data = []
    for line in input_file:
        parts = line.split(',')  # Separate the data into its parts (each line)
        record = [parts[0], parts[1], int(parts[2])]
        subject_data.append(record)  # Adds each record to data as a nested list
    input_file.close()
    return subject_data


def display_subject_details(data):
    for subject, lecturer, number_of_students in data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students.")


main()
