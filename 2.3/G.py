'''
НОК
Спустя время НИИ потребовалось находить наименьшее общее кратное (НОК) двух чисел. К нам вновь обратились за помощью.

Формат ввода
Вводится два натуральных числа, каждое на своей строке.

Формат вывода
Требуется вывести одно натуральное число — НОК двух данных чисел.
'''

first_number, second_number = int(input()), int(input())
if first_number > second_number:
    min = first_number
else:
    min = second_number
while min % second_number != 0 or min % first_number != 0:
    min += 1
print(min)
