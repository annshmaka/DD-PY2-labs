import doctest


class Cake:
    def __init__(self, expiration_date: int, calories: int):
        """
        Создание и подготовка к работе объекта "Торт"
        :param expiration_date: Срок годности торта в днях
        :param calories: Число калорий на 100 г торта
        Примеры:
        >>> cake = Cake(5, 400)  # инициализация экземпляра класса
        """
        if not isinstance(expiration_date, int):
            raise TypeError("Срок годности торта должен быть типа int")
        if expiration_date <= 0:
            raise ValueError("Срок годности торта должен быть положительным числом")
        self.expiration_date = expiration_date

        if not isinstance(calories, int):
            raise TypeError("Число калорий в торте должно быть типа int")
        if calories < 0:
            raise ValueError("Число калорий в торте не может быть отрицательным числом")
        self.calories = calories

        def is_cake_vegan(self) -> bool:
            """
            Функция которая проверяет является ли торт веганским
            :return: Является ли  торт подходящим для веганов
            Примеры:
            >>> cake = cake(4, 350)
            >>> cake.is_cake_vegan()
            """
            ...

        def add_candles_to_cake(self, candles: int) -> None:
            """
            Добавление свечей на торт.
            :param candles: Количество добавляемых свечей
            Примеры:
            >>> cake = Cake(5, 400)
            >>> cake.add_candles_to_cake(15)
            """
            if not isinstance(candles, int):
                raise TypeError("Добавляемое число свечей должено быть типа int")
            ...


class Car:
    def __init__(self, speed_max: int, seats_count: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param speed_max: Максимальная скорость автомобиля км/ч
        :param seats_count: Количество мест для пассажиров автомобиля
        Примеры:
        >>> car = Car(200, 5)  # инициализация экземпляра класса
        """
        if not isinstance(speed_max, int):
            raise TypeError("Максимальная скорость автомобиля должна быть типа int")
        if speed_max <= 0:
            raise ValueError("Максимальная скорость автомобиля должна быть положительным числом")
        self.speed_max = speed_max

        if not isinstance(seats_count, int):
            raise TypeError("Число пассажирских мест в автомобиле должно быть int")
        if seats_count < 0:
            raise ValueError("Число пассажирских мест в автомобиле не может быть отрицательным числом")
        self.seats_count = seats_count

    def is_drivers__seatbelt_fastened(self) -> bool:
        """
        Функция которая проверяет пристегнут ли ремень безопасности водителя автомобиля
        :return: Пристегнут ли водитель автомобиля
        Примеры:
        >>> car = Car(200, 5)
        >>> car.is_drivers__seatbelt_fastened()
        """
        ...

    def add_fuel(self, fuel: float) -> None:
        """
        Добавление топлива в бензобак автомобиля.
        :param fuel: Объем добавляемого топлива в литрах
        :raise ValueError: Если объем добавляемого топлива превышает свободное место в бензобаке, то вызываем ошибку
        Примеры:
        >>> car = Car(200, 2)
        >>> car.add_fuel(5)
        """
        if not isinstance(fuel, (int, float)):
            raise TypeError("Добавляемый объем топлива должен быть типа int или float")
        if fuel < 0:
            raise ValueError("Добавляемый объем топлива должен быть положительным числом")
        ...

    def add_baby_car_seat (self, baby_car_seat: int) -> None:
        """
        Добавление детского дорожного кресла в машину.
        :param baby_car_seat: Число добавляемых детских дорожных кресел
        :raise ValueError: Если количество добавляемых детских дорожных кресел превышает (число пассажирских мест - 1),
        то возвращается ошибка.
        :return: Число добавленных детских кресел в автомобиль
        Примеры:
        >>> car = Car(180, 7)
        >>> car.add_baby_car_seat(2)
        """
        ...


class Container:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Контейнер"
        :param capacity_volume: Объем контейнера
        :param occupied_volume: Занимаемый объем контейнера
        Примеры:
        >>> container = Container(10000, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем контейнера должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем контейнера должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем груза должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Объем груза не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_container(self) -> bool:
        """
        Функция которая проверяет является ли контейнер пустым
        :return: Является ли контейнер пустым
        Примеры:
        >>> container = Container(10000, 0)
        >>> container.is_empty_container()
        """
        ...

    def add_cargo_to_container(self, cargo: float) -> None:
        """
        Добавление груза в контейнер.
        :param cargo: Объем добавляемого груза
        :raise ValueError: Если объем добавляемого груза превышает свободное место в контейнере, то вызываем ошибку
        Примеры:
        >>> container = Container(500, 0)
        >>> container.add_cargo_to_container(200)
        """
        if not isinstance(cargo, (int, float)):
            raise TypeError("Добавляемый груз должен быть типа int или float")
        if cargo < 0:
            raise ValueError("Добавляемый груз должен быть положительным числом")
        ...

    def remove_cargo_from_container(self, estimate_cargo: float) -> None:
        """
        Извлечение груза из контейнера.
        :param estimate_cargo: Объем извлекаемого груза
        :raise ValueError: Если количество извлекаемого груза превышает количество груза в контейнере,
        то возвращается ошибка.
        :return: Объем реально извлеченного груза
        Примеры:
        >>> container = Container(10000, 10000)
        >>> container.remove_cargo_from_container(5000)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
