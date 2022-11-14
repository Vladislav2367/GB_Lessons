my_list = list(range(1, 11))
new_list = [n + 10 for n in my_list]
print(new_list)

my_list = list(range(1, 11))
new_list = [n + 10 if n % 2 == 0 else n ** 3 for n in my_list]  # исключение только для тернарного оператора
print(new_list)

new_list = [n + 10 for n in list(range(1, 11))]
print(new_list)


new_list = [n ** 3 for n in list(range(1, 11)) if n % 2 == 0 or n % 3 == 0]  # правильная запись для нескольких условий
print(new_list)

new_list = {i: i ** 3 for i in list(range(1, 11))}
print('\n', new_list)

new_list = {k: i ** 3 for k in "asdfghjkl" for i in list(range(1, 11))}
print('\n', new_list)

new_list = {}
for k in "asdfghjkl":

    for i in range(1, 11):
        new_list[k] = i ** 3

print(new_list)

new_list = {k: i ** 3 for k, i in zip("asdfghjkl", range(1, 11))}
print('\n', new_list)
