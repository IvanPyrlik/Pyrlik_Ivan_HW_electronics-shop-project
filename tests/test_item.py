"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item3():
    return Item("Телевизор", 15000, 5)


@pytest.fixture
def item4():
    return Item("Холодильник", 30000, 3)


@pytest.fixture()
def num1():
    return '5'


@pytest.fixture()
def num2():
    return '7.0'


@pytest.fixture
def phone2():
    return Phone("Samsung", 100_000, 3, 1)


def test_calculate_total_price(item3, item4):
    """
    Когда мы создаем класс со значением Х, Y, Z, то calculate_total_price вернет нам Y * Z
    """
    assert item3.calculate_total_price() == 75000
    assert item4.calculate_total_price() == 90000


def test_apply_discount(item3, item4):
    """
    Когда мы создаем класс со значением Х, Y, Z, то apply_discount вернет нам Y * 0.5(уровень цены с учетом скидки)
    """
    Item.pay_rate = 0.5
    item3.apply_discount()
    item4.apply_discount()
    assert item3.price == 7500
    assert item4.price == 15000


def test_string_to_number(num1, num2):
    """
    Проверка перевода из str в int
    """
    assert Item.string_to_number(num1) == 5
    assert Item.string_to_number(num2) == 7


def test_repr(item3, item4):
    """
    Проверка метода __repr__
    """
    assert repr(item3) == "Item('Телевизор', 15000, 5)"
    assert repr(item4) == "Item('Холодильник', 30000, 3)"


def test_str(item3, item4):
    """
    Проверка метода __str__
    """
    assert str(item3) == 'Телевизор'
    assert str(item4) == 'Холодильник'


def test_add(item3, item4, phone2):
    """
    Проверка метода __add__
    """
    assert item3 + item4 == 8
    assert phone2 + item3 == 8
