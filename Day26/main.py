import pandas as p

phonetic_data = p.read_csv('./nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

while True:
    word = input('Enter a word → ').upper()
    try:
        nato_phonetic_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters are valid.")
    else:
        break

print(nato_phonetic_word)
