import unittest
from unittest.mock import MagicMock, patch
from src.json_loads import get_category_description, get_category_products, get_list_categories, get_name_of_categories


def test_get_name_of_categories_empty() -> None:
    assert get_name_of_categories([]) == []


def test_get_category_description_empty() -> None:
    assert get_category_description([]) == []


def test_get_category_products_empty() -> None:
    assert get_category_products([]) == {}


class TestGetListCategories(unittest.TestCase):

    @patch("builtins.open")
    def test_get_list_categories_valid_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"name": "Смартфоны", "price": 180000.0}]'
        list_categories = get_list_categories("test_file.json")
        self.assertEqual(list_categories, [{"name": "Смартфоны", "price": 180000.0}])

    @patch("builtins.open")
    def test_get_list_categories_empty_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        list_categories = get_list_categories("test_file.json")
        self.assertEqual(list_categories, [])

    def test_get_list_categories_file_not_found(self) -> None:
        list_categories = get_list_categories("nonexistent_file.json")
        self.assertEqual(list_categories, [])
