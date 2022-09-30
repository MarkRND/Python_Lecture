 # Реализуйте алгоритм перемешивания списка.


import random


list = ['Реализуйте', 'алгоритм', 'перемешивания', 'списка']
print('Исходный список ->    ', list)
random.shuffle(list)
print('Перемешаный список -> ', list)


mass = [i for i in range(random.randint(3,6))]
print('Исходный список ->    ', mass)
random.shuffle(mass)
print('Перемешаный список -> ', mass)
