from pystringtoolkit.counting import char_frequency, most_common_char, word_count, unique_words

def test_char_frequency():
    assert char_frequency("banana") == {"b": 1, "a": 3, "n": 2}

def test_most_common_char():
    assert most_common_char("banana") == "a"

def test_word_count():
    assert word_count("Hello hello world") == {"hello": 2, "world": 1}

def test_unique_words():
    assert unique_words("Hello hello world") == ["hello", "world"]
