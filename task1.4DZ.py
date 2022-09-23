# Напишите программу,
# которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y)
quarter = int(input('Введите номер четверти: '))
def GetRange(q):
    if (q == 1):
         return " X > 0 и Y > 0"
    elif (q == 2):
         return " X < 0 и Y > 0"
    elif (q == 3):
         return " X < 0 и Y < 0"
    elif (q == 4):
         return " X > 0 и Y < 0"
    else:
         return "Введено некоректное значение"
result = GetRange(quarter)
print(f'Диапазон возможных координат точек в этой четверти: {result}')