import re
def is_email():
    pass

def isalpha(s:str)->bool:
     return re.fullmatch(r"[A-Za-z]+", s) is not None

def is_numeric(string):
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
