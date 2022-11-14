"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""
sortList = []

q = (j for j in list(range(20, 241)) if j % 20 == 0 or j % 21 == 0)

for el in q:
   sortList.append(el)
   next

print(sortList)