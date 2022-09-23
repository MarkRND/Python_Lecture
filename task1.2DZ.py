# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1, y1 = map(float,input('Введите две координаты точки A, через пробел: ').split())
x2, y2 = map(float,input('Введите две координаты точки Bб через пробел: ').split())
# x1 = int(input('Введите координаты первой точки A1: '))
# y1 = int(input('Введите координаты второй точки A2: '))
# x2 = int(input('Введите координаты первой точки B2: '))
# y2 = int(input('Введите координаты второй точки B2: '))3
result = (round(((x2 - x1) ** 2 + (y2 - y1) **2) ** (1 / 2), 2))
print(f'A ({x1},{y1}); B ({x2},{y2}) -> {result}')
