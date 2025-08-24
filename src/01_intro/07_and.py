# Example of using 'and' in a conditional expression
#
# AND truth table (all 4 combinations):
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

age = 25
is_working_age = age >= 18 and age < 65  # True and True
print(is_working_age)

age = 25  # could be int(input("Enter your age: "))

result = age > 18 and age < 65  # True and True
print(result)  # True

# --

age = 25

result = age < 18 and age > 65  # False and False
print(result)  # False

# --

age = 25

result = age < 18 and age < 65  # False and True
print(result)  # False

# --

age = 25

result = age < 18 and age < 65  # False and ??? doesn't matter
print(result)  # False

# --

