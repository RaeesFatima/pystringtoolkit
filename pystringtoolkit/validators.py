import re
def is_email(text:str)->bool:
    """
    Validate whether a string is a valid email address.

    Uses a simple regex to check common email formats.

    Args:
        text (str): The input string.

    Returns:
        bool: True if the input is a valid email address, False otherwise.

    Example:
        >>> is_email("test@example.com")
        True
        >>> is_email("not-an-email")
        False
    """
    if not text:
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, text) is not None

def isalpha(s:str)->bool:
    """
        Check if a string contains only alphabetic characters (A–Z, a–z).

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string contains only alphabetic characters, False otherwise.

        Example:
            >>> isalpha("Hello")
            True
            >>> isalpha("Hello123")
            False
    """
    return re.fullmatch(r"[A-Za-z]+", s) is not None

def is_numeric(string:str|int|float)->bool:
    """
    Check if a value can be interpreted as a numeric value.
    
    Args:
        string: The value to check (can be string, int, float, or other types)
        
    Returns:
        bool: True if the value is numeric, False otherwise
        
    Examples:
        >>> is_numeric("123")
        True
        >>> is_numeric("12.34")
        True
        >>> is_numeric("1e5")
        True
        >>> is_numeric("abc")
        False
    """
    # Explicitly reject booleans (which are int subclasses in Python)
    if isinstance(string, bool):
        return False

    # Accept native numeric types
    if isinstance(string, (int, float)):
        return True
    
    # Reject None and container types early
    if string is None or isinstance(string, (list, dict, set, tuple)):
        return False
    
    # Convert to string and strip whitespace
    try:
        string_value = str(string).strip()
    except Exception:
        # Handle objects that might raise in __str__
        return False
        
    if not string_value:
        return False
    
    # Fast path for simple positive integers
    if string_value.isdigit():
        return True
    
    # Comprehensive validation for all other numeric formats
    try:
        float(string_value)
        return True
    except ValueError:
        return False
    

def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards), ignoring case and non-alphanumeric characters.

    Args:
        text (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("A man, a plan, a canal, Panama")
        True
        >>> is_palindrome("Hello")
        False
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def are_anagrams(text1: str, text2: str) -> bool:
    """
    Check if two strings are anagrams of each other (contain the same letters in a different order), ignoring case and spaces.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Example:
        >>> are_anagrams("Listen", "Silent")
        True
        >>> are_anagrams("Hello", "World")
        False
    """
    from collections import Counter
    return Counter(text1.lower().replace(" ", "")) == Counter(text2.lower().replace(" ", ""))

