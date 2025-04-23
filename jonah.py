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
