import pytest

from src.classes import Category, Product


@pytest.fixture
def category_1() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни",
        ["Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"],
    )


def test_init_1(category_1: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни"
    )
    assert category_1.products == ["Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]


@pytest.fixture
def category_2() -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником",
        ['55" QLED 4K'],
    )


def test_init_2(category_2: Category) -> None:
    assert category_2.name == "Телевизоры"
    assert category_2.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert category_2.products == ['55" QLED 4K']


@pytest.fixture
def product_4() -> Product:
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


def test_init_3(product_4: Product) -> None:
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7


def test_init_4() -> None:
    # Обнуляем счетчики
    Category.total_categories = 0
    Category.total_unique_products = 0

    # Создаем несколько экземпляров класса Category
    category_1_1 = Category("Смартфоны", "Описание смартфонов", ["iPhone", "Samsung", "Huawei"])
    category_2_1 = Category("Ноутбуки", "Описание ноутбуков", ["MacBook", "Lenovo", "Asus", "HP"])
    category_3_1 = Category("Телевизоры", "Описание телевизоров", ["Samsung", "LG", "Philips"])

    # Проверяем, что количество категорий равно 3
    assert Category.total_categories == 3

    # Обновляем значение Category.total_unique_products
    Category.total_unique_products = len(set(category_1_1.products + category_2_1.products + category_3_1.products))

    # Проверяем, что количество уникальных продуктов равно 9
    assert Category.total_unique_products == 9
