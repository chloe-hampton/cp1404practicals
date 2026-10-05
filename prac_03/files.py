# Question 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# # Question 2
in_file = open("name.txt", "r")
name = in_file.read()
print(f"Hi {name}")
in_file.close()

# Question 3
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)


# Question 4
result = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        result += int(line)
    print(result)