from solver import solve_cryptarithm
from formatter import print_solution
from validator import validate_input


def main():
    print("===== Cryptarithm Solver =====\n")

    try:
        count = int(input("Enter the number of addends: "))

        if count < 2:
            print("A cryptarithm must have at least two addends.")
            return

        addends = []

        for i in range(count):
            word = input(f"Enter addend {i + 1}: ").strip().upper()
            addends.append(word)

        result = input("Enter the result word: ").strip().upper()

        valid, message = validate_input(addends, result)

        if not valid:
            print(f"\nError: {message}")
            return

        solution = solve_cryptarithm(addends, result)

        print_solution(addends, result, solution)

    except ValueError:
        print("Please enter a valid integer for the number of addends.")


if __name__ == "__main__":
    main()