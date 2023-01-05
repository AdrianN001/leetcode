

def commonChars(words: list) -> list:

    all_chars = []

    for char in words[0]:

        for szo in words[1:]:
            if char not in szo:
                break
        else:
            all_chars.append(char)


    return all_chars

print(commonChars(["bella","label","roller"]))
