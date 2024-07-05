from typing import Any, List

from src.json_loads import (get_category_description, get_category_products, get_list_categories,
                            get_name_of_categories, json_file_path)


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        self.sales_revenue = self.price * self.quantity
        other.sales_revenue = other.price * other.quantity
        return self.sales_revenue + other.sales_revenue

    def __len__(self) -> int:
        return len(self.description)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int) -> "Product":
        """Метод для создания нового продукта и возвращения его экземпляра."""
        return cls(name, description, price, quantity)

    @property
    def _price(self) -> float:
        return self._price

    @_price.setter
    def _price(self, value: float) -> Any:
        if value <= 0:
            print("Цена введена некорректная.")
        else:
            self._price = value


class Category:
    total_categories = 0
    total_unique_products = 0

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            name = product[0]
            description = ""
            price = float(product[1])
            quantity = int(product[2])
            product_obj = Product(name, description, price, quantity)
            self.__products.append(product_obj)

        # Увеличиваем счетчик общего количества категорий
        Category.total_categories += 1

        # Увеличиваем счетчик общего количества уникальных продуктов
        unique_products = []
        for product in self.__products:
            if product.name not in unique_products:
                unique_products.append(product)
                Category.total_unique_products += 1

    def __str__(self) -> str:
        all_quantity = len(self)
        return f"{self.name}, количество продуктов: {all_quantity}"

    def __len__(self) -> int:
        return sum(product.quantity for product in self.__products)

    def get_products(self) -> List[Product]:
        return self.__products

    @property
    def products_list(self) -> str:
        """Возвращает список товаров в формате:
        Название товара, Цена руб. Остаток: Количество шт.
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result


# Получаем список категорий из файла JSON
list_categories = get_list_categories(json_file_path)


# Создаем объекты классов Category и Product
category_1 = Category(
    get_name_of_categories(list_categories)[0],
    get_category_description(list_categories)[0],
    get_category_products(list_categories)["Смартфоны"],
)
print(category_1)
print()
# Выводим список товаров для category_1
print(category_1.products_list)

category_2 = Category(
    get_name_of_categories(list_categories)[1],
    get_category_description(list_categories)[1],
    get_category_products(list_categories)["Телевизоры"],
)
# Выводим список товаров для category_2
print(category_2.products_list)


product_1 = Product(
    list_categories[0]["products"][0]["name"],
    list_categories[0]["products"][0]["description"],
    list_categories[0]["products"][0]["price"],
    list_categories[0]["products"][0]["quantity"],
)
print(product_1)
print(len(product_1))
print()
product_2 = Product(
    list_categories[0]["products"][1]["name"],
    list_categories[0]["products"][1]["description"],
    list_categories[0]["products"][1]["price"],
    list_categories[0]["products"][1]["quantity"],
)

product_3 = Product(
    list_categories[0]["products"][2]["name"],
    list_categories[0]["products"][2]["description"],
    list_categories[0]["products"][2]["price"],
    list_categories[0]["products"][2]["quantity"],
)

product_4 = Product(
    list_categories[1]["products"][0]["name"],
    list_categories[1]["products"][0]["description"],
    list_categories[1]["products"][0]["price"],
    list_categories[1]["products"][0]["quantity"],
)
print(product_1 + product_2)
print()

product_5 = Product.create_product("Продукт 5", "Описание продукта 1", 80.0, 15)
product_6 = Product.create_product("Продукт 6", "Описание продукта 2", 100.0, 20)


print(f"Общее количество категорий товаров: {Category.total_categories}")
print(f"Общее количество уникальных товаров: {Category.total_unique_products}")
print(f"Категория товара: {category_1.name}")
print(f"Описание категории: {category_1.description}")
print(f"Список товаров в категории: {[product[0] for product in get_category_products(list_categories)["Смартфоны"]]}")
print(f"Категория товара: {category_2.name}")
print(f"Описание категории: {category_2.description}")
print(
    f"Список товаров в категории: {[product[0] for product in get_category_products(list_categories)["Телевизоры"]]}"
)
print()
print(f"Название продукта: {product_1.name}")
print(f"Описание продукта: {product_1.description}")
print(f"Цена продукта: {product_1.price}")
print(f"Количество в наличии: {product_1.quantity}")
print()
print(f"Название продукта: {product_2.name}")
print(f"Описание продукта: {product_2.description}")
print(f"Цена продукта: {product_2.price}")
print(f"Количество в наличии: {product_2.quantity}")
print()
print(f"Название продукта: {product_3.name}")
print(f"Описание продукта: {product_3.description}")
print(f"Цена продукта: {product_3.price}")
print(f"Количество в наличии: {product_3.quantity}")
print()
print(f"Название продукта: {product_4.name}")
print(f"Описание продукта: {product_4.description}")
print(f"Цена продукта: {product_4.price}")
print(f"Количество в наличии: {product_4.quantity}")
