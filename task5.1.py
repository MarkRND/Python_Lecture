# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 
with open('C:/GB_1/lecture_Py/file5.1.txt', 'r') as file:
   data = file.read()
# for line in data:
print(data)

a = []
data = data.split()

a = list(map(int, data))


print(a)
for i in range(len(a)-1):
    if a[i]+1!= a[i+1]:
        print(a[i]+1)




# a = [1, 2, 3, 4 ,6]

# for i in range(len(a)-1):
#     if a[i]+1!= a[i+1]:
#         print(a[i]+1)

# for i in range(len(nums)):
#         if nums[i+1] - nums[i] > 1:
#             nums(i+1, nums[i] + 1)    
# print(nums) 