from pystringtoolkit.cleaners import remove_vowels, remove_consonants,strip_html_tags

def test_remove_vowels():
    assert remove_vowels("Hello World") == "Hll Wrld"

def test_remove_consonants():
    assert remove_consonants("Hello World") == "eo o"

def test_strip_html_tags():
    assert strip_html_tags("<p>Hello</p> World") == "Hello World"
    assert strip_html_tags("<b>Bold</b>") == "Bold"
    assert strip_html_tags("No HTML here") == "No HTML here"
    assert strip_html_tags("<div><span>Nested</span></div>") == "Nested"
    

