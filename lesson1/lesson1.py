from random import randint


# 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.
def task1():
    a = int(input("Введите a:\n"))
    b = int(input("Введите b:\n"))
    c = int(input("Введите c:\n"))

    if a + b < c or a + c < b or b + c < a:
        print("Треугольник не существует!")
        return

    if a == b and b == c:
        print("Треугольник равносторонний")
    elif a == b or b == c or c == a:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")


# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def task2():
    num = int(input("Введите число:\n"))
    if num <= 0 or num >= 100_000:
        print("Некорректное число")
        return

    div_count = 0
    for i in range(1, num, 1):
        if num % i == 0:
            div_count += 1
            print(i)

    if div_count > 1:
        print("Число составное")
    else:
        print("Число простое")


# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10


def task3():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print("Число загадано!")

    is_player_win = False
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        player_input = int(input(f"Попытка №{attempt + 1}, введите число:\n"))
        if player_input < 0 or player_input > 1000:
            print("Некорректное число, попробуйте снова")
            continue

        if player_input == num:
            is_player_win = True
            break
        elif num > player_input:
            print("Загаданое число больше")
        else:
            print("Загаданое число меньше")

        attempt += 1

    if is_player_win:
        print("Вы угадали число!")
    else:
        print("Попытки закончились, увы :(")


task1()
task2()
task3()
