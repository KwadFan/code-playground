# This folder contains python script to learn about basics

## Resources

I try to learn python in a self thought manner, so making bad decision might occure but as normal behaviour for humans, we learn from errors we made in the past. So, what resources I will use?
For now a Video from freecodecamp.org -> https://youtu.be/nLRL_NcnK-4
and https://www.w3schools.com/python/python_intro.asp

Also I use a printed media aka book :P named

[Python - Der Grundkurs](https://www.rheinwerk-verlag.de/python-der-grundkurs/)

As you you can guess it is written in my native language, german.

## helloworld.py

A basic structure that any python script should contain according to
https://docs.python.org/3/tutorial/interpreter.html#source-code-encoding
and
https://realpython.com/if-name-main-python/

The main() function might be personal preference but I think its the way to go.

## Python Style Guide or the Zen of Python

This is a cute easteregg in the python interpreter, which describes in a few
sentences the Zen of python.

```python
import this
```

A brief overview, that I found really useful, is
[RealPython - python-pep8](https://realpython.com/python-pep8/)
to read about the fullblown Styleguide head over to
[PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

Summarized to some basics:

-   Use [UTF-8](https://en.wikipedia.org/wiki/UTF-8) for character encoding, this is pythons default but can be manipulated by

```python
# -*- coding: <charset> -*-
```

-   Use 4 spaces for indentation. Don't mix Tabs and spaces.
-   Use LF line endings (`\n`) instead CRLF (as used in Windows - `\r\n`).
-   Limit line length for code to 79 characters.
    -   If your or your team wants to increase used line length
        limit those to 99 characters
-   Use a limit of 72 characters for docstrings and/or comments
-   Surround top-level functions and classes by two blank lines
-   Surround methods inside classes by a single blank line
-   Don't use noisy unicode characters

## Naming conventions

Instead of typing it down here, head over to
[RealPython - Naming Conventions](https://realpython.com/python-pep8/#naming-conventions)
