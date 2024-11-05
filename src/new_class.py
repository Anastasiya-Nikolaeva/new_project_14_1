from typing import Any

from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Product") -> Any:
        """Переопределение оператора сложения для получения полной стоимости"""
        if isinstance(other, Smartphone):
            total_value_self = self.price * self.quantity
            total_value_other = other.price * other.quantity
            return total_value_self + total_value_other
        raise TypeError


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "Product") -> Any:
        """Переопределение оператора сложения для получения полной стоимости"""
        if isinstance(other, LawnGrass):
            total_value_self = self.price * self.quantity
            total_value_other = other.price * other.quantity
            return total_value_self + total_value_other
        raise TypeError
