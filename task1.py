

# Задача 2
# Напишите программу, котрая принимает на вход два числа и проверяет, являються ли одно число квадратом другого

a = int(input('a = ')) # a = input().split() а = int(c[0]) b = int(c[1])
b = int(input('b = '))
if b**2 == a or a**2 == b:
    print('явл')
else:
    print('нет')

# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
a = input().split()
а = int(c[0])
b = int(c[1])
d = int(c[2])
e = int(c[3])
k = int(c[4])
max = a
# for i in range(5):

a = map(int,input().split())
print(a)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

a = int(input('a = '))
mass = []
for i in range(-a,a+1,1):
    mass.append(i)
print(mass)

#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
n = float(input())
d = int(n * 10) % 10
print(d)

a = input()
print (a.find('.'))
# print (a[a.find('.')+1])


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
a = int(input())
if (a % 5 == 0 and (a%10 ==0 or a%15 ==0)) and a%30 !=0:
    print('ok')
else:
    print('not ok')