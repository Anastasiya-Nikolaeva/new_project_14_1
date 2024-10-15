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


if __name__ == "__main__":
    sys.exit(pytest.main())
