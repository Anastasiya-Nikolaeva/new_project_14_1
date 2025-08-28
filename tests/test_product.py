import sys
from typing import Any

import pytest

from src.product import Product


def test_product_initialization(product: Product) -> None:
    """Тестирование инициализации продукта"""
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_product_name(product: Product) -> None:
    """Тестирование имени продукта"""
    product.name = "Samsung Galaxy S23 Ultra"
    assert product.name == "Samsung Galaxy S23 Ultra"


def test_product_description(product: Product) -> None:
    """Тестирование описания продукта"""
    product.description = "256GB, Серый цвет, 200MP камера"
    assert product.description == "256GB, Серый цвет, 200MP камера"


def test_product_price(product: Product) -> None:
    """Тестирование цены продукта"""
    product.price = 31000.0
    assert product.price == 31000.0


def test_product_quantity(product: Product) -> None:
    """Тестирование количества продукта"""
    product.quantity = 14
    assert product.quantity == 14


def test_set_price_negative_value(product: Product) -> None:
    """Тестирование установки отрицательной цены"""
    product.price = -5000.0
    assert product.price == 31000.0  # Цена не должна измениться


def test_set_price_zero_value(product: Product) -> None:
    """Тестирование установки нулевой цены"""
    product.price = 0.0
    assert product.price == 31000.0  # Цена не должна измениться


def test_set_price_lower_than_current(product: Product, monkeypatch: Any) -> None:
    """Тестирование установки цены ниже текущей с подтверждением"""
    # Подменяем ввод пользователя
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 25000.0
    assert product.price == 25000.0  # Цена должна измениться


def test_set_price_lower_than_current_cancel(product: Product, monkeypatch: Any) -> None:
    """Тестирование установки цены ниже текущей с отменой"""
    # Подменяем ввод пользователя
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 25000.0
    assert product.price == 31000.0  # Цена не должна измениться


def test_new_product_creation() -> None:
    """Тестирование создания нового продукта"""
    product_data = {"name": "Apple iPhone 14", "description": "128GB, Черный", "price": "80000.0", "quantity": "5"}
    new_product = Product.new_product(product_data)
    assert new_product.name == "Apple iPhone 14"
    assert new_product.description == "128GB, Черный"
    assert new_product.price == 80000.0
    assert new_product.quantity == 5


def test_new_product_update_existing(product: Product) -> None:
    """Тестирование обновления существующего продукта"""
    existing_products = [product]
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": "32000.0",
        "quantity": "5",
    }

    # Обновляем существующий продукт
    updated_product = Product.new_product(product_data, existing_products)

    assert updated_product.quantity == 19  # Количество должно увеличиться
    assert updated_product.price == 32000.0  # Цена должна обновиться


def test_product_str(product: Product) -> None:
    """Тестирование строкового представления продукта"""
    assert str(product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add_products() -> None:
    """Тестирование сложения двух продуктов"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    total_value = product1 + product2
    assert total_value == (180000.0 * 5) + (210000.0 * 8)  # Ожидаемая общая стоимость


def test_product_initialization_invalid_price() -> None:
    """Тестирование инициализации продукта с некорректной ценой"""
    with pytest.raises(ValueError):
        Product("Товар", "Описание", -100.0, 10)


def test_product_initialization_invalid_quantity() -> None:
    """Тестирование инициализации продукта с некорректным количеством"""
    with pytest.raises(ValueError):
        Product("Товар", "Описание", 100.0, -5)


def test_add_invalid_type() -> None:
    """Тестирование сложения с объектом неверного типа"""
    product1 = Product("Товар 1", "Описание 1", 100.0, 10)
    with pytest.raises(TypeError):
        product1 + "непродукт"


def test_new_product_update_existing_same_name(product: Product) -> None:
    """Тестирование обновления существующего продукта с одинаковым именем"""
    existing_products = [product]
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "Обновленное описание",
        "price": "33000.0",
        "quantity": "3",
    }

    # Обновляем существующий продукт
    updated_product = Product.new_product(product_data, existing_products)

    assert updated_product.quantity == 17  # Количество должно увеличиться
    assert updated_product.price == 33000.0  # Цена должна обновиться


if __name__ == "__main__":
    sys.exit(pytest.main())
