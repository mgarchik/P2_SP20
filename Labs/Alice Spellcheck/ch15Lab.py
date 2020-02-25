'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def linear_search(key, list):
    i = 0
    while i < (len(list) - 1) and key.upper() != list[i]:
        i += 1

    if i < len(list) - 1:
        return True
    else:
        return False

with open('dictionary.txt', 'r') as dict:
    dictionary_list = [x.strip().upper() for x in dict]

print("--- Linear Search ---")
misspellings = 0
alice200 = open('AliceInWonderLand200.txt', 'r')
on_line = 0
for line in alice200:
    line = line.strip()
    on_line += 1
    words = split_line(line)
    for word in words:
        if not linear_search(word, dictionary_list):
            print(word, "in line", on_line)
            misspellings += 1
print("There were", misspellings, "misspellings")


print("--- Binary Search ---")
def binary_search(word, list):
    if word not in list:
        return False
    key = list.index(word)
    lower_bound = 0
    upper_bound = len(list)
    found = False
    middle_pos = 0
    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if middle_pos < key:
            lower_bound = middle_pos + 1
        elif middle_pos > key:
            upper_bound = middle_pos - 1
        else:
            return True, middle_pos
    else:
        return False


misspellings = 0
alice200 = open('AliceInWonderLand200.txt', 'r')
on_line = 0
for line in alice200:
    line = line.strip().upper()
    on_line += 1
    words = split_line(line)
    for word in words:
        if not binary_search(word, dictionary_list):
            print(word, "in line", on_line)
            misspellings += 1
print("There were", misspellings, "misspellings")



# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
alice200 = open('AliceInWonderland.txt', 'r')
a_words = []
for line in alice200:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word not in a_words:
            a_words.append(word)
print(a_words)

looking_glass = open('AliceThroughTheLookingGlass.txt')
not_in = []
for line in looking_glass:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if not binary_search(word, a_words):
            not_in.append(word)
print(not_in)
print(len(not_in))