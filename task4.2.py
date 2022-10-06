# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python(sympy)
from sympy.solvers import solve
from sympy import Symbol
from math import sqrt


# a = int(input("Введите число А: "))
# b = int(input("Введите число B: "))
# c = int(input("Введите число C: "))

# d = b**2 - 4*a*c 
# print(d)

# x1 = (-b + sqrt(d)) / (2*a)
# x2 = (-b - sqrt(d)) / (2*a)
# print(x1, x2)



 
def fun(a,b,c):
    x = Symbol('x')
    return solve(f'{a}*x**2+{b}*x+{c}', x)
    
print('Корни уравнения:', *fun(1, -16, 28))  #  2 14