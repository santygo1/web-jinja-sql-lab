class Genre:

    def __init__(self, genre_id, name):
        self.__id = genre_id
        self.__name = name

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
