class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    @staticmethod
    def capitalize(string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        Пример: `capitalize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    @staticmethod
    def trim(string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале,
        если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        return string.lstrip()

    @staticmethod
    def contains(string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        return symbol in string

    @staticmethod
    def delete_symbol(string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ для удаления
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        return string.replace(symbol, "")
