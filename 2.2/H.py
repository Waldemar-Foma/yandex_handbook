'''
Зайка — 1
В долгой дороге дети могут капризничать, поэтому родители их развлекают с помощью игр. Одна из них — поиск различных зверушек в придорожной растительности.

Давайте немного поиграем и выясним, не спрятался ли зайка во введённом предложении.

Формат ввода
Строка описывающая придорожную местность.

Формат вывода
YES — если в этой местности есть зайка, иначе — NO.
'''

string = input()
if 'зайка' in string:
    print('YES')
else:
    print('NO')
