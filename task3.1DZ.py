# '1. Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

num = int(input('Введите длинну списка: '))# 
list = [random.randint(-15,20)for i in range(num)]
result = 0
for i in range(1,len(list),2): 
    result += list[i]
print()
print(f'Сумма {list} -> {result}')

# def sumofunemen(mass):
#     for i in range(1,len(mass),2): 
#       result += mass[i]
# a = [random.randint(-15,20)for i in range()]
# print()  
# sumofunemen(a)  