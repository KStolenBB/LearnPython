"""ValueError
Demonstration of a ValueError by converting an invalid string to int.

ValueError is raised when a function receives an argument of the right type but
an inappropriate value.
"""

invalid_number = "abc"
print(int(invalid_number))  # Raises: ValueError: invalid literal for int() with base 10: 'abc'
