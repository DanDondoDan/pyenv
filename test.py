

from pyenv import ENV
import os

""" Make sure you do this in Bash before running this script.

export MY_BOOL_VALUE=True
export MY_FLOAT_VAR=3.14
export MY_STRING=megusta123.13
export MY_INTEGER=100500
"""

for var in ('MY_BOOL_VALUE',
            'MY_FLOAT_VAR',
            'MY_STRING',
            'MY_INTEGER',
            'SOME_UNKNOWN_VAR'):
    value = getattr(ENV, var)
    print(value, type(value))


print(os.environ())
