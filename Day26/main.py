import pandas as p

phonetic_data = p.read_csv('./nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

word = input('Enter a word → ').upper()

nato_phonetic_word = [phonetic_dict[letter.upper()] for letter in word if letter in phonetic_dict]

print(nato_phonetic_word)
