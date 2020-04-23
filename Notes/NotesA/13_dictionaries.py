# Dictionaries (dict)

# str, int, bool, list, tuple, dict, set, object

# Quick look at sets
# not used widely in python
# sets store UNIQUE values as unordered groups
my_set = {1, 2, 3, 4, 5}
print(my_set)

# one very specific use of a set
my_list = [6, 7, 8, 9, 8, 7]  # list with duplicates
print(set(my_list))

my_list = list(set(my_list))
print(my_list)


# Dictionaries are just unordered collections of key: info value

# Why use a dict over a list
mr_lee = ['Aaron', 'Lee', 46, ['Python', 'SQL']]
mr_leed = {'first': 'Aaron', 'last': 'Lee', 'age': 46, 'fav_prog_lang': ['Python', 'SQL']}

# structure {key1: val1, key2: val2...}

# Accessing values
print(mr_leed['age'])  # index a dict using the key
print(mr_leed['fav_prog_lang'][1])

# iterable
for key in mr_leed:
    print(mr_leed[key])

# adding to a dict
mr_leed['spoken_langs'] = ['English', 'Pig Latin']
print(mr_leed)

# cannot be accessed by index number

# Build a simple dict
community = {'genre': ['comedy'],
             'creators': ['Dan Harmon'],
             'starring': ['Joel McHale', 'Gillian Jacobs', "Danny Pudi"],
             'no_season': 6
             }

community['no_episodes'] = 110
print(community['no_episodes'])

# Change items in a dict
community['starring'].append('Alison Brie')
print(community['starring'])

# increment item
community['no_episodes'] += 1
print(community['no_episodes'])
