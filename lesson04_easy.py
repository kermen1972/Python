# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

my_list = [1, 2, 4, 0]
sq_list = [a ** 2 for a in my_list]
print(sq_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list = ['банан', 'апельсин', 'яблоко', 'груша']
another_list = ['киви', 'банан', 'персик', 'яблоко']
sort_list = list (set (fruit_list) & set (another_list))
print(sort_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = [1, 2, 4, 9, 0, -3, 16, -23, -9]
sort_list = [el for el in my_list if el % 3 == 0 and el >=0 and el % 4 !=0]
print(sort_list)
