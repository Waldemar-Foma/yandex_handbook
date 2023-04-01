'''
Зайка — 2
По пути домой родители вновь решили сыграть с детьми в поиск зверушек.

Формат ввода
Три строки описывающих придорожную местность.

Формат вывода
Строка в которой есть зайка, а затем её длина.
Если таких строк несколько, выбрать ту, что меньше всех лексикографически.
'''

first_side, second_side, third_side = input(), input(), input()
find_word = 'зайка'
length = len(first_side)
find_side = ''
if find_word in first_side:
    find_side = first_side
    length = len(first_side)
if find_word in second_side:
    if find_side >= second_side or find_side == '':
        length = len(second_side)
        find_side = second_side
if find_word in third_side:
    if find_side >= third_side or find_side == '':
        length = len(third_side)
        find_side = third_side
print(f"{find_side} {length}")
