'''
Максимальная сумма
Ребята в детском саду снова играют с числами. И пусть числа они знают плохо, придумывать их они очень любят.
Они договорились, что будут называть числа по очереди и тот, кто назовёт число с наибольшей суммой цифр, будет 
считаться победителем. В качестве судьи они выбрали бедную воспитательницу, и она попросила нас о помощи. 
Напишите программу, которая определит победителя.
'''

count = int(input())

name_winner = ''
total = 0
for i in range(count):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if summa >= total:
        total = summa
        name_winner = name

print(name_winner)