"""NotImplementedError
Demonstration of NotImplementedError by defining a base class method that is
intended to be overridden but is called directly instead.

NotImplementedError is typically raised in abstract methods to indicate that
subclasses must provide an implementation.
"""

class Shape:
    def area(self):  # pragma: no cover - simple demo
        """Return the area of the shape (must be implemented by subclasses)."""
        raise NotImplementedError("Subclasses must implement 'area'.")


# Calling the abstract-like method directly triggers the exception.
Shape().area()
