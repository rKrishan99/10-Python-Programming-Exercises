class Movie:
    def __init__(self, title, genre, rating):
        """Initialize a movie with a title, genre, and rating."""
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        """Return string representation of the movie."""
        return f"'{self.title}' - Genre: {self.genre}, Rating: {self.rating}"


class MovieDatabase:
    def __init__(self):
        """Initialize an empty movie database and a set for unique genres."""
        self.movies = []  # List to hold movie objects
        self.genres = set()  # Set to hold unique genres

    def add_movie(self, movie):
        """Add a movie to the database and its genre to the set of unique genres."""
        self.movies.append(movie)  # Add movie to the list
        self.genres.add(movie.genre)  # Add genre to the set
        print(f"Added movie: {movie}")

    def search_by_genre(self, genre):
        """Search and display movies by a specific genre."""
        print(f"\nMovies in genre '{genre}':")
        found_movies = [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
        if found_movies:
            for movie in found_movies:
                print(movie)
        else:
            print(f"No movies found in the genre '{genre}'.")

    def display_movies_sorted_by_rating(self):
        """Display all movies sorted by their rating in descending order."""
        print("\nMovies sorted by rating:")
        sorted_movies = sorted(self.movies, key=lambda x: x.rating, reverse=True)  # Sort movies by rating
        for movie in sorted_movies:
            print(movie)

    def display_unique_genres(self):
        """Display all unique genres available in the database."""
        print("\nUnique Genres in the Database:")
        if self.genres:
            for genre in sorted(self.genres):  # Sort genres for better readability
                print(genre)
        else:
            print("No genres available.")


def main():
    """Main program loop for the movie database."""
    movie_database = MovieDatabase()

    while True:
        print("\n--- Movie Database ---")
        print("1. Add Movie")
        print("2. Search by Genre")
        print("3. Display All Movies Sorted by Rating")
        print("4. Display Unique Genres")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            rating = float(input("Enter movie rating (0-10): "))
            movie = Movie(title, genre, rating)
            movie_database.add_movie(movie)

        elif choice == '2':
            genre = input("Enter genre to search: ")
            movie_database.search_by_genre(genre)

        elif choice == '3':
            movie_database.display_movies_sorted_by_rating()

        elif choice == '4':
            movie_database.display_unique_genres()

        elif choice == '5':
            print("Exiting Movie Database. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
