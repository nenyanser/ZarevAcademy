# задание 1
'''
Придумай переменные имя, количество акков, сумма дропа, цена ламбо,
количество ламбо и подставь чтобы все считалось сами.
Используйте f строки
'''
name = "Max"
num_of_accs = 1000
drop_amount = 1000
price_of_lambo = 300000
full_drop = drop_amount * num_of_accs

print(f"Hello, Brayan, My name is {name}, I have {num_of_accs} accs LayerZero")
print(f"I want airdrop {drop_amount}$ for every acc")
print(f"Give me my drop = {drop_amount}$ * {num_of_accs} accs = {full_drop}$")
print(f"I want to buy Lambo, lambo price {price_of_lambo}$")
print(f"I want to buy {full_drop // price_of_lambo} Lambo")

# задание 2
'''
Поменяйте местами значения переменных name и surname не используя дополнительных переменных.
Дополните код так, чтобы переменная full_name содержала имя и фамилию через пробел
'''
surname = "Max"
name = "Zarev"
name, surname = surname, name
full_name = name + " " + surname
print(f"My name is {name}, my surname is {surname}")
print(f"My full name is {full_name}")

# задание 3
'''
Доработайте код чтобы он печатал 10, 20, 30, 40 используя переменную total
'''

total = 0
total = total + 10
print(total)
total = total + 10
print(total)
total = total + 10
print(total)
total = total + 10
print(total)


# задание 4
'''
Напишите программу-рецепт шаурмы, чтобы робот готовил шаурму с курицей, говядиной или овощами
с обычным лавашeм или лавашом с сыром
на старте программы вы должны написать какой лаваш использовать и какая будет начинка, 
а робот должен собрать шаурму и написать об этом в терминале
'''
print('Как тебя зовут?')
print('Привет,', name := input(), ', меня зовут Ахмед-Бот, я делаю цифровую шаурму, какую шаурму ты хочешь сегодня?')
print('Любая хорошая шаурма начинается с лаваша, но к сожалению, поставщик задерживается и на выбор у тебя только сырный и классический. Какой выбираешь?')
print('Отлично! Значит возьмем', lavash_type := input(), 'лаваш. Теперь перейдем к начинке. Тут как в самолете - мясо, рыба, курица?')
print('Супер! Значит у тебя будет', lavash_type, 'лаваш и', nachinka_type := input(), 'в качестве начинки!')
print('А теперь самое главное, соус, на выбор есть томатный и чесночный. Какой соус ты предпочтешь?')
print('Ну вот и готово! Вот твоя идеальная шаурма, я взял', lavash_type, 'лаваш, в качестве начинки тут', nachinka_type, ', а также я добавил', sauce_type := input(), 'соус, ну и конечно не забыл про секретный ингридиент!')
print('Кушай, не обляпайся,', name, ', с тебя 50 акков LayerZero.')