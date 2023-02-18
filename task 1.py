if __name__ == "__main__":
    # Write your solution here
    pass


class Song:
    """Класс песня, который будет использоваться для хранения названий песен"""
    def __init__(self, name: str, author: str):
        """
        Создание объекта класса песня
        :param name: название песни
        :param author: автор песни

        Примеры:
        >>> test_song = Song("Hello, Dolly", "Louis Armstrong") #Инициализация объекта класса
        """
        self.name = name  # Название песни можно менять
        self.author = author # Имя автора тоже можно менять
        self._genre = None  # Жанр песни по умолчанию отсутствует, не может меняться пользователем

        @property
        def genre(self):
            return self._genre

        def add_genre(self, genre: str):
            """
            Метод, позволяющий добавить жанр песни
            :param genre:
            :return:

            Примеры:
            >>> test_song = Song("Hello, Dolly", "Louis Armstrong")
            >>> test_song.add_genre("Jazz")
            """
            self._genre = genre

        def write_genre(self):
            """
            Метод, позволяющий вернуть добавленный ранее жанр песни
            :return: возвращает название жанра
            Примеры:
            >>> test_song = Song("Hello, Dolly", "Louis Armstrong") #Инициализация объекта класса песня
            >>> test_song.add_genre("Jazz")
            >>> test_song.write_genre()
            'Jazz'
            """
            return self._genre

        def __str__(self) -> str:
            return f'Название песни "{self.name}", Имя автора песни "{self.author}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.year!r})'

        def __eq__(self: Song, other: Song):
            """
            Метод, позволяющий проверить, одинаковые ли песни
            Примеры:
            song_1 = Song("Happy New Year")
            song_2 = Song("Happy New Year")
            print(song_1 == song_2)  # song_1 - self, song_2 - other
            """
        return self.name == other.name


class JazzSong(Song):
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание объекта класса джазовая песня
        :param name: название песни
        :param author: автор песни
        :param duration: длительность песни
        Примеры:
        >>> test_song = JazzSong("Hello, Dolly", "Louis Armstrong") #Инициализация объекта класса
        """
        super().__init__(name, author)  # вызываем конструктор базового класса
        self.duration = duration

        def __str__(self) -> str:
            return f'Название песни "{self.name}", Имя автора песни "{self.author}", ' \
                   f'Длительность джазовой песни "{self.duration}"'

        # Перегружаем магический метод __repr__

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, {self.author!r} {self.duration!r})'
            # Перегружаем магический метод __repr__

