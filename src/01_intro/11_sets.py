 # Initialize art friends set and add a new member
art_friends = {"Rolf", "Bob", "Charlie"}
art_friends.add("Diana")
print(art_friends)

 # Initialize science friends set, add a member, then remove one
science_friends = {"Alice", "Bob", "Charlie"}
science_friends.add("Diana")
print(science_friends)
science_friends.remove("Alice")
print(science_friends)


 # Reset sets for demonstrating set operations
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

 # Elements in art_friends but not in science_friends
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

 # Elements present in exactly one of the sets
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

 # Elements common to both sets
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

 # All unique elements from both sets
all_friends = art_friends.union(science_friends)
print(all_friends)

user_friends = set()  # This is an empty set, like {}


## Long example
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend = input("Enter the name of a friend: ")

# Add the name to the empty set
user_friends.add(friend)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
nearby_friends = user_friends.intersection(nearby_people)
print(nearby_friends)
