# Example of using 'or' in a conditional expression
#
# OR truth table (all 4 combinations):
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False

age = 25

result = age > 18 or age < 65  # True and ??? doesn't matter
print(result)  # True

# --

bool(0)  # False, zero
bool(13)  # True

bool("")  # False, empty string
bool("Hello")  # True

bool([])  # False, empty list
bool([1, 3, 5])  # True

# --

default_age = 30
age = 0

user_age = age or default_age
print(user_age)  # 30

# --

default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting
print(f"Hello, {user_name}!")

