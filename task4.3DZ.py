# Задайте последовательность чисел.
# Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


import random
mass = [random.randint(1,10)for i in range(10)]
print(f"Исходный список --> {mass}")
new_mass = []
[new_mass.append(i) for i in mass if i not in new_mass]
print(f"Список из неповторяющихся элементов --> {new_mass}")