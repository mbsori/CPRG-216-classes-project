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
        success, movies = load_movies(file_name)
        if not success:
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