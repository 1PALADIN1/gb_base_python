import typing


# 1. Напишите функцию для транспонирования матрицы
def task1():
    m = [
        [2, 3, 4],
        [7, 8, 9],
    ]
    print(f'Результат для матрицы {m} -> {transpose_matrix(m)}')
    m = [
        [2, 7],
        [3, 8],
        [4, 9],
    ]
    print(f'Результат для матрицы {m} -> {transpose_matrix(m)}')


def transpose_matrix(m: [[int]]) -> [[int]]:
    result = []
    for row in m:
        i = 0
        for num in row:
            if len(result) <= i:
                col = [num]
                result.append(col)
            else:
                result[i].append(num)

            i += 1

    return result


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
def task2():
    result = convert_to_dict(a='123', b=329, c=23.09, test='test', f=sum)
    print(f'Результат: {result}')


def convert_to_dict(**kwargs) -> {}:
    d = {}
    for k, v in kwargs.items():
        if isinstance(v, typing.Hashable):
            d[v] = k
        else:
            d[str(v)] = k

    return d


# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
def task3():
    pass


# task1()
task2()
task3()
