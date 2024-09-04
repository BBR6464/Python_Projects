PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as latter_file:
    latter_contents = latter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_latter = latter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/latter_for_{stripped_name}.txt", mode="w") as completed_latter:
            completed_latter.write(new_latter)