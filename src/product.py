from typing import Dict, List, Optional


class Product:
    """Класс для представления продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для установки цены с проверкой и подтверждением"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            confirmation = input(
                f"Новая цена {value} ниже текущей цены {self.__price}. Вы уверены, что хотите "
                f"понизить цену? (y/n): "
            )
            if confirmation.lower() != "y":
                print("Изменение цены отменено.")
                return

        self.__price = value

    def __add__(self, other: "Product") -> float:
        """Переопределение оператора сложения для получения полной стоимости"""
        if type(other) is Product:
            # Полная стоимость для каждого продукта
            total_value_self = self.price * self.quantity
            total_value_other = other.price * other.quantity
            return total_value_self + total_value_other
        raise TypeError

    @classmethod
    def new_product(cls, product_dt: Dict[str, str], existing_products: Optional[List["Product"]] = None) -> "Product":
        """Класс-метод для создания нового продукта из словаря"""
        if existing_products is None:
            existing_products = []

        name = product_dt.get("name", "") or ""  # Пустая строка по умолчанию чтобы mypy не выдавал ошибку
        description = (
            product_dt.get("description", "") or ""
        )  # Пустая строка по умолчанию чтобы mypy не выдавал ошибку
        price = float(product_dt.get("price", 0))
        quantity = int(product_dt.get("quantity", 0))

        for existing_product in existing_products:
            if existing_product.name == name:
                # Если товар существует, обновляем количество и цену
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)
                return existing_product

        new_product_instance = cls(name, description, price, quantity)
        return new_product_instance
