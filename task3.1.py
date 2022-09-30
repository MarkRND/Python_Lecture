# 1)Дан список. Выведите те его элементы,
#  которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
import random
num = [random.randint(-15,100)for i in range(10)]
print(num)
mass = []
for i in num:
    if num.count(i) == 1:
        mass.append(i)
print(mass)