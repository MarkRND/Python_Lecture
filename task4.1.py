# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.



list = input('Введите список').split()
print(list)
print(min(list), max(list))