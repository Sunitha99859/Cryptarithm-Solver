from z3 import *


def main():
    S = Int("S")
    E = Int("E")
    N = Int("N")
    D = Int("D")
    M = Int("M")
    O = Int("O")
    R = Int("R")
    Y = Int("Y")

    letters = [S, E, N, D, M, O, R, Y]
    solver = Solver()
    for letter in letters:
        solver.add(letter >= 0)
        solver.add(letter <= 9)

    solver.add(Distinct(letters))
    solver.add(S != 0)
    solver.add(M != 0)

    SEND = (
        1000 * S +
        100 * E +
        10 * N +
        D
    )

    MORE = (
        1000 * M +
        100 * O +
        10 * R +
        E
    )

    MONEY = (
        10000 * M +
        1000 * O +
        100 * N +
        10 * E +
        Y
    )

    solver.add(SEND + MORE == MONEY)
    result = solver.check()
    if result == sat:
        model = solver.model()

        print("Solution Found\n")

        print("Letter Assignments")
        print("------------------")

        for letter in letters:
            print(f"{letter} = {model[letter]}")
        print()
        print("Puzzle")
        print("------")
        print(f"  {model.evaluate(SEND)}")
        print(f"+ {model.evaluate(MORE)}")
        print("------")
        print(f" {model.evaluate(MONEY)}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()