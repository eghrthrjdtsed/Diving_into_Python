'''Задание №6 Напишите программу банкомат.
✔Начальная сумма равна нулю
✔Допустимые действия: пополнить, снять, выйти
✔Сумма пополнения и снятия кратны 50 у.е.
✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔Нельзя снять больше, чем на счёте
✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔Любое действие выводит сумму денег'''



class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = 0

    def deposit(self, amount):
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратна 50 у.е.")
            return
        if self.transactions % 3 == 0:
            print(f"Начислен процент: {self.balance * .03 :.2f} у.е.")
            self.balance += self.balance * .03
        self.balance += amount
        self.transactions += 1
        print(f"Вы пополнили счет на {amount :.2f} у.е. Баланс: {self.balance :.2f} у.е.")

    def withdraw(self, amount):
        if self.transactions % 3 == 0:
            self.balance += self.balance * .03
            print(f"Начислен процент: {self.balance * .03:.2f} у.е.")
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратна 50 у.е.")
            return
        if self.balance <= 5_000_000:
            withdrawal_fee = min(max(amount * 0.015, 30), 600)
            amount -= withdrawal_fee
        if self.balance < amount:
            print("Недостаточно средств на счете.")
            return
        self.balance -= amount
        self.transactions += 1
        print(f"Вы сняли {amount :.2f} у.е. Баланс: {self.balance:.2f}")

    def exit(self):
        print(f"Баланс: {self.balance :.2f} у.е.")
        if self.balance > 5_000_000:
            wealth_tax = self.balance * .10
            print(f"Баланс на момент завершения: {self.balance - wealth_tax:.2f} у.е.")
            self.balance -= wealth_tax
            print(f"Удержан налог на богатство: {wealth_tax :.2f} у.е.")
        print("Сессия завершена. До свидания!")


def main():
    account = ATM()

    while True:
        print("\nВыберите действие:")
        print("1. Пополнить счет")
        print("2. Снять деньги")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            amount = int(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        elif choice == '2':
            amount = int(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '3':
            account.exit()
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие снова.")


if __name__ == "__main__":
    main()
