from abc import ABC, abstractmethod
from typing import Any, List

from src.mixinlog import MixinLog


class BaseProduct(ABC):
    @abstractmethod
    def create_product(self, *args: Any, **kwargs: Any) -> Any:
        pass


class Product(BaseProduct, MixinLog):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__repr__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if type(other) is self.__class__:
            self.sales_revenue = self.price * self.quantity
            other.sales_revenue = other.price * other.quantity
            return self.sales_revenue + other.sales_revenue
        else:
            raise TypeError

    def __len__(self) -> int:
        return len(self.description)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int) -> "Product":
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


class Smartphones(Product, MixinLog):
    performance: float
    model: str
    built_in_memory_capacity: str
    colour: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        performance: float,
        model: str,
        built_in_memory_capacity: str,
        colour: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.built_in_memory_capacity = built_in_memory_capacity
        self.colour = colour

    @classmethod
    def create_product(cls, *args: Any) -> "Smartphones":
        return cls(*args)


class LawnGrass(Product, MixinLog):
    country: str
    germination_period: str
    colour: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        colour: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.colour = colour

    @classmethod
    def create_product(cls, *args: Any) -> "LawnGrass":
        return cls(*args)


class Category:
    total_categories = 0
    total_unique_products = 0

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
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
            super().__repr__()

        # Увеличиваем счетчик общего количества категорий
        Category.total_categories += 1

        # Увеличиваем счетчик общего количества уникальных продуктов
        unique_products = []
        for product in self.__products:
            if product.name not in unique_products:
                unique_products.append(product)
                Category.total_unique_products += 1

    def __repr__(self: Any) -> Any:
        return super().__repr__()

    def add_product(self, product: Product) -> None:
        if product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        self.__products.append(product)

    def average_price(self) -> float:
        total_price = sum(product.price * product.quantity for product in self.__products)
        total_quantity = sum(product.quantity for product in self.__products)
        try:
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0

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
