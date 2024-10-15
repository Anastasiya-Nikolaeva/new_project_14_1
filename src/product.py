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
            confirmation = input(f"Новая цена {value} ниже текущей цены {self.__price}. Вы уверены, что хотите "
                                 f"понизить цену? (y/n): ")
            if confirmation.lower() != 'y':
                print("Изменение цены отменено.")
                return

        self.__price = value

    @classmethod
    def new_product(cls, product_dt: Dict[str, str], existing_products: Optional[List['Product']] = None) -> 'Product':
        """Класс-метод для создания нового продукта из словаря"""
        if existing_products is None:
            existing_products = []

        name = product_dt.get('name', '') or ''  # Пустая строка по умолчанию чтобы mypy не выдавал ошибку
        description = product_dt.get('description', '') or ''  # Пустая строка по умолчанию чтобы mypy не выдавал ошибку
        price = float(product_dt.get('price', 0))
        quantity = int(product_dt.get('quantity', 0))

        for existing_product in existing_products:
            if existing_product.name == name:
                # Если товар существует, обновляем количество и цену
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)
                return existing_product

        new_product_instance = cls(name, description, price, quantity)
        return new_product_instance


# if __name__ == "__main__":
#     existing_products = []
#
#     product_dt1 = {
#         'name': 'Samsung Galaxy S23 Ultra',
#         'description': 'Современный смартфон',
#         'price': '180000.0',
#         'quantity': '5'
#     }
#
#     product1 = Product.new_product(product_dt1, existing_products)
#     existing_products.append(product1)
#
#     print(product1.name, product1.description, product1.price, product1.quantity)
#
#     product_dt2 = {
#         'name': 'Samsung Galaxy S23 Ultra',
#         'description': 'Современный смартфон',
#         'price': '190000.0',
#         'quantity': '3'
#     }
#
#     product2 = Product.new_product(product_dt2, existing_products)
#
#     print(product2.name, product2.description, product2.price, product2.quantity)
#
#     # Пример понижения цены
#     print("Попробуем понизить цену на продукт:")
#     product1.price = 170000.0  # Понижение цены, должно запросить подтверждение
#
#     print(f"Обновленная цена: {product1.price}")
#
#     for product in existing_products:
#         print(f"{product.name}: {product.quantity} шт, цена: {product.price}")
