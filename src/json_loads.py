import json

from main import json_file_path


def get_list_categories(json_file_path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает данные"""
    # noinspection PyBroadException
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            list_categories = json.load(file)
            if isinstance(list_categories, list):
                return list_categories
            else:
                return []

    except Exception:
        return []


get_list_categories(json_file_path)


def get_name_of_categories(list_categories: list) -> list:
    """Функция получает данные из JSON-файла и возвращает список категорий товаров"""
    name_categories = []
    for category in list_categories:
        if "name" in category:
            name_categories.append(category["name"])
    return name_categories


get_name_of_categories(get_list_categories(json_file_path))


def get_category_description(list_categories: list) -> list:
    """Функция получает данные из JSON-файла и возвращает описание категорий товаров"""
    descriptions = []
    for my_dict in list_categories:
        if "description" in my_dict:
            descriptions.append(my_dict["description"])
    return descriptions


get_category_description(get_list_categories(json_file_path))


def get_category_products(list_categories: list) -> dict:
    """Функция получает данные из JSON-файла и возвращает словарь,
    где ключ - категория товара, значение - список товаров в категории"""
    category_products = {}
    for category in list_categories:
        if "name" in category:
            category_name = category["name"]
            if "products" in category:
                products = []
                for product in category["products"]:
                    products.append(product["name"])
                category_products[category_name] = products
    return category_products


get_category_products(get_list_categories(json_file_path))
