"""
* Assignment: Loop For Count
* Required: yes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Count occurrences of each color
    2.
    3. Run doctests - all must succeed

Polish:
    1. Zlicz wystąpienia każdego z kolorów
    2. Nie używaj `list.count()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(red)
    <class 'int'>
    >>> type(green)
    <class 'int'>
    >>> type(blue)
    <class 'int'>
    >>> red
    3
    >>> green
    2
    >>> blue
    2
"""

DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

# Number of 'red' elements in DATA
# type: int
red = 0
for color in DATA:
    if color == 'red':
        red += 1

# Number of 'green' elements in DATA
# type: int
green = 0
for color in DATA:
    if color == 'green':
        green += 1

# Number of 'blue' elements in DATA
# type: int
blue = 0
for color in DATA:
    if color == 'blue':
        blue += 1

