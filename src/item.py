import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден.'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}'f'(\'{self.name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        # elif len(new_name) > 10:
        # self.__name = new_name[0:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError('Файл item.csv поврежден.')
                    else:
                        print(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            print('Отсутствует файл item.csv.')



    @staticmethod
    def string_to_number(num: str):
        num = float(num)
        num_int = int(float(num))
        return num_int

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
