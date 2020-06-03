"""
Barack Obama Twitter Data Analysis 2012-2019
Matthew Garchik

What are his most common words?
Who does he @ the most?
What gets him the most likes and retweets?

Average likes: 14095.15092687199
Average retweets: 4162.726609254123
"""

import pandas as pd
df = pd.read_csv('/Users/garch/PycharmProjects/P2_SP20/Final Project/Tweets-BarackObama.csv')
df['Likes'].mean()
# Out[7]: 14095.15092687199
df['Retweets'].mean()
# Out[8]: 4162.726609254123
df['Likes'].plot.hist()


df['Tweet-text'] = df['Tweet-text'].str.upper()
df['Words'] = df['Tweet-text'].str.strip()
df['Words'] = df['Words'].str.split()

dict = {}
for i in range(df['Words'].size):
    for j in range(len(df['Words'][i])):
        if df['Words'][i][j] in dict.keys():
            dict[df['Words'][i][j]] += 1
        else:
            dict[df['Words'][i][j]] = 1

words_text_file = open('/Users/garch/Downloads/4148741-98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt', 'r')
data = words_text_file.readlines()
top_75 = [x.strip() for x in data[:75]]

new_dict = {}

keys = list(dict.keys())

for i in range(len(keys)):
    if keys[i].lower() not in top_75:
        new_dict[keys[i]] = dict[keys[i]]

sorted_d = sorted(new_dict.items(), key=lambda x: -x[1])



