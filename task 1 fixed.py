class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
                Создание объекта класса Книга
                :param name: название книги
                :param author: автор книги
                """
        self._name = name
        self._author = author

        @property
        def name(self):
            return self._name

        @property
        def author(self):
            return self._author

        @name.setter
        def name(self, new_name: str) -> None:
            """Устанавливает имя книги."""
            if not isinstance(new_name, str):
                raise TypeError("название книги должно быть типа str")
        self._name = name

        @author.setter
        def author(self, new_author: str) -> None:
            """Устанавливает автора книги."""
            if not isinstance(new_author, str):
                raise TypeError("имя автора книги должно быть типа str")
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        """
            Создание объекта класса бумажная книга
            :param name: название книги
            :param author: автор книги
            :param pages: количество страниц книги
            """
        super().__init__(name, author)
        self.pages = pages

        @property
        def pages(self) -> int:
            """Возвращает количество страниц в бумажной книге."""
            return self.pages

        @pages.setter
        def pages(self, new_pages: int) -> None:
            """Устанавливает количество страниц в книге."""
            if not isinstance(new_pages, int):
                raise TypeError("Количество страниц должно быть типа int")
            if new_pages <= 0:
                raise ValueError("Количество страниц должно быть положительным числом")
            self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страницы {self.pages}"
    # перегружаем метод __str__, т.к. добавили количество страниц в книге и изменили название класса на Бумажная книга

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"
    # перегружаем метод __repr__, т.к. добавили количество страниц в книге


class AudioBook(Book):
    """Дочерний класс Аудиокнига"""
    def __init__(self, name: str, author: str, duration: float):
        """
            Создание объекта класса аудиокнига
            :param name: название книги
            :param author: автор книги
            :param duration: длительность аудиокниги в часах
            """
        super().__init__(name, author)
        self.duration = duration

        @property
        def duration(self) -> float:
            """Возвращает продолжительность аудиокниги."""
            return self._duration

        @duration.setter
        def duration(self, new_duration: float) -> None:
            """Устанавливает продолжительность аудиокниги."""
            if not isinstance(new_duration, float):
                raise TypeError("Продолжительность аудиокниги должна быть типа int")
            if new_duration <= 0:
                raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
            self._duration = new_duration

    def __str__(self):
        return f"Аудио книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    # перегружаем метод __str__, т.к. добавили длительность аудиокниги и изменили название класса на Аудиокнига

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
    # перегружаем метод __repr__, т.к. добавили длительность аудиокниги

