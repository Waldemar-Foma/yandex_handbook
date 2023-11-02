'''
Большое число
Дети никак не успокоятся и продолжают «мучить» числа. Сейчас они хотят общими силами составить очень большое число. 
Каждый ребёнок называет число состоящее из цифр, которые он знает. Напишите программу, которая строит число, 
состоящее из максимальных цифр каждого ребёнка.
'''

number_n = int(input())

result = ''

for _ in range(number_n):
    number = int(input())
    maximum = -1
    while number > 0:
        if number % 10 > maximum:
            maximum = number % 10
        number //= 10
    result += str(maximum)
    
print(result)
