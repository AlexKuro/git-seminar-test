""" 
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) 
"""

import random
a = random.randint(-5, 5)
b = random.randint(5, 10)
arr = []
ind = []
n = 10
rand = random.randint(-10, 20)
for i in range(n):
    arr.append(random.randint(-10, 20))

print(f"\nЗадан список: ---> {arr}")
print(f"Индексы, к которым принадлажат диапазону от {a} до {b}", end=' --> ')

for i in range(len(arr)):
    if a > arr[i] < b:
        ind.append(i)

print(f"{ind}\n")
