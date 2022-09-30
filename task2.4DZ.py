# '4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


num = int(input('Введите число N: '))
mass = []
for i in range(-num, num + 1):
    mass.append((i * 2) + 1)
print(mass)
p1 = int(input('Введите первую позицию элемента: '))
p2 = int(input('Введите вторую позицию элемента: '))
for i in range(len(mass)):
    result = mass[p1 - 1] * mass[p2 - 1]
print(f'Произведение элементов на позициях {p1} и {p2}: -> {result}')

num = int(input('Введите число N: '))

mass = [i for i in range(-num, num + 1)]
mult = 1
pos = list(map(int,input().split()))
for i in pos:
    mult*=mass[i]
print(f'Произведение элементов {mult}')