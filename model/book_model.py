from model.genre_model import Genre


class Book:
    def __init__(self, title, reader, date, genre: Genre):
        self.__title = title
        self.__reader = reader
        self.__date = date
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_reader(self):
        return self.__reader

    def get_date(self):
        return self.__date

    def get_genre(self):
        return self.__genre
