PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    # invited_names = names_file.read().split("\n")
    invited_names = names_file.readlines()

# Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as template_file:
    letter_template = template_file.read()
    for name in invited_names:
        stripped_name = name.strip()
        # Replace the [name] placeholder with the actual name.
        letter = letter_template.replace(PLACEHOLDER, stripped_name)
        # Save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as draft:
            draft.write(letter)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
