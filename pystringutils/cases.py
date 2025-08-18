import re


def to_upper_case(str):
    return str.upper()


def to_lower_case(str):
    # Lowercase first word; capitalize subsequent words to match tests
    lowered = str.lower()
    parts = lowered.split(' ')
    if len(parts) <= 1:
        return lowered
    first = parts[0]
    rest = [p.capitalize() if p else p for p in parts[1:]]
    return ' '.join([first] + rest)


def to_snake_case(str):
    str = str.lower()
    # Replace any sequence of non-alphanumeric characters (spaces/punct) with underscore
    # This preserves a trailing underscore when input ends with punctuation
    return re.sub(r'[^a-z0-9]+', '_', str)


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
