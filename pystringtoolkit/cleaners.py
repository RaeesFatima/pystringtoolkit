import re

def remove_punctuation(str:str)->str:
    """
        Remove all punctuation from a string, keeping only alphanumeric characters and whitespace.

        Args:
            text (str): The input string.

        Returns:
            str: The string with punctuation removed.

        Example:
            >>> remove_punctuation("Hello, World!")
            'Hello World'
        """
    return re.sub(r'[^\w\s]','',str)

def remove_whitespaces(str:str)->str:
    """
       Remove all whitespace characters from a string (spaces, tabs, newlines).

       Args:
           text (str): The input string.

       Returns:
           str: The string without any whitespace.

       Example:
           >>> remove_whitespaces("Hello World")
           'HelloWorld'
       """
    return re.sub(r'[\s]','',str)

def remove_extra_spaces(str:str)->str:
    """
        Remove leading and trailing spaces from a string.

        Args:
            text (str): The input string.

        Returns:
            str: The string without extra spaces at the beginning and end.

        Example:
            >>> remove_extra_spaces("   Hello World   ")
            'Hello World'
        """
    return str.strip()

def truncate(str,length:str)->str:
    """
        Truncate a string to a given length and append an ellipsis ("...").
        If the string is shorter than or equal to the given length, it is returned unchanged.

        Args:
            text (str): The input string.
            length (int): The maximum length of the truncated string.

        Returns:
            str: The truncated string with ellipsis if necessary.

        Example:
            >>> truncate("Hello World", 5)
            'Hello...'
        """
    return str[:length] + '...'

def contains_only_alpha(str:str)->bool:
    """
        Check if a string contains only alphabetic characters and spaces.

        Args:
            text (str): The input string.

        Returns:
            bool: True if the string contains only letters and spaces, False otherwise.

        Example:
            >>> contains_only_alpha("Hello World")
            True
            >>> contains_only_alpha("Hello123")
            False
        """
    return bool(re.fullmatch(r'[A-Za-z\s]+',str))
