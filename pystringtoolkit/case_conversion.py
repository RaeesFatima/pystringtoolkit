def invert_cases(str:str)->str:
    """
       Invert the case of each character in a string.
       Lowercase characters become uppercase, and uppercase characters become lowercase.
       Non-alphabetic characters (like numbers and symbols) remain unchanged.

       Args:
           text (str): The input string.

       Returns:
           str: A string with inverted letter cases.

       Example:
           >>> invert_cases("Hello World 123")
           'hELLO wORLD 123'
       """
    inverted = []
    for char in str:
        if char.islower():
            inverted.append(char.upper())
        elif char.isupper():
            inverted.append(char.lower())
        else:
            inverted.append(char) #This is for the case of the numericals part
    return ''.join(inverted)


