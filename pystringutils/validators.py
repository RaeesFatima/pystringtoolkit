import re


def is_email(text: str) -> bool:
    """Return True if the input is a valid email address, False otherwise.

    Uses a simple regex to validate common email formats.
    """
    if not text:
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, text) is not None