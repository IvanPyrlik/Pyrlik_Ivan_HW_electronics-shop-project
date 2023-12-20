from src.item import Item


class MixinLog:
    """
    Создание класса для дополнительного функционала.
    """
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language: str):
        if new_language != 'EN' or new_language != 'RU':
            raise AttributeError
        else:
            self.__language = new_language

    def change_lang(self):
        """
        Метод для изменения языка.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLog):
    """
    Создание экземпляра подкласса Keyboard.
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

