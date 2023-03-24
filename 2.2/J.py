'''
Лучшая защита — шифрование
Коля испугался, что Аня подсмотрит все его пароли в блокноте, и решил их зашифровать. 
Для этого он берёт изначальный пароль — трёхзначное число — и по нему строит новое число по следующим правилам:

находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы);
находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число.
Помогите реализовать алгоритм шифрования.

Формат ввода
Одно трёхзначное число

Формат вывода
Результат шифрования
'''

num = int(input())
num_1 = num // 100
num_2 = num // 10 % 10
num_3 = num % 10
res1 = num_2 + num_3
res2 = num_1 + num_2
if res1 > res2:
    print(res1, res2, sep='')
else:
    print(res2, res1, sep='')
