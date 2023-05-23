# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
def task2():
    num = int(input("Введите целое число:\n"))
    if num < 0:
        print("Некорректное число")
        return
    if num == 0:
        print("Результат: 0")
        return

    check_num = hex(num)

    result = []
    while num > 0:
        hex_num = num % 16
        num //= 16

        match hex_num:
            case 10:
                result.append('a')
            case 11:
                result.append('b')
            case 12:
                result.append('c')
            case 13:
                result.append('d')
            case 14:
                result.append('e')
            case 15:
                result.append('f')
            case _:
                result.append(str(hex_num))

    result.reverse()
    print("Результат: 0x", ''.join(result), sep='')
    print("Функция hex:", check_num)


# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
def task3():
    pass


task2()
task3()
