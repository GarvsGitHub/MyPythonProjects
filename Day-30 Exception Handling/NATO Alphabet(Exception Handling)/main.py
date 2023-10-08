# ===== Welcome back to the NATO Phonetic Dictionary ===== #
# In this project we have added exception handling for wrong user input and have also used List Comprehension.
# Other than this minor changes rest of the functionality is same as previous project of NATO Alphabet.
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Dictionary Comprehension
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter the word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]  # List Comprehension
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # Calls Itself when wrong user input
    else:
        print(output_list)


generate_phonetic()
