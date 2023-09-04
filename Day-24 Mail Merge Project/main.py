# ===== Welcome to the Python File Handling Project ===== #
# Create birthday invitation card for each friend you want to invite.
PLACEHOLDER = "[name]"

# Create names list by fetching data from a file.
with open("Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

# Generating invitation card
with open("Input/Letters/starting_letter.txt") as letter_format:
    letter_contents = letter_format.read()
    for name in names_list:
        stripped_name = name.strip()  # This removes next line from name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # It replaces "[name]" with actual name of your friend within the list.
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:  # Generating file
            complete_letter.write(new_letter)
