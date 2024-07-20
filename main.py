
from src.classes import Category, Product, Smartphones, LawnGrass
from src.json_loads import get_category_products, get_list_categories, get_name_of_categories, get_category_description
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "data", "products.json")


# Получаем список категорий из файла JSON
list_categories = get_list_categories(json_file_path)


# # Создаем объекты классов Category и Product
category_1 = Category(
    get_name_of_categories(list_categories)[0],
    get_category_description(list_categories)[0],
    get_category_products(list_categories)["Смартфоны"],
)

category_2 = Category(
    get_name_of_categories(list_categories)[1],
    get_category_description(list_categories)[1],
    get_category_products(list_categories)["Телевизоры"])


product_1 = Product(
    list_categories[0]["products"][0]["name"],
    list_categories[0]["products"][0]["description"],
    list_categories[0]["products"][0]["price"],
    list_categories[0]["products"][0]["quantity"],
)

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

product_5 = Product.create_product("Продукт 5", "Описание продукта 5", 80.0, 15)
product_6 = Product.create_product("Продукт 6", "Описание продукта 6", 100.0, 20)

smartphone1 = Smartphones("Samsung Galaxy C23 Ultra", "Описание продукта", 180000.0, 5,
                          3.36, "Galaxy C23 Ultra", "256GB", "Blue")

smartphone2 = Smartphones("Xiaomi Redmi Note 11", "Описание продукта", 31000.0, 14,
                          3.36, "Redmi Note 11", "1024GB", "Gray")

lawn_grass1 = LawnGrass("Мятлик луговой, сорт Гранит", "Американский сорт газонного назначения",
                        48000.0, 10, "США", "21 день", "темно-зеленый")
# print(category_1)
# print()
# # Выводим список товаров для category_1
# print(category_1.products_list)
# # Выводим список товаров для category_2
# print(category_2.products_list)
# print(product_1)
# print(len(product_1))
# print()
# print(product_1 + product_2)
# print()
# print(f"Общее количество категорий товаров: {Category.total_categories}")
# print(f"Общее количество уникальных товаров: {Category.total_unique_products}")
# print(f"Категория товара: {category_1.name}")
# print(f"Описание категории: {category_1.description}")
# print(f"Список товаров в категории: {[product[0] for product in get_category_products(list_categories)
# ["Смартфоны"]]}")
# print(f"Категория товара: {category_2.name}")
# print(f"Описание категории: {category_2.description}")
# print(
#     f"Список товаров в категории: {[product[0] for product in get_category_products(list_categories)
#     ["Телевизоры"]]}"
# )
# print()
# print(f"Название продукта: {product_1.name}")
# print(f"Описание продукта: {product_1.description}")
# print(f"Цена продукта: {product_1.price}")
# print(f"Количество в наличии: {product_1.quantity}")
# print()
# print(f"Название продукта: {product_2.name}")
# print(f"Описание продукта: {product_2.description}")
# print(f"Цена продукта: {product_2.price}")
# print(f"Количество в наличии: {product_2.quantity}")
# print()
# print(f"Название продукта: {product_3.name}")
# print(f"Описание продукта: {product_3.description}")
# print(f"Цена продукта: {product_3.price}")
# print(f"Количество в наличии: {product_3.quantity}")
# print()
# print(f"Название продукта: {product_4.name}")
# print(f"Описание продукта: {product_4.description}")
# print(f"Цена продукта: {product_4.price}")
# print(f"Количество в наличии: {product_4.quantity}")
