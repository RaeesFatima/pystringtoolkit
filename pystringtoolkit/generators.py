import random
import string
import re

def slugify(str:str)->str:
    """
        Convert a string into a slug by lowercasing, trimming, and replacing spaces with hyphens.

        Args:
            text (str): The input string.

        Returns:
            str: A slugified version of the string.

        Example:
            >>> slugify("Hello World Example")
    """
    str=str.lower().strip()
    return re.sub(r'\s+','-',str)

def random_string(length:int)->str:
    """
        Generate a random alphanumeric string of a given length.

        Args:
            length (int): The length of the string to generate.

        Returns:
            str: A randomly generated string containing letters and digits.

        Example:
            >>> random_string(8)
            'aB3kLm9X'
        """
    str=''.join(random.choices(string.ascii_letters+string.digits,k=length))
    return str


def reverse_string(text: str) -> str:
    """
    Reverse the given string.

    Args:
        text (str): The input string.

    Returns:
        str: The reversed string.

    Example:
        >>> reverse_string("Hello")
        'olleH'
    """
    return text[::-1]