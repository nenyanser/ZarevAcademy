

# задание 1

"""
Напишите программу, которая генерирует случайное целое число между двумя введенными числами
и выводит сообщение о выводе токенов с биржи на кошелек
с указанной суммой
"""

import random
random_int = random.randint(1, 10)
print(f"C вашей биржи было успешно выведено ${random_int}kk, а надо было всего лишь не скипать модуль по безопасности.")


# задание 2

"""
Доработайте код так, чтобы при сложении переменной number и числа 10 получалось 25, при этом
использовать математические операции с числами запрещено, только встроенные функции
"""

number = -15
number = abs(number)
print(number + 10)


# задание 3

"""
Написать программу которая запрашивает число у пользователя через функцию input()
и выводит сообщение о том, является ли число четным или нечетным - True или False
"""

a = int(input())
print(a % 2 == 0)


# задание 4

"""
Создайте 3 переменные с характеристиками кошелька: баланс, количество транзакций, объем транзакций.
Создайте 4 переменные с минимальными критерием дропа: объем, количество транзакций, средняя сумма транзакции
и баланс и подставьте желаемые значения.
Обратите внимание что значение средней суммы транзакции у кошелька нужно высчитывать
на основе других переменных кошелька.
Чтобы быть Eligible нужно чтобы все значения были больше минимальных критериев.
Напишите программу, которая проверяет Eligible и выводит True или False, 
"""

print("Ну вот и подошли к концу первые голодные игры, введите свои параметры в чекер L0, чтобы узнать можете ли вы претендовать на дроп!")

my_balance = int(input("Введите баланс на момент снепшота 01.01.1970:"))
my_transactions = int(input("Введите количество транзакций на момент снепшота 01.01.1970:"))
my_volume = int(input("Введите общий объем на момент снепшота 01.01.1970:"))
my_avgtransactionvolume = my_volume / my_transactions

eligible_balance = 1000000
eligible_transactions = 5000
eligible_volume = 1000000000
eligible_avgtransactionvolume = eligible_volume / eligible_transactions

balance_check = my_balance >= eligible_balance
transactions_check = my_transactions >= eligible_transactions
volume_check = my_volume >= eligible_volume
avgtransactionvolume = my_avgtransactionvolume >= eligible_avgtransactionvolume

print(f"Проверяем баланс: {my_balance} >= {eligible_balance}, результат - {my_balance >= eligible_balance}.")
print(f"Проверяем количество транзакций: {my_transactions} >= {eligible_transactions}, результат - {my_transactions >= eligible_transactions}.")
print(f"Проверяем объем сделок: {my_volume} >= {eligible_volume}, результат - {my_volume >= eligible_volume}.")
print(f"Проверяем средний объем сделки: {my_avgtransactionvolume} >= {eligible_avgtransactionvolume}, результат - {my_avgtransactionvolume >= eligible_avgtransactionvolume}.")

if balance_check and transactions_check and volume_check and avgtransactionvolume:
    print("You're eligible!")
else:
    print("You're not eligible!")