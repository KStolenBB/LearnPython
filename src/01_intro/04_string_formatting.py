## String formatting

# You can add strings together to concatenate them (join them together).

name = "Jose"
greeting = "Hello, " + name

print(greeting)

# You can also use f-strings if you are using Python 3.6 or later.
# f-strings don't work in Python 3.5 or earlier.
# In f-strings, {name} gets replaced by the value of the variable name.

another_greeting = f"How are you, {name}?"
print(another_greeting)

# It's also possible to use the format method.
# We've not looked at methods yet, but it works this way:

final_greeting = "How are you, {}?".format(name)
print(final_greeting)

# The {} are replacement fields. Each empty pair is replaced (left to right)
# by the corresponding positional argument you pass to .format().
# You can also number them {0}, {1} or give them names {user}, mixing is allowed
# but generally you pick one style for clarity.

# Multiple placeholders (positional):
multi_greeting = "Hello {}, you have {} new messages.".format(name, 5)
print(multi_greeting)

# Numbered placeholders (useful if you want to re-order):
reordered = "{1} comes after {0}".format("first", "second")
print(reordered)


# You can also give names to variables inside a formattable string:
friend_name = "Rolf"
goodbye = "Goodbye, {name}!"
goodbye_rolf = goodbye.format(name=friend_name)
print(goodbye_rolf)


# Another example of using `.format()` on a variable:
greeting = "How are you, {}?"
print(greeting.format(name))

# Usually you will be using f-strings, just because they are shorter and more readable.
# However sometimes you may need to re-use a format string, and that is when using .format() is useful.

# Decimals:
pi = 3.14159
print("The value of pi is approximately {:.2f}.".format(pi))

# The same format specifiers work in f-strings:
print(f"The value of pi is approximately {pi:.2f}.")

# For many concatenations in a loop, prefer building a list and then '\n'.join(parts)
# instead of using + repeatedly (efficiency & readability). f-strings are usually
# the most concise when you format values inline.
