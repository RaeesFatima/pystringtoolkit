from pystringtoolkit import (to_snake_case, to_upper_case, to_lower_case,
                             to_kebab_case, to_pascal_case, to_camel_case, to_title_case, remove_punctuation,
                             remove_whitespaces, remove_extra_spaces, truncate, contains_only_alpha, slugify, random_string,
                             to_alternating_case)

#cases
def test_to_snake_case():
    assert to_snake_case("Hello World!") == "hello_world_"

def test_to_upper_case():
    assert to_upper_case("Hello World!") == "HELLO WORLD!"

def test_to_lower_case():
    assert to_lower_case("Raees fatima") == "raees Fatima"

def test_to_kebab_case():
    assert to_kebab_case("Raees fatima") == "raees-fatima"

def test_to_pascal_case():
    assert to_pascal_case("raees fatima") == "RaeesFatima"

def test_to_camel_case():
    assert to_camel_case("raees fatima") == "raeesFatima"

def test_to_title_case():
    assert to_title_case("raees fatima") == "Raees Fatima"

#cleaners
def test_remove_punctuation():
    assert remove_punctuation("raees, fatima!") == "raees fatima"

def test_remove_whitespaces():
    assert remove_whitespaces("raees\t  fatima\n") == "raeesfatima"

def test_remove_extra_spaces():
    assert remove_extra_spaces("raees fatima   ") == "raees fatima"

def test_truncate():
    assert truncate("this is a test",4) == "this..."

def test_contains_only_alpha():
    assert not contains_only_alpha("this123")

#generators
def test_slugify():
    assert slugify("hello world") == "hello-world"

def test_random_string():
    print(random_string(10))
    assert random_string(10)

def test_alternating_case():
    print(to_alternating_case("hello"))
    assert to_alternating_case("hello") == "HeLlO"
