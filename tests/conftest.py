from typing import Generator

import pytest

from src.category import Category
from src.new_class import LawnGrass, Smartphone
from src.product import Product


@pytest.fixture
def product() -> Product:
    """Для создания продукта"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product2() -> Product:
    """Создание второго продукта"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category() -> Category:
    """Для создания категории"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций "
        "для удобства жизни",
        [],
    )


@pytest.fixture(autouse=True)
def reset_category_count() -> Generator[None, None, None]:
    """Фикстура для сброса счетчика категорий перед каждым тестом."""
    Category.category_count = 0
    yield
    Category.category_count = 0  # Сброс после теста, если это необходимо


@pytest.fixture(autouse=True)
def reset_product_count() -> Generator[None, None, None]:
    """Фикстура для сброса счетчика продуктов перед каждым тестом."""
    Category.product_count = 0
    yield
    Category.product_count = 0  # Сброс после теста, если это необходимо


@pytest.fixture
def smartphone1() -> Smartphone:
    """Создание первого смартфона"""
    return Smartphone("Xiaomi Redmi Note 11", "Смартфон с хорошей камерой", 31000.0, 10, 2.5, "Redmi", 128, "Синий")


@pytest.fixture
def smartphone2() -> Smartphone:
    """Создание второго смартфона"""
    return Smartphone("Samsung Galaxy S23", "Флагманский смартфон", 80000.0, 5, 3.0, "Galaxy", 256, "Черный")


@pytest.fixture
def lawn_grass1() -> LawnGrass:
    """Создание первого сорта газона"""
    return LawnGrass("Газонная трава", "Трава для газонов", 1500.0, 20, "Россия", "14 дней", "Зеленый")


@pytest.fixture
def lawn_grass2() -> LawnGrass:
    """Создание второго сорта газона"""
    return LawnGrass(
        "Спортивная трава", "Трава для спортивных площадок", 2000.0, 10, "США", "10 дней", "Темно-зеленый"
    )
