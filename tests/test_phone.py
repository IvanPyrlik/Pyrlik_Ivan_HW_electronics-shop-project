import pytest

from src.phone import Phone


@pytest.fixture
def phone2():
    return Phone("Samsung", 100_000, 3, 1)


@pytest.fixture
def phone3():
    return Phone("Honor", 90_000, 6, 2)


@pytest.fixture
def phone4():
    return Phone("Iron", 20_000, 3, 0)


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


def test_number_of_sim(phone4):
    """
    Проверка number_of_sim
    """
    with pytest.raises(ValueError):
        phone4.number_of_sim = 0
        phone4.number_of_sim = -1
        phone4.number_of_sim = 1.6
