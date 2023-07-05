'''
НОД 2.0
В одном из местных НИИ часто требуется находить наибольший общий делитель (НОД) нескольких чисел. Вам уже доверяют, так что вновь пришли с этой задачей.

Формат ввода
В первой строке записано одно число N — количество данных. В каждой из последующих N строк записано по одному натуральному числу.

Формат вывода
Требуется вывести одно натуральное число — НОД всех данных чисел (кроме N).

Примечание
Самый распространённый способ поиска НОД — Алгоритм Эвклида.
'''

numbers = int(input())
second_number = int(input())

for i in range(1, numbers):
    first_number = int(input())
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    second_number += first_number
print(second_number)
