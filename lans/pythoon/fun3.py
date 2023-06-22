def cword(word):
    if len(word) == 1:
        return word
    print(f"{word}")
    if word[0] == word[1]:
        return cword(word[1:])

    return word[0]+cword(word[1:])


print(cword("aaassjjjjffffdd"))
