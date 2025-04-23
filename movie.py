class Movie:
    """A class to represent a movie in the library."""

    GENRES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Animation", "Documentary", "Fantasy"]

    def __init__(self, id, title, director, genre, available=True, price=0.0, rental_count=0):
        """
        Initialize a new Movie instance.

        Parameters:
        id (str): Unique identifier for the movie.
        title (str): Title of the movie.
        director (str): Director of the movie.
        genre (int): Genre index of the movie.
        available (bool): Availability status of the movie. Defaults to True.
        price (float): Rental price of the movie. Defaults to 0.0.
        rental_count (int): Number of times the movie has been rented. Defaults to 0.
        """
        self.__id = id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__rental_count = rental_count

    # Getters
    def get_id(self):
        """Return the movie ID."""
        return self.__id

    def get_title(self):
        """Return the movie title."""
        return self.__title

    def get_director(self):
        """Return the movie director."""
        return self.__director

    def get_genre(self):
        """Return the genre index of the movie."""
        return self.__genre

    def get_genre_name(self):
        """Return the genre name of the movie."""
        return Movie.GENRES[self.__genre]

    def get_availability(self):
        """Return the availability status of the movie."""
        return "Available" if self.__available else "Rented"

    def get_price(self):
        """Return the rental price of the movie."""
        return self.__price

    def get_rental_count(self):
        """Return the rental count of the movie."""
        return self.__rental_count

    # Setters
    def set_title(self, title):
        """Set the movie title."""
        self.__title = title

    def set_director(self, director):
        """Set the movie director."""
        self.__director = director

    def set_genre(self, genre):
        """Set the genre index of the movie."""
        self.__genre = genre

    def set_price(self, price):
        """Set the rental price of the movie."""
        self.__price = price

    # Methods for borrowing and returning movies
    def borrow_movie(self):
        """Borrow the movie if available."""
        if self.__available:
            self.__available = False
            self.__rental_count += 1
            return True
        return False

    def return_movie(self):
        """Return the movie if rented."""
        if not self.__available:
            self.__available = True
            return True
        return False

    # String representation
    def __str__(self):
        """Return a formatted string representation of the movie."""
        return f"{self.__id} {self.__title} {self.__director} {self.get_genre_name()} {self.get_availability()} {self.__price} {self.__rental_count}"
def print_genres():
    """
    Display the genre menu with indices.
    """
    print("\n    Genres")
    for i, name in enumerate(Movie.GENRES):
        print(f"    {i}) {name}")
    print()


