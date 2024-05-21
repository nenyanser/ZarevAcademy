# задание 1

"""
Найти информацию об форматировании float чисел в f-строчках и попробовать написать код,
который будет округлять число для вывода в терминале без функции round()
f"Ваше число: {number}"
"""

balance = 10.55051651
print(f"Ваше число: {balance:.1f}")


# задание 2

"""
Написать программу которая имитирует вывод случайной суммы токенов ETH с биржи,
код должен генерировать случайную сумму вывода между 0.001 и 0.09 с округлением до 4 символов после точки.
И выводить в терминале сообщение "Ваша сумма вывода: {случайное число} ETH"
"""

import random

a = random.uniform(0.001, 0.09)
rounded_a = round(a, 4)
print(f"Ваша сумма вывода: {rounded_a} ETH")