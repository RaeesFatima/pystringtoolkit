def char_frequency(text: str) -> dict:
    """
    Count the frequency of each character in a string.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.

    Example:
        >>> char_frequency("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


def most_common_char(text: str) -> str | None:
    """
    Find the most common character in a string.

    Args:
        text (str): The input string.

    Returns:
        str | None: The character that appears most frequently, or None if string is empty.

    Example:
        >>> most_common_char("hello")
        'l'
    """
    if not text:
        return None
    freq = char_frequency(text)
    return max(freq, key=freq.get)


def word_count(text: str) -> dict:
    """
    Count the occurrences of each word in a string (case-insensitive).

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with words as keys and their counts as values.

    Example:
        >>> word_count("Hello hello world")
        {'hello': 2, 'world': 1}
    """
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def unique_words(text: str) -> list:
    """
    Return a list of unique words from the string (case-insensitive), preserving order.

    Args:
        text (str): The input string.

    Returns:
        list: A list of unique words.

    Example:
        >>> unique_words("Hello hello world")
        ['hello', 'world']
    """
    words = text.lower().split()
    return list(dict.fromkeys(words))