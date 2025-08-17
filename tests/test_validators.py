import pytest
from pystringutils.validators import is_email, is_numeric

def test_is_email():
    # Valid email addresses
    assert is_email("user@example.com") is True
    assert is_email("user.name+tag@example.co.uk") is True
    assert is_email("user123@sub.domain.com") is True
    
    # Invalid email addresses
    assert is_email("") is False
    assert is_email("invalid.email") is False
    assert is_email("@domain.com") is False
    assert is_email("user@") is False
    assert is_email("user@.com") is False
    assert is_email("user@domain.") is False


def test_is_numeric():
    # Valid numerics
    assert is_numeric("0") is True
    assert is_numeric("1") is True
    assert is_numeric("123") is True
    assert is_numeric("000123") is True

    # Invalid numerics
    assert is_numeric("abc") is False
    assert is_numeric("12.34.56") is False
    assert is_numeric(True) is False

    assert is_numeric("-1") is True         # Simple negative
    assert is_numeric("-123") is True       # Multi-digit negative
    assert is_numeric("-0") is True         # Negative zero (mathematically valid)
    
    # === DECIMAL NUMBERS ===
    assert is_numeric("0.0") is True        # Simple decimal
    assert is_numeric("12.34") is True      # Standard decimal
    assert is_numeric("-45.67") is True     # Negative decimal
    assert is_numeric(".5") is True         # Decimal without leading digit
    assert is_numeric("5.") is True         # Decimal without trailing digits
    assert is_numeric("-.5") is True        # Negative decimal without leading digit
    
    # === SCIENTIFIC NOTATION ===
    assert is_numeric("1e5") is True        # Simple scientific notation
    assert is_numeric("1.23e4") is True     # Decimal with exponent
    assert is_numeric("1.23e-4") is True    # Negative exponent
    assert is_numeric("1.23E4") is True     # Capital E notation
    assert is_numeric("-1.23e-4") is True  # Negative number in scientific notation
    assert is_numeric("1e+5") is True      # Explicit positive exponent
    
    # === WHITESPACE HANDLING ===
    assert is_numeric("  123  ") is True    # Leading and trailing spaces
    assert is_numeric(" -45.67 ") is True  # Spaces around negative decimal
    assert is_numeric("\t123\n") is True   # Tab and newline characters
    
    # === EDGE CASE VALID NUMBERS ===
    assert is_numeric("0.000001") is True  # Very small decimal
    assert is_numeric("1000000") is True   # Large integer without scientific notation

    assert is_numeric("abc") is False       # Pure alphabetic
    assert is_numeric("hello123") is False  # Mixed letters and numbers
    assert is_numeric("123abc") is False    # Numbers followed by letters
    assert is_numeric("12a34") is False     # Letters in the middle
    
    # === MALFORMED DECIMAL NUMBERS ===
    assert is_numeric("12.34.56") is False # Multiple decimal points
    assert is_numeric("12..34") is False   # Adjacent decimal points
    assert is_numeric("..123") is False    # Multiple leading decimal points
    assert is_numeric("123..") is False    # Multiple trailing decimal points
    
    # === MALFORMED NEGATIVE SIGNS ===
    assert is_numeric("1-23") is False     # Negative sign in middle
    assert is_numeric("123-") is False     # Negative sign at end
    assert is_numeric("--123") is False    # Multiple negative signs
    assert is_numeric("-") is False        # Just a negative sign
    assert is_numeric("+-123") is False    # Conflicting signs
    
    # === MALFORMED SCIENTIFIC NOTATION ===
    assert is_numeric("1e") is False       # Missing exponent value
    assert is_numeric("e5") is False       # Missing base number
    assert is_numeric("1e2.3") is False    # Decimal in exponent
    assert is_numeric("1ee5") is False     # Multiple e's
    assert is_numeric("1e+") is False      # Missing exponent after sign

    assert is_numeric(123) is True         # Integer input
    assert is_numeric(45.67) is True       # Float input
    assert is_numeric(-89) is True         # Negative integer input
    
    # === INFINITY AND NaN ===
    assert is_numeric("inf") is True       # Positive infinity
    assert is_numeric("-inf") is True      # Negative infinity
    assert is_numeric("nan") is True       # Not a Number (still a float in Python)
    assert is_numeric("INF") is True       # Case insensitive infinity
    assert is_numeric("NaN") is True       # Case insensitive NaN
    
    # === ADDITIONAL EDGE CASES ===
    assert is_numeric("") is False         # Empty string
    assert is_numeric("   ") is False      # Whitespace only
    assert is_numeric("\t\n") is False     # Tab and newline only
    assert is_numeric(None) is False       # None value
    assert is_numeric([]) is False         # Empty list
    assert is_numeric({}) is False         # Empty dict
    assert is_numeric(set()) is False      # Empty set
    assert is_numeric(()) is False         # Empty tuple
    
    # === NON-STANDARD NUMERIC FORMATS ===
    assert is_numeric("0x123") is False    # Hexadecimal (not standard numeric)
    assert is_numeric("0o123") is False    # Octal (not standard numeric)
    assert is_numeric("0b101") is False    # Binary (not standard numeric)
    assert is_numeric("1+2j") is False     # Complex number string
    
    # === OVERFLOW CASES ===
    assert is_numeric("1" + "0" * 400) is True  # Very large number (should work)
    
    # === CUSTOM OBJECTS ===
    class NumericStr:
        def __str__(self):
            return "42"
    
    class BadStr:
        def __str__(self):
            raise ValueError("Bad conversion")
    
    assert is_numeric(NumericStr()) is True    # Object with numeric __str__
    assert is_numeric(BadStr()) is False       # Object that raises in __str__
