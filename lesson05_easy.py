# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Already exist")
a = input("enter something ")
print(a)
try:
    for i in range(3, 8):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")
# Задача-2:
# Напишите скрипт отображающий папки текущей директории
list = os.listdir()
for i in list:
    print(i)
# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт