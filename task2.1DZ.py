# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число: ')
result = 0
for i in num:
    if i.isdigit():
        result += int(i)
print(f'Сумма цифр числа {num} -> {result}')


num = input('Введите вещественное число: ')
result = 0
for i in range(len(num)):
    if num[i] == '.':
        continue
    else:
        result += int(num[i])
print(f'Сумма цифр числа {num} -> {result}')
