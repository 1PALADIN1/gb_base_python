from typing import Optional


# Начальная сумма равна нулю:
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
OPER_PUT = 1
OPER_GET = 2
OPER_EXIT = 3
WEALTH_TAX_VALUE = 5_000_000

_transactions: [float] = []
_wallet: float = 0
_operations_count = 0


def start():
    print('Добро пожаловать в банк!')

    while True:
        operation, err = _show_operations()
        if err is not None:
            print(err)
            continue

        stop_prog = False
        if operation == OPER_EXIT:
            stop_prog = True
        elif operation == OPER_PUT:
            err = _put_money()
            if err is not None:
                print(err)
        elif operation == OPER_GET:
            err = _get_money()
            if err is not None:
                print(err)
        else:
            print('Некорректный ввод, повторите попытку...')
            continue

        if stop_prog:
            print('Программа завершена, до скорых встреч!')
            break


def _show_operations() -> (int, Optional[str]):
    try:
        operation = int(input('Выберете операцию:\n1 - пополнить\n2 - снять\n3 - выйти\n'))
    except Exception as e:
        return 0, str(e)

    return operation, None


def _put_money() -> Optional[str]:
    try:
        money = int(input('Введите сумму для пополнения:\n'))
        return _perform_operation(money, True)
    except Exception as e:
        return str(e)


def _get_money() -> Optional[str]:
    try:
        money = int(input('Введите сумму для снятия:\n'))
        return _perform_operation(money, False)
    except Exception as e:
        return str(e)


def _perform_operation(value: int, operation_put: bool) -> Optional[str]:
    _apply_wealth_tax(value)

    if value <= 0:
        return f'Неккоретное количество средства: {value}'

    # Сумма пополнения и снятия кратны 50 у.е.
    if value % 50 != 0:
        return f'Сумма должна быть кратна 50 у.е.'

    if operation_put:
        # пополнение
        _update_wallet(value)
    else:
        # снятие
        # Нельзя снять больше, чем на счёте
        value = _apply_get_commission(value)
        if _wallet < value:
            return 'Недостаточно средств на счете'

        _update_wallet(-value)

    _add_percent(value)
    return None


def _apply_wealth_tax(value: float):
    # При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
    if _wallet < WEALTH_TAX_VALUE:
        return

    tax = value * 0.1
    _update_wallet(-tax)


def _apply_get_commission(value: float) -> float:
    # Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    commission = value * 0.015
    if commission < 30:
        commission = 30

    if commission > 600:
        commission = 600

    return value + commission


def _add_percent(value: float):
    global _operations_count
    _operations_count += 1

    # После каждой третей операции пополнения или снятия начисляются проценты - 3%
    if _operations_count % 3 == 0:
        _update_wallet(value * 0.03)


def _update_wallet(diff: float):
    global _wallet
    _wallet += diff

    # Дополнительно сохраняйте все операции поступления и снятия средств в список.
    _transactions.append(diff)
    print(f'Транзакция выполнена: {diff}')
    # Любое действие выводит сумму денег
    print(f'Сумма: {_wallet}')
