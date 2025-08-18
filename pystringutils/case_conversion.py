def invert_cases(str):
    inverted = []
    for char in str:
        if char.islower():
            inverted.append(char.upper())
        elif char.isupper():
            inverted.append(char.lower())
        else:
            inverted.append(char) #This is for the case of the numericals part
    return ''.join(inverted)


