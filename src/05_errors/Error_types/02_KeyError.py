"""KeyError
Demonstration script triggering a KeyError by attempting to access a dictionary
entry with a key that does not exist.

KeyError is raised when a mapping (like dict) is accessed with a key that isn't
present. Valid keys are the ones that currently exist in the dictionary.
"""

person = {"name": "Ada", "language": "Python"}

# This will raise: KeyError: 'age' because 'age' is not a key in the dict.
print(person["age"])  # noqa: F821
