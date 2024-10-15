import sys

import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(category: Category) -> None:
    """Тестирование инициализации категории"""
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни"
    )
    assert category.products == []
    assert Category.category_count == 1  # Проверка, что счетчик категорий равен 1


def test_multiple_categories() -> None:
    """Тестирование подсчета категорий при создании нескольких категорий"""
    category1 = Category("Смартфоны", "Описание смартфонов")
    category2 = Category("Ноутбуки", "Описание ноутбуков")
    category3 = Category("Планшеты", "Описание планшетов")

    assert Category.category_count == 3
    assert category1.name == "Смартфоны"
    assert category2.name == "Ноутбуки"
    assert category3.name == "Планшеты"


def test_add_product(category: Category, product: Product) -> None:
    """Тестирование добавления продукта в категорию"""
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.product_count == 1  # Проверка, что счетчик продуктов увеличился на 1


def test_add_multiple_products(category: Category, product: Product) -> None:
    """Тестирование добавления нескольких продуктов в категорию"""
    product2 = Product("Samsung Galaxy", "128GB, Черный", 25000.0, 10)
    category.add_product(product)
    category.add_product(product2)

    assert len(category.products) == 2
    assert category.products[0] == product
    assert category.products[1] == product2
    assert Category.product_count == 2  # Проверка, что счетчик продуктов увеличился на 2


def test_add_duplicate_product(category: Category, product: Product) -> None:
    """Тестирование добавления дубликата продукта в категорию"""
    category.add_product(product)
    category.add_product(product)  # Добавляем тот же продукт еще раз

    assert len(category.products) == 1  # Продукт не должен добавляться повторно
    assert Category.product_count == 1  # Счетчик продуктов не должен увеличиваться


def test_products_info(category: Category, product: Product) -> None:
    """Тестирование получения информации о продуктах"""
    category.add_product(product)
    expected_info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
    assert category.products_info == expected_info


def test_get_products(category: Category, product: Product) -> None:
    """Тестирование метода получения списка продуктов"""
    category.add_product(product)
    products = category.get_products()

    assert len(products) == 1
    assert products[0] == product
    assert products is not category.products  # Проверка, что возвращается копия списка


if __name__ == "__main__":
    sys.exit(pytest.main())
