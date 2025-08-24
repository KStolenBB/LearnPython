grades = [85, 90, 78, 92, 88]

# Calculate the total sum of grades
total = sum(grades)
print("Total:", total)

# Calculate the number of grades
count = len(grades)
print("Count:", count)

# Calculate the average
average = total / count
print("Average:", average)


############################################################

lottery_numbers = {13, 21, 22, 5, 8}


#Define a list with two players (you can come up with their names and numbers).

players = [
    {
        'name': 'Synne',
        'numbers': {13, 22, 23, 24, 25}
    },
    {
        'name': 'Alexander',
        'numbers': {13, 24, 31, 41, 15}
    }    
]

#For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
#Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
#You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
#Then construct a string and print it out.

player0right = lottery_numbers.intersection(players[0]["numbers"])
print(f'Player {players[0]["name"]} got {len(player0right)} numbers right.')

player1right = lottery_numbers.intersection(players[1]["numbers"])
print(f'Player {players[1]["name"]} got {len(player1right)} numbers right.')

