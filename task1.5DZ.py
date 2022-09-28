# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x, y, z = map(float,input('Введите значения X,Y,Z через "," : ').split(","))    
if (not (x or y or z) == (not x and not y and not z)):
    print(f"истина")
else:
    print(f"ложь")