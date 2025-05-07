# Функция month_to_season() принимает 1 аргумент (номер месяца) и возвращает название сезона, к которому относится этот месяц.
def month_to_season():
    if month in (12, 1, 2):
        return 'Зима'
    elif month in (3, 4, 5):
        return 'Весна'
    elif month in (6, 7, 8):
        return 'Лето'
    elif month in (9, 10, 11):
        return 'Осень'
    else:
        return 'Неверный номер месяца'

try:
    month: int = int(input("Введите номер месяца (1-12): "))
    print(month_to_season())
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")