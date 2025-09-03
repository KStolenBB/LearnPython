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
