import os
from movie import Movie, print_genres
 
GENRES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance",
          "Thriller", "Animation", "Documentary", "Fantasy"]
 
SEPARATOR = "-" * 104
 
def load_movies(file_name):
    movies = []
    file = open(file_name, "r")
    count = 0
    for line in file:
        parts = line.strip().split(",")
        if len(parts) >= 7:
            movie = Movie(
                int(parts[0]), parts[1], parts[2], int(parts[3]),
                parts[4].lower() == "true", float(parts[5]), int(parts[6])
            )
            movies.append(movie)
            count += 1
    file.close()
    return True, movies
 
 
def save_movies(file_name, movies):
    file = open(file_name, "w")
    count = 0
    for movie in movies:
        file.write(f"{movie.get_id()},{movie.get_title()},{movie.get_director()},"
                   f"{movie.get_genre()},{str(movie.get_availability() == 'Available')},"
                   f"{movie.get_price()},{movie.get_rental_count()}\n")
        count += 1
    file.close()
    return count
 
 
def print_menu():
    print("\nMovie Library - Main Menu")
    print("=========================")
    print(" 1) Search for movies")
    print(" 2) Rent a movie")
    print(" 3) Return a movie")
    print(" 4) Add a movie")
    print(" 5) Remove a movie")
    print(" 6) Update movie details")
    print(" 7) List movies by genre")
    print(" 8) Find popular movies")
    print(" 9) Check availability by genre")
    print("10) Display library summary")
    print(" 0) Exit the system")
    return input("Enter your selection: ").strip()
 
 
def get_genre():
    print()
    for i in range(len(GENRES)):
        print("    " + str(i) + ") " + GENRES[i])
    genre_input = input("    Choose genre(0-9): ")
    while not genre_input.isdigit() or int(genre_input) < 0 or int(genre_input) > 9:
        print("Invalid Genre: Enter a valid genre (0-9)")
        genre_input = input("    Choose genre(0-9): ")
    return int(genre_input)
 
 
def print_movies(movies):
    print("\nID        Title                         Director                 Genre           Availability     Price   # Rentals")
    print("---------------------------------------------------------------------------------------------------------------------")
    for movie in movies:
        print(movie)
 
 
def find_movie_by_id(movies, movie_id):
    for movie in movies:
        if movie.get_id() == movie_id:
            return movie
    return None
 
 
def search_movies(movies, search_term):
    found = []
    lower_term = search_term.lower()
    for movie in movies:
        if (lower_term in movie.get_title().lower()
            or lower_term in movie.get_director().lower()
            or lower_term in movie.get_genre_name().lower()):
            found.append(movie)
    if not found:
        print("No matching movies found.")
    else:
        print_movies(found)
def rent_movie(movies, movie_id):
    """
    Rent a movie by its ID if it is available.
 
    Parameters:
    movies (list): A list of Movie objects.
    movie_id (str): The ID of the movie to rent.
 
    Returns:
    str: A string indicating the result of the rental attempt.
    """
    movie = find_movie_by_id(movies, movie_id)
    if movie is None:
        return f"\nMovie with ID {movie_id} not found in library."
    if movie.borrow_movie():
        return f"\n'{movie.get_title()}' rented successfully."
    else:
        return f"\n'{movie.get_title()}' is already rented - cannot be rented again."
 
 
def return_movie(movies, movie_id):
    """
    Return a rented movie by its ID.
 
    Parameters:
    movies (list): A list of Movie objects.
    movie_id (str): The ID of the movie to return.
 
    Returns:
    str: A string indicating the result of the return attempt.
    """
    movie = find_movie_by_id(movies, movie_id)
    if movie is None:
        return f"\nMovie with ID {movie_id} not found in library."
    if movie.return_movie():
        return f"\n'{movie.get_title()}' was returned successfully."
    else:
        return f"\n'{movie.get_title()}' was not rented - cannot be returned."
 
 
def add_movie(movies):
    """
    Add a new movie to the library.
 
    Parameters:
    movies (list): A list of Movie objects.
 
    Returns:
    str: A string indicating the result of the add attempt.
    """
    id_ = input("Enter movie ID: ")
    if find_movie_by_id(movies, id_):
        return f"Movie with ID {id_} already exists - cannot be added to library."
    title = input("Enter title: ")
    director = input("Enter director: ")
    print_genres()
    genre = int(input("Choose genre(0-9): "))
    price = float(input("Enter price: "))
    movies.append(Movie(id_, title, director, genre, True, price, 0))
    return f"Movie '{title}' added to library successfully."
 
 
def remove_movie(movies):
    """
    Remove a movie from the library by its ID.
 
    Parameters:
    movies (list): A list of Movie objects.
 
    Returns:
    str: A string indicating the result of the remove attempt.
    """
    id = input("Enter the movie ID to remove: ")
    movie = find_movie_by_id(movies, id)
    if movie:
        movies.remove(movie)
        return f"\nMovie '{movie.get_title()}' has been removed from library successfully."
    return f"\nMovie with ID {id} not found in library - cannot be removed."
 
 
def update_movie_details(movies):
    """
    Update the details of a movie by its ID.
 
    Parameters:
    movies (list): A list of Movie objects.
 
    Returns:
    str: A string indicating the result of the update attempt.
    """
    id = input("Enter the movie ID to update: ")
    movie = find_movie_by_id(movies, id)
    if movie is None:
        return f"Movie with ID {id} not found in library."
 
    print("Leave fields blank to keep current values.")
    title = input(f"Enter new title (current: {movie.get_title()}): ") or movie.get_title()
    director = input(f"Enter new director (current: {movie.get_director()}): ") or movie.get_director()
    genre_input = input(f"Enter new genre (current: {movie.get_genre_name()}) (Yes/Y, No/N)? ").lower()
    if genre_input in ['no', 'n', 'NO', 'N']:
        genre = movie.get_genre()
    elif genre_input in ['yes', 'y', 'YES', 'Y']:
        print_genres()
        genre = int(input("Choose genre (0-9): "))
    else:
        genre = movie.get_genre()
    price_input = input(f"Enter new price (current: {movie.get_price()}): ")
    price = float(price_input) if price_input else movie.get_price()
 
    movie.set_title(title)
    movie.set_director(director)
    movie.set_genre(genre)
    movie.set_price(price)
 
    return f"Movie with ID {id} is updated successfully."
def list_movies_by_genre(movies):
    """
    List all movies of a specified genre.
 
    Parameters:
    movies (list): A list of Movie objects.
 
    Returns:
    None
    """
    genre = -1
    while genre < 0 or genre > 9:
        print_genres()
        genre_input = input("Choose genre (0-9): ")
        if genre_input.isdigit():
            genre = int(genre_input)
            if genre < 0 or genre > 9:
                print("\nInvalid Genre: Enter a valid genre (0-9)")
        else:
            print("\nInvalid Genre: Enter a valid genre (0-9)")
   
    genre_movies = []
    for movie in movies:
        if movie.get_genre() == genre:
            genre_movies.append(movie)
 
    if genre_movies:
        print(f"\n{'ID':<4} {'Title':<25} {'Director':<20} {'Genre':<10} {'Availability':<10} {'Price':>6} {'# Rentals':>12}")
        print(SEPARATOR)
        for movie in genre_movies:
            print(f"{movie.get_id():<4} {movie.get_title():<25} {movie.get_director():<20} {movie.get_genre_name():<10} {movie.get_availability():<10} {movie.get_price():>7} {movie.get_rental_count():>12}")
    else:
        print("No movies found for the selected genre.")
 
def check_availability_by_genre(movies):
    """
    Check and display the availability of movies in a specified genre.
 
    Parameters:
    movies (list): A list of Movie objects.
 
    Returns:
    None
    """
    print_genres()
    genre = int(input("\nChoose genre(0-9): "))
    available_movies = []
    for movie in movies:
        if movie.get_genre() == genre and movie.get_availability() == "Available":
            available_movies.append(movie)
   
    if available_movies:
        print(f"\n{'ID':<4} {'Title':<20} {'Director':<25} {'Genre':<15} {'Availability':<15} {'Price':<6} {'# Rentals':>12}")
        print(SEPARATOR)
        for movie in available_movies:
            print(f"{movie.get_id():<4} {movie.get_title():<20} {movie.get_director():<25} {movie.get_genre_name():<15} {movie.get_availability():<15} {movie.get_price():<6} {movie.get_rental_count():>10}")
    else:
        print("\nNo available movies in this genre.")
 
def display_library_summary(movies):
    """
    Display a summary of the library.
 
    Parameters:
    movies (list): A list of Movie objects.
 
    Returns:
    None
    """
    total_movies = len(movies)
    available_movies = 0
    rented_movies = 0
    for movie in movies:
        if movie.get_availability() == "Available":
            available_movies += 1
        else:
            rented_movies += 1
   
    print(f"{'\nTotal movies:':<20} {total_movies}")
    print(f"{'Available movies:':<19} {available_movies}")
    print(f"{'Rented movies:':<19} {rented_movies}")
 
def popular_movies(movies):
    """
    Displays all the movies that have a rental_count >= to the entered value.
   
    Parameters:
    - movies: A list of Movie objects.
   
    Return Value: None.
    """
    min_rental_count = input("Enter the minimum number of rentals for the movies you want to view: ")
   
    if not min_rental_count.isdigit():
        print("Invalid input. Please enter a valid number.")
        return
   
    min_rental_count = int(min_rental_count)
    popular_movies_list = []
 
    for movie in movies:
        if movie.get_rental_count() >= min_rental_count:
            popular_movies_list.append(movie)
 
    if not popular_movies_list:
        print(f"No movies found with a rental count of {min_rental_count} or more.")
    else:
        print(f"\nMovies Rented {min_rental_count} times or more")
        print(f"{'ID':<4} {'Title':<30} {'Director':<20} {'Genre':>15} {'# Rentals':>20}")
        print(SEPARATOR)
        for movie in popular_movies_list:
            print(f"{movie.get_id():<4} {movie.get_title():<30} {movie.get_director():<20} {movie.get_genre_name():>15} {movie.get_rental_count():>20}")
 
 
def main():
    """
    The main function that runs the Movie Library Management System.
    It loads movies from a file, displays the menu, and handles user interactions.
    """
 
    while True:
        file_name = input("Enter the movie catalog filename: ")
        if not os.path.isfile(file_name):
            print(f'The catalog file "{file_name}" is not found')
            continue_without_file = input("Do you want to continue without loading a file (Yes/Y, No/N))? ").lower()
            if continue_without_file in ['no', 'n']:
                print("The Movie Library System will not continue...")
                print("Movie Library System Closed Successfully")
                return
            else:
                print("The Movie Library System is opened without loading catalog")
                movies = []
                break
        else:
            success, movies = load_movies(file_name)
            print(f'The catalog file "{file_name}" successfully loaded {len(movies)} movies to the Movie Library System')
            break
 
    running = True
 
    while running:
        choice = print_menu()  # Call to print_menu function
 
        if choice == '0':
            update_catalog = input("Would you like to update the catalog (Yes/Y, No/N))? ").lower()
            if update_catalog in ['yes', 'y']:
                save_movies(file_name, movies)
                print(f"{len(movies)} movies have been written to Movie catalog.")
            print("Movie Library System Closed Successfully")
            running = False
        elif choice == '1':
            search_term = input("Enter search term: ")
            print(f'\nSearching for "{search_term}" in title, director, or genre...')
            search_movies(movies, search_term)
        elif choice == '2':
            movie_id = input("Enter the movie ID to rent: ")
            print(rent_movie(movies, movie_id))
        elif choice == '3':
            movie_id = input("Enter the movie ID to return: ")
            print(return_movie(movies, movie_id))
        elif choice == '4':
            print(add_movie(movies))
        elif choice == '5':
            print(remove_movie(movies))
        elif choice == '6':
            print(update_movie_details(movies))
        elif choice == '7':
            list_movies_by_genre(movies)
        elif choice == '8':
            popular_movies(movies)
        elif choice == '9':
            check_availability_by_genre(movies)
        elif choice == '10':
            display_library_summary(movies)
        else:
            print("Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main()