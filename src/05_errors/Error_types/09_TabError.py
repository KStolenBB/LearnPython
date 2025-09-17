"""TabError
Demonstration of a TabError using dynamic execution.

TabError is a subclass of IndentationError raised when indentation contains
inconsistent use of tabs and spaces in Python 3.
"""

# Mixing a tab and spaces in the same block deliberately. The second line has a tab, the third has spaces.
mixed_indentation_code = "def mixed():\n\tprint('tab indented')\n    print('space indented')"  # noqa: W191

# Commented invalid example:
# def mixed():
# \tprint('tab indented')
#     print('space indented')

exec(mixed_indentation_code)  # Raises: TabError (or IndentationError depending on environment)
