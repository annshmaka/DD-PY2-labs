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
        self.author = author # Имя автора можно менять
        self._year = None  # Год написания песни по умолчанию отсутствует, не может меняться пользователем

        @property
        def year(self):
            return self._year

        def add_year(self, year: int):
            """
            Метод, позволяющий добавить год написания песни
            :param year:
            :return:

            Примеры:
            >>> test_song = Song("Hello, Dolly", "Louis Armstrong")
            >>> test_song.add_year(1968)
            """
            self.year = year

        def __str__(self) -> str:
            return f'Название песни "{self.name}", Имя автора песни "{self.author}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.year!r})'


class JazzSong(Song):

    def __init__(self, name: str, duration: float):
        """
               Создание объекта класса джазовая песня
               :param name: название песни
               :param duration: длительность песни

               Примеры:
               >>> test_song = JazzSong("Hello, Dolly", "Louis Armstrong") #Инициализация объекта класса
               """
        super().__init__(name)  # вызываем конструктор базового класса
        self.duration = duration

        def __str__(self) -> str:
            return f'Название песни "{self.name}". Длительность джазовой песни "{self.duration}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, {self.duration!r})' # Перегружаем магический метод __repr__

