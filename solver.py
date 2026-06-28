from z3 import Solver, Distinct, sat
from utils import create_variables, word_to_number


def solve_cryptarithm(addends, result):
    words = addends + [result]
    variables = create_variables(words)
    solver = Solver()

    for variable in variables.values():
        solver.add(variable >= 0, variable <= 9)

    solver.add(Distinct(list(variables.values())))

    for word in words:
        solver.add(variables[word[0]] != 0)

    addend_values = [word_to_number(word, variables) for word in addends]
    result_value = word_to_number(result, variables)

    solver.add(sum(addend_values) == result_value)

    if solver.check() != sat:
        return None

    model = solver.model()

    return {
        letter: model[variables[letter]].as_long()
        for letter in sorted(variables)
    }