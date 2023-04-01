'''
Легенды велогонок возвращаются: кто быстрее?
В новом сезоне за первенство в велогонках вновь борются лучшие из лучших. Протяжённость заключительной трассы — 43872м, и все хотят знать, кто получит золотую медаль.

Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Красивый пьедестал (ширина ступеней 8 символов).
'''

Petya_speed, Vasia_speed, Tolya_speed = int(input()), int(input()), int(input())

if Petya_speed > Vasia_speed and Petya_speed > Tolya_speed and Tolya_speed > Vasia_speed:
    print("""          Петя\n  Толя\n                  Вася""")
    print("""   II      I      III   """)
elif Petya_speed > Vasia_speed and Petya_speed > Tolya_speed and Tolya_speed < Vasia_speed:
    print("""          Петя\n  Вася\n                  Толя""")
    print("""   II      I      III   """)
elif Petya_speed > Vasia_speed and Petya_speed < Tolya_speed and Tolya_speed > Vasia_speed:
    print("""          Толя\n  Петя\n                  Вася""")
    print("""   II      I      III   """)
elif Petya_speed < Vasia_speed and Petya_speed > Tolya_speed and Tolya_speed < Vasia_speed:
    print("""          Вася\n  Петя\n                  Толя""")
    print("""   II      I      III   """)
elif Petya_speed < Vasia_speed and Petya_speed < Tolya_speed and Tolya_speed > Vasia_speed:
    print("""          Толя\n  Вася\n                  Петя""")
    print("""   II      I      III   """)
elif Petya_speed < Vasia_speed and Petya_speed < Tolya_speed and Tolya_speed < Vasia_speed:
    print("""          Вася\n  Толя\n                  Петя""")
    print("""   II      I      III   """)
