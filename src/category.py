from typing import List, Optional

from src.product import Product


class Category:
    """Класс для представления категорий"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию, если его еще нет в списке"""
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products_info(self) -> str:
        """Геттер для получения информации о товарах в формате строки"""
        if not self.__products:
            return "Нет товаров в категории."

        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        )

    def get_products(self) -> List[Product]:
        """Метод для получения списка продуктов"""
        return self.__products.copy()

    @property
    def products(self) -> List[Product]:
        """Геттер для получения списка продуктов"""
        return self.__products.copy()


# Пример использования
if __name__ == "__main__":
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
                        "для удобства жизни")
    product1 = Product("Samsung Galaxy S23 Ultra", "Современный смартфон", 180000.0, 5)
    product2 = Product("Iphone 15", "1024GB, Синий", 210000.0, 8)

    category.add_product(product1)
    category.add_product(product2)

    print(category.products_info)
