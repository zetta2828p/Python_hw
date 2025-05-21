import unittest
from string_utils import StringUtils


class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_capitalize_positive(self):
        # Позитивный тест: обычная строка
        result = self.utils.capitalize('hello')
        expected_result = 'Hello'
        self.assertEqual(result, expected_result)

    def test_capitalize_negative_empty_string(self):
        # Негативный тест: пустая строка
        result = self.utils.capitalize('')
        expected_result = ''
        self.assertEqual(result, expected_result)

    def test_trim_positive(self):
        # Позитивный тест: удаление лишнего пробела вначале
        result = self.utils.trim('   hello ')
        expected_result = 'hello '
        self.assertEqual(result, expected_result)

    def test_trim_negative_empty_string(self):
        # Негативный тест с пустой строкой
        result = self.utils.trim('')
        expected_result = ''
        self.assertEqual(result, expected_result)

    def test_contains_positive(self):
        # Позитивный тест: проверка наличия символа в строке
        result = self.utils.contains('Python', 'P')
        expected_result = True
        self.assertEqual(result, expected_result)

    def test_contains_negative_not_found(self):
        # Негативная проверка: передаем несуществующий символ
        result = self.utils.contains('Python', 'X')
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_delete_symbol_positive_single_char(self):
        # Позитивная проверка: удаление одного символа из строки
        result = self.utils.delete_symbol('SkyPro', 'y')
        expected_result = 'SkPro'
        self.assertEqual(result, expected_result)

    def test_delete_symbol_negative_no_match(self):
        # Негативная проверка: удаление отсутствующего символа
        result = self.utils.delete_symbol('SkyPro', 'z')
        expected_result = 'SkyPro'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
