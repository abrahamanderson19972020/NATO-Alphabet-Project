import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format and import all the information into a list:
{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
new_dic = {row.letter: row.code for index, row in df.iterrows()}
print(new_dic)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your word>>>").upper()
new_list = [new_dic[letter] for letter in user_input]
#Below is the another way for creating the list
# new_list = list()
# for word in user_input:
#     new_list.append(new_dic[word])
print(new_list)
