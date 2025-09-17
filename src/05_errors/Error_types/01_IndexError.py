#IndexError
"""
Demonstration script triggering an IndexError by attempting to access a list element
at an index that does not exist.

An IndexError in Python is raised when you use an invalid index on a sequence
(e.g., list, tuple, string). This happens here because the code tries to access
numbers[5] while the list has only three elements (valid indices: 0–2).
"""
numbers = [1, 2, 3]
print(numbers[5])

