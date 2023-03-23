# Калькулятор "цветной" патриотический
import math

# Цвета для калькулятора
from colorama import init
from colorama import Fore, Back, Style

# Чтобы работало на windows
init()

# Бесконечный цикл
while True:
    one = int(input(f"{Fore.LIGHTBLUE_EX}Введи число: "))  # Спрашиваем первое число
    operation = input(f"{Fore.LIGHTWHITE_EX}Что Делаем? (+, -, *, /, %, !, **(степень), √): ") # Спрашиваем пользователя операцию

    # Логика калькулятора
    # + - Сложение
    if operation == "+":
        two = int(input(f"{Fore.LIGHTBLUE_EX}Введи второе число: "))  # Спрашиваем второе число
        response = one + two
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")

    # - - Вычитание
    elif operation == "-":
        two = int(input(f"{Fore.LIGHTBLUE_EX}Введи второе число: "))  # Спрашиваем второе число
        response = one - two
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")
    
    # * - Умножение
    elif operation == "*":
        two = int(input(f"{Fore.LIGHTBLUE_EX}Введи второе число: "))  # Спрашиваем второе число
        response = one * two
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")
    
    # / - Деление
    elif operation == "/":
        two = int(input(f"{Fore.LIGHTBLUE_EX}Введи второе число: "))  # Спрашиваем второе число
        response = one / two
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")

    # % - Процент
    elif operation == "%":
        two = int(input(f"{Fore.LIGHTBLUE_EX}Введи второе число: "))  # Спрашиваем второе число
        response = one / two
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")

    # ! - Факториал
    elif operation == "!":
        print(f"{Fore.LIGHTRED_EX}Результат: {math.factorial(one)}")

    # ** - Степень
    elif operation == "**":
        two = int(input(f"{Fore.LIGHTBLUE_EX}Введи второе число: "))  # Спрашиваем второе число
        response = one ** two
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")

    #  √ - Корень
    elif operation == "√":
        response = math.sqrt(one)
        print(f"{Fore.LIGHTRED_EX}Результат: {str(response)}")

    # Иной случай
    else:
        print(f"{Fore.LIGHTRED_EX}error404 \nПроверьте написание символов")