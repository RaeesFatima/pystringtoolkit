import pytest
from pystringtoolkit.validators import is_email

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