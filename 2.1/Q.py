'''
Ошибка кассового аппарата
Мы уже помогали магазину с расчётами и формированием чеков, но сегодня кассовый аппарат вместо привычных продавцу десятичных чисел начал выдавать двоичные.
Техподдержка приедет только завтра, а магазин должен продолжать работать. Надо помочь.

Формат ввода
В первой строке записано десятичное число — общая сумма купленных в магазине товаров на данный момент.
Во второй строке указано двоичное число — сумма за последнюю покупку.

Формат вывода
Одно десятичное число — сумма прибыли за день с учётом последней покупки.
'''

n_1 = int(input())
n_2 = input()
result = int(n_2, 2)
print(result + n_1)
