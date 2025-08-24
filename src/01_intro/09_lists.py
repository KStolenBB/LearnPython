friend1 = "Alice"
friend2 = "Bob"
friend3 = "Charlie"
friends = [friend1, friend2, friend3]
print(friends)

friends = ["Ivy", "Jack", "Karen"]
print(friends)

friends = [["Alice", 24], ["Bob", 30], ["Charlie", 22], ["Diana", 27], ["Ethan", 29], ["Fiona", 25]]

friends = [
    ["Alice", 24],
    ["Bob", 30],
    ["Charlie", 22],
    ["Diana", 27],
    ["Ethan", 29],
    ["Fiona", 25],
]


print(f"{friends[0][0]} is {friends[0][1]} years old")


print(friends[1][1])

friends.append(["George", 31])
friends.append(["Hannah", 28])

print(friends)
print(f"{friends[0][0]} is {friends[0][1]} years old")
friends.pop(0)
print(f"{friends[0][0]} is {friends[0][1]} years old")
friends.remove(["Bob", 30])
print(f"{friends[0][0]} is {friends[0][1]} years old")
print(friends)

friends = ["Ivy", "Jack", "Karen"]
comma_separated = ", ".join(friends)
print(f"My friends: {comma_separated}")
