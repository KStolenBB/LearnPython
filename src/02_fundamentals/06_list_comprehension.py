numbers = [0, 1, 2, 3, 4]

###

doubled_numbers1 = []
for number in numbers:
    doubled_numbers1.append(number * 2)

print(doubled_numbers1) # [0, 2, 4, 6, 8]

### 

doubled_numbers2 = [number * 2 for number in numbers]
print(doubled_numbers2) # [0, 2, 4, 6, 8]

###

doubled_numbers3 = [number * 2 for number in numbers]
print(doubled_numbers3) # [0, 2, 4, 6, 8]

###

doubled_numbers4 = [number * 2 for number in range(5)]
print(doubled_numbers4) # [0, 2, 4, 6, 8]

###

doubled_numbers5 = [5 for number in range(5)]
print(doubled_numbers5) # [5, 5, 5, 5, 5]

###

doubled_numbers6 = [number + 5 for number in range(5)]
print(doubled_numbers6) # [5, 6, 7, 8, 9]

#######

friend_ages = [22, 31, 35, 37]
age_strings = [f"Your friend is {age} years old" for age in friend_ages]
print(age_strings) # ['Your friend is 22 years old', 'Your friend is 31 years old', 'Your friend is 35 years old', 'Your friend is 37 years old']

######

names = ["Rolf", "Bob", "Jen", "Anne", "Charlie"]
lowercase_names = [name.lower() for name in names]
print(lowercase_names) # ['rolf', 'bob', 'jen', 'anne', 'charlie']

######

friends = ["Rolf", "Bob", "Jen", "Anne", "Charlie"]
friend = input("Enter a name: ")
if friend.lower() in [name.lower() for name in friends]:
    print(f"{friend.title()} is one of your friends!")
else:
    print(f"{friend.title()} is not one of your friends.")

############



ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
even = [age for age in ages if age % 2 == 0]
print(odds)  # [35, 27, 21]
print(even)  # [22, 20]

#####

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# Using set intersection
friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])
print(friends_lower.intersection(guests_lower))

# Using list comprehension
friends_lower = [f.lower() for f in friends]
guests_lower = [g.lower() for g in guests]
common = [name for name in friends_lower if name in guests_lower]
print(common)  # ['rolf', 'charlie']

# Using list comprehension
present_friends = [
    name.title() for name in guests if name.lower() in [f.lower() for f in friends]
]
print(present_friends)  # ['Rolf', 'Charlie']

# Using list comprehension
friends_lower = [f.lower() for f in friends]
present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)  # ['Rolf', 'Charlie']

###############



friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# Using set intersection (via list)
friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])
print(friends_lower.intersection(guests_lower))

# Using set intersection directly
friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}
print(friends_lower.intersection(guests_lower))

# Create a new set with the names of present friends, properly capitalized
present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print(present_friends)

# Easier to read
present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}
print(present_friends)

###################

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i] 
    for i in range(len(friends))    
}
print(long_timers) # {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 11}

#

long_timers = {
    friends[i]: time_since_seen[i] 
    for i in range(len(friends))    
    if time_since_seen[i] > 5
}
print(long_timers) # {'Bob': 7, 'Jen': 15, 'Anne': 11}


######

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends, time_since_seen))

print(long_timers) # {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 11}

#
long_timers = list(zip(friends, time_since_seen))
print(long_timers)

#
long_timers = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))
print(long_timers) # {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 11}

#
long_timers = list(zip(range(15), friends, time_since_seen))
print(long_timers) # {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 11}


###

friends = ["Rolf", "Bob", "Jen", "Anne"]
counter = 0

for friend in friends:
    print(counter, friend)
    counter += 1

#
for counter, friend in enumerate(friends):
    print(counter, friend)

#    
friends_list = list(enumerate(friends))
print(friends_list)

#
friends_list = list(zip(range(1, 40), friends))
print(friends_list)

#
for counter, friend in enumerate(friends, start=1):
    print(counter, friend)

#
friends_list = list(enumerate(friends, start=1))
print(friends_list)
