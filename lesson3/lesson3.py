# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
def task2():
    ls = [10, 23, 10, -2, 34, 0, -10, 30, 31, 23, 20, 23, 0, 0, 10, -2, -1]
    d = {}
    for item in ls:
        if item not in d:
            d[item] = 0

        d[item] += 1

    result = []
    for key in d:
        if d[key] == 1:
            result.append(key)
    print(f'Результат: {result}')


# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
MAX_WORDS = 10


def task3():
    d = {}
    with open('wiki.txt') as f:
        for line in f:
            for word in line.split(sep=' '):
                w = word.lower()
                for c in ',.:;-—':
                    w = w.replace(c, '')
                w = w.strip()
                if w == '':
                    continue

                if w not in d:
                    d[w] = 0

                d[w] += 1

    result = sorted(d.items(), key=lambda x: x[1], reverse=True)[:MAX_WORDS]
    print('Топ 10 слов статьи:')
    for i in range(MAX_WORDS):
        print(f'{i + 1}. {result[i][0]} - {result[i][1]}')


# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
def task4():
    backpack = {
        'Термос': 6,
        'Утюг': 7,
        'Штаны': 2,
        'Светильник': 5,
        'Тарелка': 4,
        'Котелок': 3,
        'Книга': 5,
        'Компас': 1,
    }

    total_weight = sum(backpack.values())
    max_weight = int(input(f'Введите макс. грузоподъёмность (общий вес: {total_weight})\n'))

    result = []
    weight = 0
    for k, v in backpack.items():
        if weight + v > max_weight:
            break

        weight += v
        result.append((k, v))

    print(f'Результат (вес {weight}): {result}')


task2()
task3()
task4()
