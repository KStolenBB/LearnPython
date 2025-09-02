friends = ["Rolf", "Sam", "Alex"]

for friend in friends:
    print(friend)


elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for element in elements:
    print(element)



elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in elements:
    print("Hello, World!")


for _ in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Hello, Sandnes!")

for _ in range(10):
    print("Hello, Stavanger!")
    

for i in range(5, 10):
    print(f"Hello, {i}")
    

for i in range(50, 100, 5):
    print(f"Hello, X{i}")
    

students = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 22},
    {"name": "Jim", "age": 21}
]

for student in students:
    print(f"Hello, {student['name']}! You are {student['age']} years old.")


#####

cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for car in cars:
    if car == "faulty":
        print("Found a faulty car!")
        break
    print(f"{car} is fine.")



#####

cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for car in cars:
    if car == "faulty":
        print("Found a faulty car, skipping...")
        continue
    print(f"This car is {car}.")
    print("Shipping new car to customer!")

#####



cars = ["ok", "ok", "ok", "ok", "ok", "ok", "ok"]

for car in cars:
    if car == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {car}.")
    print("Shipping new car to customer!")
else:
    print("All cars are fine!")

#####


cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for car in cars:
    if car == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {car}.")
    print("Shipping new car to customer!")
else:
    print("All cars are fine!")

#####

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

for name, days in my_friends.items():
    print(f"{name} has been my friend for {days} years.")


####

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}
 
do_i_know = 'Anne'
 
if do_i_know in my_friends:
  print(f'I know {do_i_know}')  


# Find prime numbers

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

