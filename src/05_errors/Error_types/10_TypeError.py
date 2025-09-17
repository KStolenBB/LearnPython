"""TypeError
Demonstration of a TypeError by performing an operation on incompatible types.

TypeError is raised when an operation or function is applied to an object of
an inappropriate type.
"""

# Adding an int and a str is not defined.
result = 5 + "7"  # Raises: TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(result)
