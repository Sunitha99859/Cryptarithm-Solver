import random

PUZZLES = [
    (["SEND", "MORE"], "MONEY"),
    (["TWO", "TWO"], "FOUR"),
    (["I", "BB"], "ILL"),
]


def generate_puzzle():
    return random.choice(PUZZLES)