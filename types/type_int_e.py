"""
* Assignment: Type Int Time
* Required: yes
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Calculate how many seconds is one day (24 hours)
    2. Calculate how many minutes is one week (7 days)
    3. Calculate how many hours is in one month (31 days)
    4. Calculate how many seconds is work day (8 hours)
    5. Calculate how many minutes is work week (5 work days)
    6. Calculate how many hours is work month (22 work days)
    7. In Calculations use floordiv (`//`)
    8. Run doctests - all must succeed

Polish:
    1. Oblicz ile sekund to jedna doba (24 godziny)
    2. Oblicz ile minut to jeden tydzień (7 dni)
    3. Oblicz ile godzin to jeden miesiąc (31 dni)
    4. Oblicz ile sekund to dzień pracy (8 godzin)
    5. Oblicz ile minut to tydzień pracy (5 dni pracy)
    6. Oblicz ile godzin to miesiąc pracy (22 dni pracy)
    7. W obliczeniach użyj floordiv (`//`)
    8. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert day is not Ellipsis, \
    'Assign result to variable: `day`'
    >>> assert week is not Ellipsis, \
    'Assign result to variable: `week`'
    >>> assert month is not Ellipsis, \
    'Assign result to variable: `month`'
    >>> assert workday is not Ellipsis, \
    'Assign result to variable: `workday`'
    >>> assert workweek is not Ellipsis, \
    'Assign result to variable: `workweek`'
    >>> assert workmonth is not Ellipsis, \
    'Assign result to variable: `workmonth`'
    >>> assert type(day) is int, \
    'Variable `day` has invalid type, should be int'
    >>> assert type(week) is int, \
    'Variable `week` has invalid type, should be int'
    >>> assert type(month) is int, \
    'Variable `month` has invalid type, should be int'
    >>> assert type(workday) is int, \
    'Variable `workday` has invalid type, should be int'
    >>> assert type(workweek) is int, \
    'Variable `workweek` has invalid type, should be int'
    >>> assert type(workmonth) is int, \
    'Variable `workmonth` has invalid type, should be int'

    >>> day
    86400
    >>> week
    10080
    >>> month
    744
    >>> workday
    28800
    >>> workweek
    2400
    >>> workmonth
    176
"""

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

# 1 day in seconds
# type: int
day = 1*DAY // SECOND

# 7 days in minutes
# type: int
week = 7*DAY // MINUTE

# 31 days in hours
# type: int
month = 31*DAY // HOUR

# 8 hours in seconds
# type: int
workday = 8*HOUR // SECOND

# 5 workdays in minutes
# type: int
workweek = 5*workday // MINUTE

# 22 workdays in hours
# type: int
workmonth = 22 * HOUR * 8 // HOUR

