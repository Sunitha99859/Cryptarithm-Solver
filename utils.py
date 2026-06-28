from z3 import Int


def create_variables(words):
    unique_letters = set("".join(words))
    return {letter: Int(letter) for letter in unique_letters}


def word_to_number(word, variables):
    value = 0
    for letter in word:
        value = value * 10 + variables[letter]
    return value