# https://www.codewars.com/kata/577e277c9fb2a5511c00001d/train/python

def vowel_shifting(text: str, n: int) -> str:
    
    if n == 0:
        return text

    vowels: str = "aeiou" + "aeiou".upper()

    letters = set(text)
    has_vowels = False
    for letter in letters: 
        if letter in vowels: 
            has_vowels = True
            break
    if not has_vowels:
        return text
    
    vowels = [ x for x in text if x in vowels]

    # list of all the non vowels with their original index
    non_vowels = []
    
    for idx, char in enumerate(text):
        if char not in vowels:
            non_vowels.append((idx,char))

    # rotate the vowels 
    if n > 0:
        for _ in range(n):
            last_element = vowels[-1]

            del vowels[-1]

            vowels.insert(0, last_element)
    elif n < 0: 
        for _ in range(abs(n)):
            
            first_element = vowels[0]

            del vowels[0]

            vowels.append(first_element)


    for idx, char in non_vowels:
        vowels.insert(idx,char)

        print(vowels)
    
    return "".join(vowels)


print(vowel_shifting("AEIOUaeiou",1))