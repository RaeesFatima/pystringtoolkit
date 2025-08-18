import pytest
from pystringutils.validators import is_email


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


@pytest.mark.parametrize(
    "address",
    [
        "USER@EXAMPLE.COM",
        "first_last@example.io",
        "name.surname+alias@domain.info",
        "x@a9.io",
    ],
)
def test_is_email_additional_valid(address):
    assert is_email(address) is True


@pytest.mark.parametrize(
    "address",
    [
        None,
        " user@example.com ",  # spaces
        "user@@example.com",   # double @
        "user@domain",         # missing TLD
        "user@domain.c",       # TLD too short
    ],
)
def test_is_email_additional_invalid(address):
    assert is_email(address) is False