# 3) Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# Пример:

a = input('Введите список').split()
b = input('Введите искомое')
print(a)
if a.count(b) > 1:
   i = a.find(b) 
   j = a[i+1:].find(b)
   print(j+i+1)
else:
    print("нет")
