# Создан класса
from user import User

# Создаем объект User
my_user = User("Оля", "Иванова")

# Доступ к полям и вывод данных
print(my_user.get_first_name())       # Вывод имени
print(my_user.get_last_name())        # Вывод фамилии
print(my_user.get_user_info())        # Вывод имени и фамилии в строке
