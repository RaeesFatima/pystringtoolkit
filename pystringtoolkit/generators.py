import random
import string
import re

def slugify(str):
    str=str.lower().strip()
    return re.sub(r'\s+','-',str)

def random_string(length):
    str=''.join(random.choices(string.ascii_letters+string.digits,k=length))
    return str