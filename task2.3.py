# 3. Напишите программу, в которой пользователь будет задавать две строки, а 
# программа - определять количество вхождений одной строки в другой.


from itertools import count


a = 'привет мир'
b = 'и'
count = 0
for i in range(len(a)- len(b)):
    if a[i: i+len(b)] == b:
        count+=1
print(count)