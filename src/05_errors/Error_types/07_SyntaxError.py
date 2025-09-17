"""SyntaxError
Demonstration of a SyntaxError using dynamic execution.

We cannot leave invalid Python syntax directly in this file because it would
prevent the file from being imported or executed normally. Instead we place the
invalid code in a string and execute it with exec() to trigger the SyntaxError.

Typical causes: missing colons, unmatched parentheses, incorrect keywords.
"""


# 1. Missing colon after an if statement

if True
    print("Hello")

# Error: SyntaxError: expected ':'

# 2. Unmatched parenthesis

print("Hi"

# Error: SyntaxError: '(' was never closed

# 3. Mixing tabs and spaces in an indented block (can also become an IndentationError, but often reported as a syntax issue)

def greet():
   	print("Hello")  # (Assume this line starts with a tab)
    print("World")  # (Assume this line starts with 4 spaces)

# Depending on environment: TabError: inconsistent use of tabs and spaces in indentation

# 4. Using a reserved keyword as a variable name

class = "something"

# Error: SyntaxError: invalid syntax (because 'class' is reserved)

# 5. Improper assignment target

5 = x

# Error: SyntaxError: cannot assign to literal

# 6. Duplicate parameter name in function definition

def add(x, x):
    return x + x

# Error: SyntaxError: duplicate argument 'x' in function definition

# 7. Bad f-string expression (unterminated brace)

name = "Ada"
print(f"Hello {name")

# Error: SyntaxError: f-string: expecting '}'

# 8. Using continue outside a loop

def something():
    continue

# Error: SyntaxError: 'continue' not properly in loop

# 9. Incorrect indentation starting a file with an indented line

    print("Starts with indentation")

# Error: IndentationError (a form of syntax error): unexpected indent
