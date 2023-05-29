from fractions import Fraction


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
    first_frac = input("Введите первую дробь:\n").split(sep='/')
    second_frac = input("Введите вторую дробь:\n").split(sep='/')

    first_numerator = int(first_frac[0])
    first_denominator = int(first_frac[1])
    second_numerator = int(second_frac[0])
    second_denominator = int(second_frac[1])

    check_first_frac = Fraction(first_numerator, first_denominator)
    check_second_frac = Fraction(second_numerator, second_denominator)

    print(f'Произведение дробей: {simplify_fraction(first_numerator * second_numerator, first_denominator * second_denominator)}')
    print(f'Произведение дробей (Fraction): {check_first_frac * check_second_frac}')

    if first_denominator != second_denominator:
        tmp = first_denominator
        first_numerator *= second_denominator
        first_denominator *= second_denominator
        second_numerator *= tmp
        second_denominator *= tmp

    print(f'Сумма дробей: {simplify_fraction(first_numerator + second_numerator, first_denominator)}')
    print(f'Сумма дробей (Fraction): {check_first_frac + check_second_frac}')


def simplify_fraction(numerator: int, denominator: int) -> str:
    val = denominator
    while val > 1:
        if numerator % val == 0 and denominator % val == 0:
            numerator //= val
            denominator //= val
            val = denominator
            continue

        val -= 1

    return f'{numerator}/{denominator}'


task2()
task3()
