from pystringtoolkit.cleaners import remove_vowels, remove_consonants

def test_remove_vowels():
    assert remove_vowels("Hello World") == "Hll Wrld"

def test_remove_consonants():
    assert remove_consonants("Hello World") == "eo o"
