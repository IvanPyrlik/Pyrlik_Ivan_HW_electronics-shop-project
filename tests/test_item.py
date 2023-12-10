"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


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
    assert Item.string_to_number(num1) == 5
    assert Item.string_to_number(num2) == 7
