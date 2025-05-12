# Создание класса
from user import User

# Создаем объект User
my_user = User("Оля", "Иванова")

# Доступ к полям и вывод данных
print(my_user.first_name)       # Вывод имени
print(my_user.last_name)        # Вывод фамилии
print(str(my_user))             # Вывод имени и фамилии в строке
