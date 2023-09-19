import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Dictionary Comprehension
# Above the iterrows() iterates each row in the Dataframe and each iteration produces an index object and a row object
# So we used index and row above as "for (index, row)"
# and from row object we added column "letter" and "code" which is present in the csv file to add in our dictionary
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word: ").upper()
phonetic_words = [phonetic_dict[letter] for letter in user_input]  # List Comprehension
print(phonetic_words)
