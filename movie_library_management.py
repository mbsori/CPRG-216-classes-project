from movie import Movie
import os

GENRES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance",
          "Thriller", "Animation", "Documentary", "Fantasy"]

def load_movies(file_name):
    movie_list = []
    file = open(file_name, "r")
    count = 0
    for line in file:
        parts = line.strip().split(",")
        if len(parts) >= 7:
            movie = Movie(
                int(parts[0]), parts[1], parts[2], int(parts[3]),
                parts[4].lower() == "true", float(parts[5]), int(parts[6])
            )
            movie_list.append(movie)
            count += 1
    file.close()
    print("The catalog file \"" + file_name + "\" successfully loaded " + str(count) + " movies to the Movie Library System")
    return movie_list

def save_movies(file_name, movies):
    file = open(file_name, "w")
    count = 0
    for m in movies:
        file.write(f"{m.get_id()},{m.get_title()},{m.get_director()},{m.get_genre()},{str(m.get_availability() == 'Available')},{m.get_price()},{m.get_rental_count()}\n")
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
    for m in movies:
        print(m)

def find_movie_by_id(movies, movie_id):
    for m in movies:
        if m.get_id() == movie_id:
            return m
    return -1

def search_movies(movies, search_term):
    print(f'Searching for "{search_term.lower()}" in title, director, or genre...')
    found = []
    lower_term = search_term.lower()
    for m in movies:
        if lower_term in m.get_title().lower() or lower_term in m.get_director().lower() or lower_term in m.get_genre_name().lower():
            found.append(m)
    if not found:
        print("No matching movies found.")
    else:
        print_movies(found)

def rent_movie(movies, movie_id):
    m = find_movie_by_id(movies, movie_id)
    if m == -1:
        print("Movie with ID " + str(movie_id) + " not found in library.")
    elif m.get_availability() == "Rented":
        print("'" + m.get_title() + "' is already rented - cannot be rented again.")
    else:
        m.borrow_movie()
        print("'" + m.get_title() + "' rented successfully.")

def return_movie(movies, movie_id):
    m = find_movie_by_id(movies, movie_id)
    if m == -1:
        print("Movie with ID " + str(movie_id) + " not found in library.")
    elif m.get_availability() == "Available":
        print("'" + m.get_title() + "' was not rented - cannot be returned.")
    else:
        m.return_movie()
        print("'" + m.get_title() + "' was returned successfully.")

def add_movie(movies):
    movie_id = int(input("Enter movie ID: "))
    if find_movie_by_id(movies, movie_id) != -1:
        print("Movie with ID " + str(movie_id) + " already exists - cannot be added to library")
        return
    title = input("Enter title: ")
    director = input("Enter director: ")
    print("\n    Genres", end="")
    genre = get_genre()
    price = float(input("Enter price: "))
    new_movie = Movie(movie_id, title, director, genre, True, price, 0)
    movies.append(new_movie)
    print("Movie '" + title + "' added to library successfully.")

def remove_movie(movies):
    movie_id = int(input("Enter the movie ID to remove: "))
    m = find_movie_by_id(movies, movie_id)
    if m == -1:
        print("Movie with ID " + str(movie_id) + " not found in library - cannot be removed.")
    else:
        movies.remove(m)
        print("Movie '" + m.get_title() + "' has been removed from library successfully.")

def update_movie_details(movies):
    movie_id = int(input("Enter the movie ID to update: "))
    m = find_movie_by_id(movies, movie_id)
    if m == -1:
        print("Movie with ID " + str(movie_id) + " is not found in library.")
        return
    print("Leave fields blank to keep current values.")
    title = input("Enter new title (current: " + m.get_title() + "): ")
    if title:
        m.set_title(title)
    director = input("Enter new director (current: " + m.get_director() + "): ")
    if director:
        m.set_director(director)
    change_genre = input("Enter new genre (current: " + m.get_genre_name() + ") (Yes/Y, No/N))? ").strip().lower()
    if change_genre == "yes" or change_genre == "y":
        genre = get_genre()
        m.set_genre(genre)
    price = input("Enter new price (current: " + str(m.get_price()) + "): ")
    if price:
        m.set_price(float(price))
    print("Movie with ID " + str(m.get_id()) + " is updated successfully.")

def list_movies_by_genre(movies):
    genre = get_genre()
    found = [m for m in movies if m.get_genre() == genre]
    if found:
        print_movies(found)
    else:
        print("No movies found in selected genre.")

def check_availability_by_genre(movies):
    genre = get_genre()
    found = [m for m in movies if m.get_genre() == genre and m.get_availability() == "Available"]
    if found:
        print_movies(found)
    else:
        print("No available movies in the selected genre.")

def display_library_summary(movies):
    total = len(movies)
    available = sum(1 for m in movies if m.get_availability() == "Available")
    rented = total - available
    print("\nTotal movies    : " + str(total))
    print("Available movies: " + str(available))
    print("Rented movies   : " + str(rented))

def popular_movies(movies):
    threshold = int(input("Enter the minimum number of rentals for the movies you want to view: "))
    print("\nMovies Rented " + str(threshold) + " times or more")
    print("ID        Title                         Director                 Genre                # Rentals")
    print("--------------------------------------------------------------------------------------------------")
    for m in movies:
        if m.get_rental_count() >= threshold:
            print(f"{m.get_id():<9}{m.get_title():<30}{m.get_director():<25}{m.get_genre_name():<20}{m.get_rental_count():>10}")

def main():
    filename = input("Enter the movie catalog filename: ").strip()
    if os.path.exists(filename):
        movie_list = load_movies(filename)
    else:
        print("The catalog file \"" + filename + "\" is not found")
        ans = input("\nDo you want to continue without loading a file (Yes/Y, No/N))? ").strip().lower()
        if ans != "yes" and ans != "y":
            print("The Movie Library System will not continue...")
            print("Movie Library System Closed Successfully")
            return
        movie_list = []
        print("The Movie Library System is opened without loading catalog")

    menu = print_menu()
    while menu != "0":
        if menu == "1":
            term = input("Enter search term: ")
            search_movies(movie_list, term)
        elif menu == "2":
            movie_id = int(input("Enter the movie ID to rent: "))
            rent_movie(movie_list, movie_id)
        elif menu == "3":
            movie_id = int(input("Enter the movie ID to return: "))
            return_movie(movie_list, movie_id)
        elif menu == "4":
            add_movie(movie_list)
        elif menu == "5":
            remove_movie(movie_list)
        elif menu == "6":
            update_movie_details(movie_list)
        elif menu == "7":
            list_movies_by_genre(movie_list)
        elif menu == "8":
            popular_movies(movie_list)
        elif menu == "9":
            check_availability_by_genre(movie_list)
        elif menu == "10":
            display_library_summary(movie_list)
        else:
            print("Invalid choice. Please try again.")
        menu = print_menu()

    ans = input("\nWould you like to update the catalog (Yes/Y, No/N))? ").strip().lower()
    if ans == "yes" or ans == "y":
        count = save_movies(filename, movie_list)
        print(str(count) + " movies have been written to Movie catalog.")
    else:
        print("Movie catalog has not been updated.")
    print("Movie Library System Closed Successfully")

if __name__ == "__main__":
    main()
