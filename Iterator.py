"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного; итератор, повторяющий элементы некоторого списка,
определённого заранее. Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения. Например,
в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. Вторым пунктом
необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""

from itertools import count
from itertools import cycle

def printer_(a, b):

    v = []

    for el in count(a, 2):
        if el > b:
            break
        else:
           print(el)
           v.append(el)

        next
    print(v)

d = ",".join(v)

a = int(input("Enter first iteration number ",))
b = int(input("Enter the maximum iteration value is no more than ",))

printer_(a, b)



# с = 0
# for el in cycle d:  #("ABC"):
#     if с > 30:
#         break
#     print(el)
#     с += 1
