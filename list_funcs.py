
my_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0], my_list[1], my_list[2])
print('my list[0: 3] ',my_list[0: 3])
print('my list[:3]   ',my_list[:3])
print('my list[:len(my_list)]   ',my_list[:len(my_list)])
print('my list[:9] ', my_list[:9])
print('my list[:-1]', my_list[:-1])
print('my list[:]', my_list[:])
print('my list[3:]', my_list[3:])
print('my list', my_list[3::2])
print('my list', my_list[9::-1])
print('my list', my_list[-1::-1])

my_list.insert(5, 55)
print(my_list)