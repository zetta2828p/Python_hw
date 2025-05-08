# Високосный год - True, не високосный - False

def is_year_leap(number):
    if number % 4 != 0 or (number % 100 == 0 and number % 400 != 0):
        return False
    return True


num = int(input('Введите год: '))
result = is_year_leap(num)
print(f'год {num}: {result}')
