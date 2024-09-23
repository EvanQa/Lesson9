# import random
# #index                 0  1   2  3    4      len == 4
# numbers: list[int] = [10, 2,-1, 12] #error
# print("numbers[0]:",numbers[0])
# print("numbers[1]:",numbers[1])
# print("numbers[2]:",numbers[2])
# print("numbers[0]:",numbers[3])
#
# print("len numbers",numbers[ len(numbers)-4])
#
# #create a list of 10 numbers from 1-10
# numbers_1_10: list[int] = []
# for i in range(1, 10+ 1, 1):
#     numbers_1_10.append(i ** 2)
# print("numbers_1_10:", numbers_1_10)
#
# #create list of 10 random numbers, each numbers between 1-100
# numbers_random: list[int] = []
# for _ in range(10):
#     rand_number = random.randint(1, 100)
#     numbers_random.append(rand_number)
# print("numbers_random:", numbers_random)
import random
import statistics
num_random: list[int] = []
for _ in range(10):
    rand_numbers = random.choice([1, 3,-5,12])
    num_random.append(rand_numbers)
print(num_random)
print(f"statistic is: ", {statistics.mean(num_random)})








#
# l1: list[int] = []
# for _ in range(10):
#     numbers: int = int(input('enter a numbers: '))
#     l1.append(numbers)
# import statistics
# print(f"len of list: {len(l1)}")
# # print(f"max num of list: {max(l1)}")
# print(f"min num of list: {min(l1)}")
# print(f"statistic of list: {statistics.mean(l1)}")
#
# max_number: int = l1[0]
# for i in range(1, len(l1)):
#     if l1[i] > max_number:
#         max_number = l1[i]
# print('maximum is: ', max_number)
#
# for i in range(len(l1)):
#     if l1[i] % 2 == 0:
#         print(l1[i])
