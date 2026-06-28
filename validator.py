def validate_input(addends, result):
    if len(addends) < 2:
        return False, "At least two addends are required."

    if not result:
        return False, "Result word cannot be empty."

    words = addends + [result]

    for word in words:
        if not word.isalpha():
            return False, "Words must contain only letters."

        if len(word) == 0:
            return False, "Words cannot be empty."

    unique_letters = set("".join(words))

    if len(unique_letters) > 10:
        return (
            False,
            "More than 10 unique letters. Impossible with decimal digits."
        )

    return True, ""