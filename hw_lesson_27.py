"""
Домашнее задание по function typing
"""

# задание 1

"""
Переделайте программу из 25 урока на использование функций. Найдите логические блоки кода и реализуйте по ним функции.
В итоговой программе в верхней части определены функции, в нижней реализована логика с вызовом функций.
Итоговый код с логикой программы должен сократиться и стать более понятным.
"""

import random
import time

def create_activity_costs(activities):
    return {activity: random.randint(10, 100) for activity in activities}

def generate_wallets(number_of_wallets):
    return ["0x" + "".join(random.choice("abcdef0123456789") for _ in range(40)) for _ in range(number_of_wallets)]

def initialize_wallets(wallets_list):
    wallets_data = {}
    for wallet in wallets_list:
        wallets_data[wallet] = {
            "balances": {"ETH": random.uniform(0.2, 0.8), "USDC": random.randint(0, 50)},
            "transactions": 0,
            "activities": {"swap": 0, "mint_nft": 0, "burn_nft": 0}
        }
    return wallets_data

def adjust_gas_price(current_gas_price, gas_limit):
    while current_gas_price >= gas_limit:
        current_gas_price += random.choice([-1, 1])
        if current_gas_price <= 10:
            current_gas_price = 11
        elif current_gas_price >= 50:
            current_gas_price = 49
        print(f"Газ: {current_gas_price}")
        time.sleep(0.1)
    print(f"Газ достиг нужного значения: {current_gas_price}. Начинаем работу.")
    return current_gas_price

def process_activity(wallet, activity, activity_cost, gas_price, wallets_data, activity_costs):
    price_activity = (activity_cost * gas_price) / 10000
    current_balance = wallets_data[wallet]["balances"]["ETH"]

    if current_balance < price_activity:
        withdrawal_amount = price_activity * 2 * random.uniform(1.1, 1.2)
        wallets_data[wallet]["balances"]["ETH"] += withdrawal_amount
        print(f"Кошелек {wallet} вывел {withdrawal_amount} ETH с биржи для выполнения транзакции {activity}")

    if activity == "swap":
        eth_usdc_price = random.randint(2000, 3000)
        if wallets_data[wallet]["balances"]["USDC"] > 0:
            usdc_to_swap = wallets_data[wallet]["balances"]["USDC"]
            eth_received = usdc_to_swap / eth_usdc_price
            wallets_data[wallet]["balances"]["ETH"] += eth_received
            wallets_data[wallet]["balances"]["USDC"] = 0
        else:
            swap_amount = random.uniform(0, wallets_data[wallet]["balances"]["ETH"] - price_activity)
            wallets_data[wallet]["balances"]["ETH"] -= swap_amount
            wallets_data[wallet]["balances"]["USDC"] += swap_amount * eth_usdc_price

    wallets_data[wallet]["balances"]["ETH"] -= price_activity
    wallets_data[wallet]["transactions"] += 1
    wallets_data[wallet]["activities"][activity] += 1

    print(f"Кошелек {wallet} выполнил активность {activity} за {price_activity} ETH")

def perform_transactions(number_of_wallets, number_of_transactions, gas_limit):
    activities_list = ["swap", "mint_nft", "burn_nft"]
    activity_costs = create_activity_costs(activities_list)
    wallets_list = generate_wallets(number_of_wallets)
    wallets_data = initialize_wallets(wallets_list)
    gas_price = random.randint(10, 50)
    active_wallets = wallets_list[:]

    while active_wallets:
        wallet = random.choice(active_wallets)
        gas_price = adjust_gas_price(gas_price, gas_limit)

        activities = wallets_data[wallet]["activities"]
        if all(activities.values()) or not any(activities.values()):
            activity = random.choice(list(activities.keys()))
        else:
            zero_activities = [activity for activity in activities if not activities[activity]]
            activity = random.choice(zero_activities)

        process_activity(wallet, activity, activity_costs[activity], gas_price, wallets_data, activity_costs)

        if wallets_data[wallet]["transactions"] >= number_of_transactions:
            active_wallets.remove(wallet)

        gas_price += random.choice([-1, 1])
        if gas_price <= 10:
            gas_price = 11
        elif gas_price >= 50:
            gas_price = 49

        time.sleep(random.uniform(0.5, 1.5))

    return wallets_data

def print_wallet_summary(wallets_data):
    print("Итоговые данные по кошелькам:")
    for wallet, data in wallets_data.items():
        print(f"Кошелек {wallet}:")
        print(f"--- Баланс ETH: {data['balances']['ETH']}")
        print(f"--- Баланс USDC: {data['balances']['USDC']}")
        print(f"--- Количество транзакций: {data['transactions']}")
        print(f"--- Количество транзакций swap: {data['activities']['swap']}")
        print(f"--- Количество транзакций mint_nft: {data['activities']['mint_nft']}")
        print(f"--- Количество транзакций burn_nft: {data['activities']['burn_nft']}")

number_of_wallets = int(input("Сколько кошельков сделать: "))

while True:
    number_of_transactions = int(input("Сколько минимально сделать транзакций: "))
    if not number_of_transactions >= number_of_wallets:
        print(f"Я не могу сделать {number_of_transactions} транзакций, потому как их должно быть столько же или больше, сколько и кошельков. Сейчас кошельков: {number_of_wallets}. Давай попробуем еще раз.")
        continue
    break

gas_limit = 30
wallets_data = perform_transactions(number_of_wallets, number_of_transactions, gas_limit)
print_wallet_summary(wallets_data)