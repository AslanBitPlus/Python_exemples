# Задача 10: На столе лежат n монеток. Некоторые из них лежат 
# вверх решкой, а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет N : "))
o = 0
r = 0

for i in range(n):
    v = int(input(f"Монета - {i} :"))
    if v == 1:
        o += 1
    if v == 0:
        r += 1
if o > r:
    print(r)
else:
    print(o)
