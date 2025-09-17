"""IndentationError
Demonstration of an IndentationError using dynamic execution.

IndentationError occurs when the indentation of code is incorrect, such as a
missing indent inside a function body or inconsistent indentation structure.
"""

bad_indentation = "def greet():\nprint('Hello')"  # Body not indented

# Direct invalid example (commented):
# def greet():
# print("Hello")

exec(bad_indentation)  # Raises: IndentationError
