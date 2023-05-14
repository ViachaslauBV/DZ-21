# BV_DZ
# Бандик Вячеслав
# bvii@mail.ru
# ДЗ урок 6
# 14.05.2003

# Условия
# Домашка
# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

class Calculator:

    def addition(self):
        print(a + b)

    def subtraction(self):
        print(a - b)

    def multiplication(self):
        print(a * b)

    def division(self):
        print(a / b)


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
obj = Calculator()


choice = 1
while choice != 0:
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    choice = int(input("Enter your choice:"))
    pass
    if choice == 1:
        print(obj.addition())
    elif choice == 2:
        print(obj.subtraction())
    elif choice == 3:
        print(obj.multiplication())
    elif choice == 4:
        print(obj.division())
    else:
        print("Invalid choice")
    break
