# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))
bin = []
while num >= 1:
        bin.insert(0, num % 2)
        num = num // 2
print(bin)


num = int(input('Введите число: '))
print(bin(num))
print(str(bin(num))[2::])