'''
Властелин Чисел: Две Башни
Во времена, когда люди верили в великую силу чисел, оказалось, что волшебник Пифуман предал все народы и стал помогать Зерону.

Чтобы посетить башни обоих злодеев одновременно, нам следует разделить магию числа, которое защищало нас в дороге.

Чтобы поделить трёхзначное число, нам нужно составить из него минимально и максимально возможные двухзначные числа.

Формат ввода
Одно трёхзначное число.

Формат вывода
Два защитных числа для каждого отряда, записанные через пробел.
'''

number = int(input())

num_1 = str(number // 100 % 10)
num_2 = str(number // 10 % 10)
num_3 = str(number % 10)

number_1 = int(num_1 + num_2)
number_2 = int(num_2 + num_1)
number_3 = int(num_1 + num_3)
number_4 = int(num_3 + num_1)
number_5 = int(num_2 + num_3)
number_6 = int(num_3 + num_2)

num_max = max(number_1, number_2, number_3, number_4, number_5, number_6)
num_min = min(number_1, number_2, number_3, number_4, number_5, number_6)

if int(num_1) == 0:
    number_1 = int(num_2 + num_1)
    number_2 = int(num_2 + num_3)
    number_3 = int(num_3 + num_1)
    number_4 = int(num_3 + num_2)
    num_min = min(number_1, number_2, number_3, number_4)

if int(num_2) == 0:
    number_1 = int(num_1 + num_2)
    number_2 = int(num_1 + num_3)
    number_3 = int(num_3 + num_1)
    number_4 = int(num_3 + num_2)
    num_min = min(number_1, number_2, number_3, number_4)

if int(num_3) == 0:
    number_1 = int(num_1 + num_2)
    number_2 = int(num_1 + num_3)
    number_3 = int(num_2 + num_1)
    number_4 = int(num_2 + num_3)
    num_min = min(number_1, number_2, number_3, number_4)

print(num_min, num_max)
