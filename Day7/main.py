import random
import words
import art

lives = len(art.stages) - 1
chosen_word = random.choice(words.word_list)
guessed_letters = []

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

print(art.logo)

display = []
for _ in chosen_word:
    display += "_"

while "_" in display and lives > 0:
    print(art.stages[lives])
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"{guess} was already guessed, try another letter.")
    else:
        guessed_letters += guess
        if guess in chosen_word:
            print("Correct")
            for pos in range(len(chosen_word)):
                if chosen_word[pos] == guess:
                    display[pos] = guess
        else:
            print(f"Wrong. {guess} is not in the word.")
            lives -= 1
    print(" ".join(display))

print(art.stages[lives])
if lives > 0:
    print("You win.")
else:
    print("You lose.")
