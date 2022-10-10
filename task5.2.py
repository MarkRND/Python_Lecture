# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

nums = [1, 5, 2, 3, 4, 6, 1, 7]
def ap(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
           ups.append(i)
    return ups
print(ap(nums))