import re

def remove_punctuation(str):
    return re.sub(r'[^\w\s]','',str)

def remove_whitespaces(str):
    return re.sub(r'[\s]','',str)

def remove_extra_spaces(str):
    return str.strip()

def truncate(str,length):
    return str[:length] + '...'

def contains_only_alpha(str):
    return bool(re.fullmatch(r'[A-Za-z\s]+',str))