colour_to_code = {"aqua": "#00ffff", "gray": "#bebebe", "jade": "#00a86b", "lavender": "#e6e6fa", "lemon": "#fff700",
                  "lilac": "#c8a2c8", "magenta": "#ff00ff", "grullo": "#a99a86", "ginger": "#b06500",
                  "emerald": "#50c878"}

colour = input("Enter colour: ").lower()
while colour != "":
    is_valid = False

    while not is_valid and colour != "":
        try:
            print(colour, "is", colour_to_code[colour])
            is_valid = True
        except KeyError:
            print("Invalid colour")
            colour = input("Enter colour: ").lower()

    if colour != "":
        colour = input("Enter colour: ").lower()