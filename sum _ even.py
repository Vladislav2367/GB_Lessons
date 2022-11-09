"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

sortList = []

even_numb = [i for i in range(100, 1001) if i % 2 ==0]
sum_all = reduce(lambda x, y: x + y, even_numb)

for el in even_numb:
   sortList.append(el)
   next

print(sortList[0:3])
print(sortList[-3:])

print(sum_all)