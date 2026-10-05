name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
print(f"Hi {name}")
in_file.close()
