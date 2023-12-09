# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Cat:
    def __init__(self, arg1: str, arg2: Union[int, float], arg3: bool):
        """
                Создание и подготовка к работе объекта "Котенок"

                :param arg1: Имя котенка
                :param arg2: Возраст котенка
                :param arg3: Накормлен ли котенок

                Примеры:
                >>> kitten = Cat("Бася", 3, False)  # инициализация экземпляра класса
                """
        if not isinstance(arg1, (str)):
            raise TypeError("Имя котенка должно быть типа str")
        self.name = arg1
        if not isinstance(arg2, (int, float)):
            raise TypeError("Возраст котенка должен быть типа int или float")
        if not (arg2 > 0 and arg2<25):
            raise ValueError("Возраст котенка должен быть положительным числом не более 25")
        self.age = arg2
        if not isinstance(arg3, (bool)):
            raise TypeError("Факт накормленности котенка должен быть типа bool")
        self.eat = arg3
    def toeat(self) -> bool:
        """
               Функция которая позволяет накормить голодного кота

                :return: Можно ли накормить котенка или он уже сыт

               Примеры:
               >>> kitten = Cat("Бася", 3, False)
               >>> kitten.toeat()
               """
        ...
    def some_years_ago(self, years:Union[int, float]) -> None:
        """
               Добавление лет котенку.
               :param years: Количество добавляемых лет

               Примеры:
               >>> kitten = Cat("Бася", 3, False)
               >>> kitten.some_years_ago(5)
               """
        if not isinstance(years, (int, float)):
            raise TypeError("Добавляемый возраст должен быть типа int или float")
        if years < 0:
            raise ValueError("Добавляемый возраст должен быть положительным числом")
        ...
    def play(self) -> bool:
        """
               Функция, позволяющая поиграть с котенком.

                :return: Можно ли поиграть с  котенком или у него нет сил от голода

               Примеры:
               >>> kitten = Cat("Бася", 3, False)
               >>> kitten.play()
               """
        ...

class Cristmas_tree:
    def __init__(self, arg1: bool, arg2: Union[int, float], arg3: bool):
        """
                Создание и подготовка к работе объекта "Рождественская елка"

                :param arg1: Жива ли елка
                :param arg2: Возраст дерева
                :param arg3: Украшена ли елка

                Примеры:
                >>> tree = Cristmas_tree(True, 120, False)  # инициализация экземпляра класса
                """
        if not isinstance(arg1, (bool)):
            raise TypeError("Факт жива ли елка должен быть типа bool")
        self.life = arg1
        if not isinstance(arg2, (int, float)):
            raise TypeError("Возраст елки должен быть типа int или float")
        if not (arg2 > 0 and arg2<300):
            raise ValueError("Возраст котенка должен быть положительным числом не более 300")
        self.age = arg2
        if not isinstance(arg3, (bool)):
            raise TypeError("Факт украшенности елки должен быть типа bool")
        self.beautiful = arg3
    def cut(self) -> bool:
        """
               Функция которая позволяет срубить елку

                :return: Можно ли срубить елку или она уже срублена

               Примеры:
               >>> tree = Cristmas_tree(True, 120, False)
               >>> tree.cut()
               """
        ...
    def some_years_ago(self, years:Union[int, float]) -> None:
        """
               Добавление лет елке.
               :param years: Количество добавляемых лет

               Примеры:
               >>> tree = Cristmas_tree(True, 120, False)
               >>> tree.some_years_ago(55)
               """
        if not isinstance(years, (int, float)):
            raise TypeError("Добавляемый возраст должен быть типа int или float")
        if years < 0:
            raise ValueError("Добавляемый возраст должен быть положительным числом")
        ...
    def to_decorate(self) -> bool:
        """
               Функция, позволяющая украсить елку.

                :return: Можно ли украсить елку или она уже украшена

               Примеры:
               >>> tree = Cristmas_tree(True, 120, False)
               >>> tree.to_decorate()
               """
        ...

class Player:
    def __init__(self, arg1: str, arg2: int, arg3: int):
        """
                Создание и подготовка к работе объекта "Игровой персонаж"

                :param arg1: Имя
                :param arg2: Количество здоровья
                :param arg3: Количеество энергии

                Примеры:
                >>> new = Player("Xiao", 1, 100)  # инициализация экземпляра класса
                """
        if not isinstance(arg1, (str)):
            raise TypeError("Имя персонажа должно быть типа str")
        self.name = arg1
        if not isinstance(arg2, (int)):
            raise TypeError("Здоровье персонажа должно быть типа int")
        if not (arg2 >= 0 and arg2<=100):
            raise ValueError("Здоровье персонажа должно быть в пределах от 0 до 100")
        self.health = arg2
        if not isinstance(arg3, (int)):
            raise TypeError("Энергия персонажа должна быть типа int")
        if not (arg3 >= 0 and arg3 <= 100):
            raise ValueError("Энергия персонажа должна быть в пределах от 0 до 100")
        self.energy = arg3
    def proigr_fight(self, minus:int) -> None:
        """
               Функция которая отнимает здоровье в случае проигрыша

               Примеры:
               >>> new = Player("Xiao", 100, 100)
               >>> new.proigr_fight(55)
               """
        if not isinstance(minus, int):
            raise TypeError("Отнимаемое здоровье должно быть типа int")
        if minus < 0:
            raise ValueError("Отнимаемое здоровье должно быть в пределах от 1 до 99")
        ...
    def to_eat(self, eat:int) -> None:
        """
               Покормить персонажа
               :param eat: Количество добавляемой энергии

               Примеры:
               >>> new = Player("Xiao", 100, 1)
               >>> new.to_eat(55)
               """
        if not isinstance(eat, int):
            raise TypeError("Добавляемая энергия должна быть типа int")
        if eat < 0:
            raise ValueError("Добавляемая энергия должна быть в пределах от 1 до 99")
        ...
    def is_on_otriad(self) -> bool:
        """
               Функция, позволяющая узнать находится ли данный персонаж в отряде.

                :return: В отряде ли персонаж

               Примеры:
               >>> new = Player("Xiao", 100, 100)
               >>> new.is_on_otriad()
               """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
