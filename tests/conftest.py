from typing import Generator

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product() -> Product:
    """Для создания продукта"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category() -> Category:
    """Для создания категории"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций "
        "для удобства жизни",
        [],
    )


@pytest.fixture(autouse=True)
def reset_category_count() -> Generator[None]:
    """Фикстура для сброса счетчика категорий перед каждым тестом."""
    Category.category_count = 0
    yield
    Category.category_count = 0  # Сброс после теста, если это необходимо


@pytest.fixture(autouse=True)
def reset_product_count() -> Generator[None]:
    """Фикстура для сброса счетчика продуктов перед каждым тестом."""
    Category.product_count = 0
    yield
    Category.product_count = 0  # Сброс после теста, если это необходимо
