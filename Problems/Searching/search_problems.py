'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
with open('dictionary.txt', 'r') as f:
    words = [x.strip().upper() for x in f]
    print(words)
    lengths = [len(x) for x in words]
    print(lengths)
    print("The longest word is", words[lengths.index(max(lengths))])


# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
with open('AliceInWonderLand.txt', 'r') as f:
    all_words = []
    for line in f:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            all_words.append(word)
    print(all_words)
    lengths = [len(x) for x in all_words]
    print("There are", len(all_words), "Words")
    print("The average word length is ", (sum(lengths) / len(all_words)), "letters")

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
with open('AliceInWonderLand.txt', 'r') as f:
    alices = 0
    for line in f:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            if "ALICE" in word:
                alices += 1
    print("There are", alices, "Alices")


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"

all_words = []
with open('AliceInWonderLand.txt', 'r') as f:
    for line in f:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            if len(word) == 7:
                all_words.append(word)
    uniques = list(set(all_words))
    print(all_words)
    counts = [all_words.count(x) for x in uniques]
    print(counts)
    print("The most common 7 letter word is", uniques[counts.index(max(counts))])



# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
with open('AliceInWonderLand.txt', 'r') as f:
    cats = 0
    cheshires = 0
    cat = False
    cheshire = False
    both = 0
    for line in f:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            if word == "CAT" or word == "CATS":
                cats += 1
                cat = True
            else:
                cat = False
            if cat and cheshire:
                both += 1
            if "CHESHIRE" in word:
                cheshires += 1
                cheshire = True
            else:
                cheshire = False

    print("There are", cats, "Cats")
    print("There are", cheshires, "Cheshires")
    print("There are", both, "Cheshires followed by cats")


