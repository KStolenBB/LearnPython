"""NameError
Demonstration script triggering a NameError by referencing a variable name
that has not been defined in the current scope.

NameError is raised when Python cannot find a variable (identifier) in local,
enclosing, global, or built-in namespaces.
"""

# This will raise: NameError: name 'undefined_variable' is not defined
print(undefined_variable)  # noqa: F821
