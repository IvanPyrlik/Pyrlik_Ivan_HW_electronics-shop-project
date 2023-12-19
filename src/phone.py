from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра подкласса Phone.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num_of_sim):
        if int(num_of_sim) > 0:
            self.__number_of_sim = num_of_sim
        else:
            return ValueError

    def __repr__(self):
        return f'{self.__class__.__name__}'f'(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'

    def __str__(self):
        return f'{self.name}'
