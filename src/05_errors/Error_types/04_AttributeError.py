"""AttributeError
Demonstration of an AttributeError by trying to access an attribute or method
that an object does not have.

AttributeError is raised when the attribute reference or assignment fails.
"""

number = 42

# int objects do not have an 'append' method; lists do.
# This will raise: AttributeError: 'int' object has no attribute 'append'
number.append(5)  # type: ignore[attr-defined]
