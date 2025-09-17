"""ImportError
Demonstration of an ImportError by attempting to import a non-existent symbol
from a standard library module.

ImportError is raised when the import statement cannot find the module or name.
"""

# Attempting to import a name that does not exist in the math module.
from math import definitely_not_there  # type: ignore[attr-defined]

print(definitely_not_there)
