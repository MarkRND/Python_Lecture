# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

mass = [1, 2, 3, 5, 1, 5, 3, 10]
mass2 = []
for i in range(len(mass)):
        if mass[i] not in mass[i+1::] and mass[i] not in mass[:i-1:]:
            mass2.append(mass[i])
print(f'{mass} -> {mass2}')