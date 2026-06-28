def print_solution(addends, result, solution):
    if solution is None:
        print("\nNo solution exists.")
        return

    print("\nLetter Assignments")
    print("------------------")

    for letter, digit in sorted(solution.items()):
        print(f"{letter} = {digit}")

    print("\nSolved Puzzle")
    print("-------------")

    converted = [
        "".join(str(solution[ch]) for ch in word)
        for word in addends
    ]
    result_number = "".join(str(solution[ch]) for ch in result)

    width = max(len(result_number), *(len(n) for n in converted))

    for i, number in enumerate(converted):
        prefix = "+ " if i == len(converted) - 1 else "  "
        print(prefix + number.rjust(width))

    print("-" * (width + 2))
    print(" " + result_number.rjust(width))