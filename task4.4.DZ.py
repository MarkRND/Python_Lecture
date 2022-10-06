# Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов 
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

n = int(input('Введите число -> '))
result = ''
for i in range(n+1):
    if i == 0:
        result += str(random.randint(1,100)) + '*x**' + str(n-i)
    if i == n:
        result += ' + ' + str(random.randint(1,100))
    else:
        result += ' + ' + str(random.randint(1,100)) + '*x**' + str(n-i) 

with open('C:/GB_1/lecture_Py/file4.1DZ.txt', 'w', encoding='utf-8') as file:
    file.write(result)
print(f'k = {n} --> {result}')





# k = int(input('Введите число -> '))
# a = random.randint(0,100)
# b = random.randint(0,100)
# c = random.randint(0,100)
# result = ''
# if b == 0: result = f"{a}*x^{k} + {c}*x^{k-2} = 0"
# if b == 0 and c == 0: result =  f"{a}*x^{k} = 0"
# else: result =  f"{a}*x^{k} + {b}*x^{k-1} + {c}*x^{k-2} = 0 "
# with open('C:/GB_1/lecture_Py/file4.1DZ.txt', 'w', encoding='utf-8') as file:
#     file.write(result)
# print(f'k = {k} --> {result}')

