MENU_PROMPT = "\nEnter: \n'a' to add a movie, \n'l' to see your movies, \n'f' to find a movie by title, or \n'q' to quit: \nYour choice: "
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

    print(f"Movie '{title}' added successfully!")

def list_movies():
    if not movies:
        print("No movies in your collection.")
        return

    for movie in movies:
        print(f"{movie['title']} (Director: {movie['director']}, Year: {movie['year']})")

def find_movie():
    search_title = input("Enter the movie title to search for: ")
    found_movies = [movie for movie in movies if movie['title'].lower() == search_title.lower()]

    if found_movies:
        for movie in found_movies:
            print(f"Found: {movie['title']} (Director: {movie['director']}, Year: {movie['year']})")
    else:
        print(f"No movie found with the title '{search_title}'.")


def menu():    
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movie()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
