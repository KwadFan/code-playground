#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basics

# This is a single line comment

"""This is a
multiline
comment or
as called in python 'docstrings' defined in PEP 257.
"""

"""This is a oneline docstring"""

# Code style guide
"""Python uses, if not defined by '# -*- coding: utf-8 -*-', UTF-8 as coding.
To get a deeper insight in how to style your python scripts/programs
head over to https://peps.python.org/pep-0008/
PEP-8 is the official style guide.

A short introduction in some basics:
- use UTF-8 for encoding
- use 4 spaces for indentation
- use LF line endings
- use two blank lines around top-level functions and classes
- use single blank line for methods inside classes
- limit line length to 79 characters
- Avoid using noisy unicode characters
"""


# Variables
"""Variables in python are dynamically typed,
this means type of a variable can change during runtime.
Other than statically typed languages, where the type has to be defined
in the beginning.
"""

# The main function will be only executed if the script is not imported
def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
