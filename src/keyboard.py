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
    pass

