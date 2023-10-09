import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False
    return True


def deposit(amount):
    """Пополнение счёта"""
    global bank_account, count
    if not check_multiplicity(amount):
        return False  # Операция не выполнена из-за некратной суммы
    count += 1
    bank_account += amount
    operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    return True


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    amount = check_multiplicity(amount)
    percent = amount * PERCENT_REMOVAL
    percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {percent}. Итого {bank_account} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {amount + percent} у.е. На карте {bank_account} у.е.')


def exit():
    """Завершение работы"""
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')
    return operations


# Пример использования
deposit(1000)
withdraw(200)
exit()

print(exit())
