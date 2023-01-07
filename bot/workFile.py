
import random


def printAnecdote():
    text = ''
    with open('anecdote.txt', 'r', encoding='utf-8') as file:
        lineNumber = random.randint(1, 10)
        text = (file.readlines())[lineNumber-1]
        return text


def printCompliments():
    text = ''
    with open('compliments.txt', 'r', encoding='utf-8') as file:
        lineNumber = random.randint(1, 10)
        text = (file.readlines())[lineNumber-1]
        return text


def printSignZodiac():
    dictionary = {}
    with open('zodiac.txt', 'r', encoding='utf-8') as file:
        for i in range(12):
            string = file.readline().split(' ', 1)
            dictionary[string[0]] = string[1]
    return dictionary
