import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
NATO_alphabet_file = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet_data = NATO_alphabet_file.iterrows()
NATO_dict = {row.letter:row.code for (index, row) in NATO_alphabet_data}
# print(NATO_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.
# name = [n for n in input("Enter a name: ").upper()]
# Nato_spelling = [NATO_dict[letter] for letter in name if letter in NATO_dict]
# print(Nato_spelling)

# a redo of number 2 with error handling implemented
def generate_phonetic():
    name = input("Enter a name: ").upper()
    try:
        nato_spelling = [NATO_dict[letter] for letter in name]
    except KeyError:
        print("Input Error: Only letters in the alphabet are accepted")
        generate_phonetic()
    else:
        print(nato_spelling)


generate_phonetic()
