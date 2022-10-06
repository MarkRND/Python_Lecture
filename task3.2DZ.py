# 2. Напишите программу,
#  которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

num = int(input('Введите длинну списка: '))
list = [random.randint(1, 10)for i in range(num)]
if len(list) % 2 != 0:
    size = len(list)//2 + 1
else:
    size = len(list)//2
works = [list[i]*list[len(list)-i-1] for i in range(size)]
print()
print(f'Gроизведение пар чисел списка :{list} -> {works}')



def sumofunemen(mass):
resmass = []
if len(mass) % 2 == 0:    
    for i in range(len(mass//2)):
        resmass.append(mass[i] * mass[len(mass) -1 -i])
else:
    for i in range(len(mass//2 + 1)):
        resmass.append(mass[i] * mass[len(mass) -1 -i])
a = [random.randint(1,10) for i in range(5)]
print(a)
print(sumofunemen(a))