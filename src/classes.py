from src.json_loads import (get_category_description, get_category_products, get_list_categories,
                            get_name_of_categories, json_file_path)


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
        self.products = products

        # Увеличиваем счетчик общего количества категорий
        Category.total_categories += 1

        # Увеличиваем счетчик общего количества уникальных продуктов
        unique_products = []
        for product in self.products:
            if product not in unique_products:
                unique_products.append(product)
                Category.total_unique_products += 1


category_1 = Category(
    get_name_of_categories(list_categories=get_list_categories(json_file_path))[0],
    get_category_description(list_categories=get_list_categories(json_file_path))[0],
    get_category_products(list_categories=get_list_categories(json_file_path))["Смартфоны"],
)

category_2 = Category(
    get_name_of_categories(list_categories=get_list_categories(json_file_path))[1],
    get_category_description(list_categories=get_list_categories(json_file_path))[1],
    get_category_products(list_categories=get_list_categories(json_file_path))["Телевизоры"],
)


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


product_1 = Product(
    get_list_categories(json_file_path)[0]["products"][0]["name"],
    get_list_categories(json_file_path)[0]["products"][0]["description"],
    get_list_categories(json_file_path)[0]["products"][0]["price"],
    get_list_categories(json_file_path)[0]["products"][0]["quantity"],
)

product_2 = Product(
    get_list_categories(json_file_path)[0]["products"][1]["name"],
    get_list_categories(json_file_path)[0]["products"][1]["description"],
    get_list_categories(json_file_path)[0]["products"][1]["price"],
    get_list_categories(json_file_path)[0]["products"][1]["quantity"],
)

product_3 = Product(
    get_list_categories(json_file_path)[0]["products"][2]["name"],
    get_list_categories(json_file_path)[0]["products"][2]["description"],
    get_list_categories(json_file_path)[0]["products"][2]["price"],
    get_list_categories(json_file_path)[0]["products"][2]["quantity"],
)

product_4 = Product(
    get_list_categories(json_file_path)[1]["products"][0]["name"],
    get_list_categories(json_file_path)[1]["products"][0]["description"],
    get_list_categories(json_file_path)[1]["products"][0]["price"],
    get_list_categories(json_file_path)[1]["products"][0]["quantity"],
)


print(f"Общее количество категорий товаров: {Category.total_categories}")
print(f"Общее количество уникальных товаров: {Category.total_unique_products}")
print(f"Категория товара: {category_1.name}")
print(f"Описание категории: {category_1.description}")
print(f"Список товаров в категории: {category_1.products}")
print(f"Категория товара: {category_2.name}")
print(f"Описание категории: {category_2.description}")
print(f"Список товаров в категории: {category_2.products}")
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
