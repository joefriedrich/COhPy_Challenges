#Author:  Joe Friedrich
#COhPy Challenge 2016-Apr solution

import requests
import re

print('Welcome to the Friedrich Gutenberg word-counter thingy.')
book_number = input('Type the number of the gutenberg publication you wish to see:  ')

print('Grabbing website data...')
website = requests.get('http://www.gutenberg.org/cache/epub/' + book_number + '/pg' + book_number + '.txt')

find_book = re.split(r'\*{3}[\s\w]*\*{3}', website.text)
book = find_book[1]

find_words = re.compile(r'[a-zA-Z]+')
words = find_words.findall(book)

print('Creating dictionary...')
dictionary = {}
for word in words:
    if len(word) > 1:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    elif word == 'A' or word == 'a' or word == 'I':
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

print('Organizing data...')
count_words = []
for entry in dictionary.items():
	count_words.append(entry)

count_words = sorted(count_words, key=lambda entry: entry[1])

print('What would you like to see?')
print('-Type a word to see how many times it appears.')
user_choice = input('-Type a number to see that number of top words:  ')

if(user_choice is str):
	print('string')	
else:
	print(count_words[-1 * int(user_choice):])
