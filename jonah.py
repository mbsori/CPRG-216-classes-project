def rent_movie(movies, movie_id):
    m = find_movie_by_id(movies, movie_id)
    if m is None:
        return f"Movie with ID {movie_id} not found in library."
    if m.borrow_movie():
        return f"'{m.get_title()}' rented successfully."
    else:
        return f"'{m.get_title()}' is already rented - cannot be rented again."


def return_movie(movies, movie_id):
    m = find_movie_by_id(movies, movie_id)
    if m is None:
        return f"Movie with ID {movie_id} not found in library."
    if m.return_movie():
        return f"'{m.get_title()}' was returned successfully."
    else:
        return f"'{m.get_title()}' was not rented - cannot be returned."


def add_movie(movies):
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
    id_ = input("Enter the movie ID to remove: ")
    m = find_movie_by_id(movies, id_)
    if m is None:
        return f"Movie with ID {id_} not found in library - cannot be removed."
    movies.remove(m)
    return f"Movie '{m.get_title()}' has been removed from library successfully."


def update_movie_details(movies):
    id_ = input("Enter the movie ID to update: ")
    m = find_movie_by_id(movies, id_)
    if m is None:
        return f"Movie with ID {id_} not found in library."
    new_title = input(f"Enter new title (current: {m.get_title()}): ") or m.get_title()
    new_director = input(f"Enter new director (current: {m.get_director()}): ") or m.get_director()
    genre_input = input(f"Enter new genre (current: {m.get_genre_name()}) (0-9): ")
    new_genre = int(genre_input) if genre_input else m.get_genre()
    price_input = input(f"Enter new price (current: {m.get_price()}): ")
    new_price = float(price_input) if price_input else m.get_price()
    m.set_title(new_title)
    m.set_director(new_director)
    m.set_genre(new_genre)
    m.set_price(new_price)
    return f"Movie with ID {id_} is updated successfully."