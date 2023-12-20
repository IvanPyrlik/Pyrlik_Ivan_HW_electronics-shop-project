import pytest

from src.keyboard import Keyboard, MixinLog


@pytest.fixture
def kb1():
    return Keyboard('Logitech', 6000, 3)


@pytest.fixture
def kb2():
    return Keyboard('Razer', 20000, 8)


def test_str(kb1, kb2):
    """
    Проверка метода __str__.
    """
    assert str(kb1) == "Logitech"
    assert str(kb2) == "Razer"

    assert str(kb1.language) == "EN"


def test_change_lang(kb1, kb2):
    """
    Проверка метода change_lang.
    """
    kb1.change_lang()
    assert str(kb1.language) == "RU"

    # Сделали EN -> RU -> EN
    kb2.change_lang().change_lang()
    assert str(kb2.language) == "EN"


def test_language(kb1):
    """
    Проверка языка.
    """
    with pytest.raises(AttributeError):
        kb1.language = 'CH'
        kb1.language = 'UK'
