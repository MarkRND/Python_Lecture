# '3. Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# list = [3.1, 1.4, 3.1, 5.6, 9.81]
# print(list)

list = [3.1, 1.4, 3.1, 5.6, 9.81]
new_list = [i % 1 for i in list if i % 1 != 0]
subt = (max(new_list)) - min(new_list)
print()
print(list)
print(f'Разницу между максимальным и минимальным значением дробной части элементов: {round(subt,2)}')




def f1(n):
    res = str(n)
    fif = res.find('.')
    res = int('0.' + res[fif+1::])
    return res

def diff(mass):
    res=[]

    for i in mass:
        res.append(f1(i))
    print(max(res)-min(res))
a = [3.1, 1.4, 3.1, 5.6, 9.81]
diff[a]