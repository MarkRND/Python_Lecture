# Даны два файла, 
# в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов. 
#  2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

import sympy


with open('C:/GB_1/lecture_Py/file5.1DZ.txt', 'r') as file:
   list1 = file.read()
   print(list1)
with open('C:/GB_1/lecture_Py/file5.2DZ.txt', 'r') as file:
   list2 = file.read()
   print(list2)
sum = sympy.simplify(list1+ '+' + list2)
print(sum)
with open('C:/GB_1/lecture_Py/file5.3DZ.txt', 'w', encoding='utf-8') as file:
   file.write(str(sum))

