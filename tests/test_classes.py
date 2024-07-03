import pytest

from src.classes import Category, Product


@pytest.fixture
def category_1() -> Category:
    products = [
        ("Samsung Galaxy C23 Ultra", 1000.0, 10),
        ("Iphone 15", 1200.0, 5),
        ("Xiaomi Redmi Note 11", 800.0, 20),
    ]
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни",
        products,
    )


def test_init_1(category_1: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    expected_products = [
        ("Samsung Galaxy C23 Ultra", 1000.0, 10),
        ("Iphone 15", 1200.0, 5),
        ("Xiaomi Redmi Note 11", 800.0, 20),
    ]
    assert [
        (product.name, product.price, product.quantity) for product in category_1._Category__products
    ] == expected_products


@pytest.fixture
def category_2() -> Category:
    products = [('55" QLED 4K', 123000.0, 7)]
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником",
        products,
    )


def test_init_2(category_2: Category) -> None:
    assert category_2.name == "Телевизоры"
    assert category_2.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    expected_products = [
        ('55" QLED 4K', 123000.0, 7),
    ]
    assert [
        (product.name, product.price, product.quantity) for product in category_2._Category__products
    ] == expected_products


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
    category_1_1 = Category(
        "Смартфоны", "Описание смартфонов", [("iPhone", 1000, 10), ("Samsung", 2000, 20), ("Huawei", 3000, 30)]
    )
    category_2_1 = Category("Телевизоры", "Описание телевизоров", [("Samsung", 5000, 5), ("LG", 6000, 6)])
    category_3_1 = Category("Ноутбуки", "Описание ноутбуков", [("Apple", 7000, 7), ("Asus", 8000, 8)])

    # Проверяем, что значения атрибутов экземпляров класса совпадают с ожидаемыми
    assert category_1_1.name == "Смартфоны"
    assert category_1_1.description == "Описание смартфонов"
    assert [(product.name, product.price, product.quantity) for product in category_1_1._Category__products] == [
        ("iPhone", 1000, 10),
        ("Samsung", 2000, 20),
        ("Huawei", 3000, 30),
    ]

    assert category_2_1.name == "Телевизоры"
    assert category_2_1.description == "Описание телевизоров"
    assert [(product.name, product.price, product.quantity) for product in category_2_1._Category__products] == [
        ("Samsung", 5000, 5),
        ("LG", 6000, 6),
    ]

    assert category_3_1.name == "Ноутбуки"
    assert category_3_1.description == "Описание ноутбуков"
    assert [(product.name, product.price, product.quantity) for product in category_3_1._Category__products] == [
        ("Apple", 7000, 7),
        ("Asus", 8000, 8),
    ]
    assert Category.total_categories == 3
    assert Category.total_unique_products == 7
