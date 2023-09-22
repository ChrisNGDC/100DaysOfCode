PLACEHOLDER = '[name]'

with open('./Input/Letters/starting_letter.txt', 'rt') as letter_file:
    starting_letter = letter_file.read()

with open('./Input/Names/invited_names.txt', 'rt') as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    complete_letter = starting_letter.replace(PLACEHOLDER, name)
    with open(f'./Output/ReadyToSend/letter_to_{name}.txt', 'wt') as new_letter:
        new_letter.write(complete_letter)
