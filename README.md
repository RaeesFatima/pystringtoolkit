# PyStringToolkit

[![PyPI version](https://badge.fury.io/py/pystringtoolkit.svg)](https://pypi.org/project/pystringtoolkit/)
[![Downloads](https://static.pepy.tech/badge/pystringtoolkit)](https://pepy.tech/project/pystringtoolkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PyStringToolkit** is a lightweight and intuitive Python library offering a rich set of utilities for string manipulation and transformation. Whether you're building web applications, preprocessing text for machine learning, or just want cleaner and more readable code — this toolkit simplifies the process with clean and reusable functions.

---

## ✨ Key Features

### 🔠 Case Conversion Utilities
Transform strings between common naming conventions:

- `to_snake_case()` → Converts text to `snake_case`
- `to_camel_case()` → Converts text to `camelCase`
- `to_pascal_case()` → Converts text to `PascalCase`
- `to_kebab_case()` → Converts text to `kebab-case`
- `to_upper_case()` → Converts all letters to uppercase
- `to_lower_case()` → Converts all letters to lowercase
- `to_title_case()` → Capitalizes the first letter of each word
- `to_alternating_case()` →  alternates uppercase and lowercase characters in a string
### 🧹 Text Cleaning Functions
Remove unwanted characters and normalize formatting:

- `remove_punctuation()` → Strips punctuation, preserving only letters and digits
- `remove_whitespaces()` → Removes all whitespaces from the string
- `remove_extra_spaces()` → Reduces multiple spaces to a single space
- `truncate(length)` → Cuts off text after a specified length, adding ellipsis
- `contains_only_alpha()` → Checks if the string contains only alphabetic characters

### 🔧 String Generation Tools
Helpful tools for generating and formatting text:

- `slugify()` → Converts text into URL-friendly slugs (`"Hello World!" → "hello-world"`)
- `random_string(length)` → Generates a random alphanumeric string of a given length

### 📧 Email Validation
The `is_email()` → function validates if a string is a properly formatted email address

---

## 📦 Installation  

Install the latest version via pip:

```bash
pip install pystringtoolkit
```
## Example
```python
from pystringutils import to_snake_case

print(to_snake_case("Hello World!"))  # hello_world
```
## Contribution guide
 You can find the contribution guide here to contribute in this project.
[Contribution Guide](CONTRIBUTING.md) 
Thanks

## Documentation

Full documentation is available here 👉 [PyStringToolkit Docs](https://pystringtoolkit-documentation.readthedocs.io/en/latest/)

The docs include:
- Installation guide
- Usage patterns & best practices

## Contributors

We value our contributors!  

All the people who help improve **PyStringToolkit** are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md).  

A huge thanks to everyone — whether it’s code, docs, tests, or ideas 🙌

