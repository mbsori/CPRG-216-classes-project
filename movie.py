class Movie:
    GENRES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance",
              "Thriller", "Animation", "Documentary", "Fantasy"]

    def __init__(self, movie_id, title, director, genre, available=True, price=0.0, rental_count=0):
        self.__id = movie_id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__rental_count = rental_count

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_director(self):
        return self.__director
    def get_genre(self):
        return self.__genre
    def get_price(self):
        return self.__price
    def get_rental_count(self):
        return self.__rental_count

    def get_genre_name(self):
        return Movie.GENRES[self.__genre] if 0 <= self.__genre < len(Movie.GENRES) else "Unknown"

    def get_availability(self):
        return "Available" if self.__available else "Rented"

    def set_id(self, movie_id):
        self.__id = movie_id
    def set_title(self, title):
        self.__title = title
    def set_director(self, director):
        self.__director = director
    def set_genre(self, genre):
        self.__genre = genre
    def set_price(self, price):
        self.__price = price

    def borrow_movie(self):
        if self.__available:
            self.__available = False
            self.__rental_count += 1

    def return_movie(self):
        if not self.__available:
            self.__available = True

    def __str__(self):
        return (f"{str(self.__id):<9}{self.__title:<30}{self.__director:<25}"
                f"{self.get_genre_name():<15}{self.get_availability():<15}"
                f"{self.__price:>10.2f}{self.__rental_count:>12}")
