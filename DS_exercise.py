from pprint import pprint
# find which letter is used the most in this sentence
# sentence = "This is a common interview question"
# # first check how many times each character is repeated
#     # store in a dictionary
# letters = {}
# # create for loop to add into dictionary
# for letter in sentence:
# # update frequency 
#     # check if we have that character and update frequency to one
#     if letter in letters:
#         letters[letter] += 1
#     else:
#     # add letter to letters 
#         letters[letter] = 1

# char_fequency = sorted(letters.items(), 
# key=lambda kv: kv[1], 
# reverse=True)

# print(char_fequency[0])
# more readable use pretty printing

sentence = "This is a long senctence to count how many times each character is used."

dictionary = {}

for letter in sentence:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

char_frequency = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
answer = char_frequency[0]
pprint(answer[1])