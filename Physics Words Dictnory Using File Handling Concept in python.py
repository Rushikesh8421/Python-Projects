#A python program in which you can find definations of physics related words
import json
data = json.load(open("C:/Users/Rushi/Desktop/data.json")) #Here you can place your own file name and location

def datafileset(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return 'Opps! that word does not exsist in our dictnory'

word = input('Enter the word: ')
output = datafileset(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)