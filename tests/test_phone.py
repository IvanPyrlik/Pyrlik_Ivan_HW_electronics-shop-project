import pytest

from src.phone import Phone


@pytest.fixture
def phone2():
    return Phone("Samsung", 100_000, 3, 1)


@pytest.fixture
def phone3():
    return Phone("Honor", 90_000, 6, 2)


def test_repr(phone2, phone3):
    """
    Проверка метода __repr__
    """
    assert repr(phone2) == "Phone('Samsung', 100000, 3, 1)"
    assert repr(phone3) == "Phone('Honor', 90000, 6, 2)"


def test_str(phone2, phone3):
    """
    Проверка метода __str__
    """
    assert str(phone2) == 'Samsung'
    assert str(phone3) == 'Honor'


def test_number_of_sim(phone2, phone3):
    """
    Проверка number_of_sim
    """
    assert phone2.number_of_sim == 1
    assert phone3.number_of_sim == 2
