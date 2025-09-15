# Initial dictionary mapping friend names to ages
friend_ages = {
    "Rolf": 25,
    "Bob": 30,
    "Charlie": 22
}


print(friend_ages["Rolf"])

# Update existing entry and add a new friend
friend_ages["Rolf"] = 26
friend_ages["Peter"] = 45


# Tuple of dictionaries, each representing a friend record
friends = (
    {"name": "Rolf Smith", "age": 26},
    {"name": "Bob Johnson", "age": 30},
    {"name": "Charlie Brown", "age": 22}
)

print(friends[0]["name"])
print(friends[1]["name"])


# Recreate data as list of (name, age) tuples
friends = [("Rolf Smith", 26), ("Bob Johnson", 30), ("Charlie Brown", 22)]
# Convert list of tuples into a dictionary
friend_ages = dict(friends)
print(friend_ages)

###

friends = [("Rolf", 25), ("Sam", 30), ("Alex", 28)]

for friend in friends:
    name = friend[0]
    age = friend[1]
    print(f"Hello, {name}! You are {age} years old.")    

for friend in friends:
    name, age = friend
    print(f"Hello, {name}! You are {age} years old.")    

for name, age in friends:    
    print(f"Hello, {name}! You are {age} years old.")
    

####

cars = {"ok", "ok", "ok", "ok", "faulty", "ok", "ok"}

for car in cars:
    if car == "faulty":
        print("Found a faulty car!")
        break
    print(f" is {car}")