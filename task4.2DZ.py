# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
from unittest import result
import sympy
# import natural
num =  int(input("Введите натуральное число: "))
def number_list(num):
    result = []
    i = 2
    while i <= num:
        if sympy.isprime(i) and not num % i:
            result.append(i)
            num /= i
        else:
            i += 1
    print (f'Cписок простых множителей числа N--> {result}')
number_list(num)

