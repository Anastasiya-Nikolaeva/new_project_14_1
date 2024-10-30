import pytest

from src.new_class import LawnGrass, Smartphone


def test_smartphone_initialization(smartphone1: Smartphone) -> None:
    """Тестирование инициализации смартфона"""
    assert smartphone1.name == "Xiaomi Redmi Note 11"
    assert smartphone1.description == "Смартфон с хорошей камерой"
    assert smartphone1.price == 31000.0
    assert smartphone1.quantity == 10
    assert smartphone1.efficiency == 2.5
    assert smartphone1.model == "Redmi"
    assert smartphone1.memory == 128
    assert smartphone1.color == "Синий"


def test_lawn_grass_initialization(lawn_grass1: LawnGrass) -> None:
    """Тестирование инициализации газона"""
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Трава для газонов"
    assert lawn_grass1.price == 1500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "14 дней"
    assert lawn_grass1.color == "Зеленый"


def test_smartphone_addition(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    """Тестирование сложения двух смартфонов"""
    total_value = smartphone1 + smartphone2
    expected_value = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)
    assert total_value == expected_value


def test_lawn_grass_addition(lawn_grass1: LawnGrass, lawn_grass2: LawnGrass) -> None:
    """Тестирование сложения двух сортов газона"""
    total_value = lawn_grass1 + lawn_grass2
    expected_value = (lawn_grass1.price * lawn_grass1.quantity) + (lawn_grass2.price * lawn_grass2.quantity)
    assert total_value == expected_value


def test_smartphone_addition_type_error(smartphone1: Smartphone) -> None:
    """Тестирование обработки ошибки при сложении с неправильным типом"""
    with pytest.raises(TypeError):
        smartphone1 + "Некорректный тип"


def test_lawn_grass_addition_type_error(lawn_grass1: LawnGrass) -> None:
    """Тестирование обработки ошибки при сложении с неправильным типом"""
    with pytest.raises(TypeError):
        lawn_grass1 + "Некорректный тип"
