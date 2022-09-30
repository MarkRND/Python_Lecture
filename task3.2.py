# 2) Задайте список. Напишите программу, 
# которая определит, присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

list = input('Введите список').split()
print(list)
z = False
for i in list:
    if i.isdigit():
        print("Да, присутствует")
        z = True
        break
if z == False:
   print('нет')
   