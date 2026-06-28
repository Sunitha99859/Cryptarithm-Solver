from z3 import Int, Solver, Distinct, sat


def word_to_number(word, variables):
    value = 0

    for letter in word:
        value = value * 10 + variables[letter]

    return value


def create_variables(words):
    unique_letters = set("".join(words))
    variables = {}

    for letter in unique_letters:
        variables[letter] = Int(letter)

    return variables


def solve_cryptarithm(addends, result):
    words = addends + [result]

    variables = create_variables(words)

    solver = Solver()

    for variable in variables.values():
        solver.add(variable >= 0)
        solver.add(variable <= 9)

    solver.add(Distinct(list(variables.values())))

    for word in words:
        solver.add(variables[word[0]] != 0)

    addend_values = []

    for word in addends:
        addend_values.append(word_to_number(word, variables))

    result_value = word_to_number(result, variables)

    solver.add(sum(addend_values) == result_value)

    if solver.check() != sat:
        return None

    model = solver.model()

    solution = {}

    for letter in sorted(variables.keys()):
        solution[letter] = model[variables[letter]].as_long()

    return solution


def print_solution(addends, result, solution):
    if solution is None:
        print("\nNo solution exists.")
        return

    print("\nLetter Assignments")
    print("------------------")

    for letter, digit in solution.items():
        print(f"{letter} = {digit}")

    print("\nSolved Puzzle")
    print("-------------")

    converted = []

    for word in addends:
        number = "".join(str(solution[ch]) for ch in word)
        converted.append(number)

    result_number = "".join(str(solution[ch]) for ch in result)

    width = max(len(result_number), max(len(n) for n in converted))

    for i, number in enumerate(converted):
        prefix = "+ " if i == len(converted) - 1 else "  "
        print(prefix + number.rjust(width))

    print("-" * (width + 2))
    print(" " + result_number.rjust(width))


def main():
    print("Cryptarithm Solver\n")

    addends = []

    count = int(input("Enter number of addends: "))

    for i in range(count):
        word = input(f"Enter addend {i + 1}: ").strip().upper()
        addends.append(word)

    result = input("Enter result word: ").strip().upper()

    solution = solve_cryptarithm(addends, result)

    print_solution(addends, result, solution)


if __name__ == "__main__":
    main()