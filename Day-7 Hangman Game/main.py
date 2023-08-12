# ====== Welcome to Hangman Game ====== #
# This code works finest on 'replit' website as we have imported their customized function just for UI improvement, 
# otherwise there is no difference other than clear screen

from replit import clear
import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
logo = hangman_art.logo
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks for guessing word
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You have already guessed: {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f'You lose! The correct word was "{chosen_word}".')

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages = hangman_art.stages
    print(stages[lives])
