import re

def to_upper_case(str):
    return str.upper()

def to_lower_case(str):
    return str.lower()

def to_snake_case(str):
    str=str.lower()
    str = re.sub(r'[^\w\s]', '', str)
    return re.sub(r'\s+','_',str)

def to_kebab_case(str):
    str=str.lower()
    str = re.sub(r'[^\w\s]', '', str)
    return re.sub(r'\s+','-',str)

def to_pascal_case(str):
    return str.title().replace(' ','')

def to_camel_case(str):
    str=str.title().replace(' ','')
    return str[0].lower() + str[1:]

def to_title_case(str):
    return str.title()
def to_alternating_case(str):
    altrnated_case = []
    for i, char in enumerate(str):
        if i % 2 == 0:
            altrnated_case.append(char.upper())
        else:
            altrnated_case.append(char.lower())
    return ''.join(altrnated_case)
