
### Slicing a list: friends[start:end]

friends = ["Rolf", "Anne", "Charlie", "Bob", "Jen"]

print(friends[1:4]) # New list from index 1 to 3, ['Anne', 'Charlie', 'Bob']
print(friends[:3]) # New list from start to index 2, ['Rolf', 'Anne', 'Charlie']
print(friends[2:]) # New list from index 2 to end, ['Charlie', 'Bob', 'Jen']
print(friends[-3:]) # New list from the end, counting backwards ['Charlie', 'Bob', 'Jen']
print(friends[:-3]) # New list from start to index -3 (3 from the end), ['Rolf', 'Anne']
print(friends[:]) # New list, copy of the original list ['Rolf', 'Anne', 'Charlie', 'Bob', 'Jen']


