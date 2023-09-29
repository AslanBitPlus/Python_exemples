# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:                 Вывод:
# 1 2 3 2 3             2

import random

size = random.randint(5, 10)
lst_1 = [random.randint(0, 10) for _ in range(size)]
print(lst_1)

count = 0
for i in range(0, size):
    for j in range(i + 1, size):
        if lst_1[i] == lst_1[j]:
            count += 1
print(count)


