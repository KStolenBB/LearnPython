friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
else:
    print(f"Hello, stranger!")    

friends = ["Rolf", "Sam", "Alex"]
family = ["Mom", "Dad", "Sister"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family member!")
else:
    print("Hello, stranger!")

