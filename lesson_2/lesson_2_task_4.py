# Функция fizz_buzz принимает один аргумент (число n):
# Если число делится на 3, печатает Fizz.
# Если число делится на 5, печатает Buzz.
# Если число делится и на 3 и на 5, печатает FizzBuzz

num = int(input("Введите число: "))


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(num)