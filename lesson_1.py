author = 'Суменов Кермен'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
chislo1 = input(" Введите число")
for i in chislo1:
    print(i)
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = input("Введите пременную")
b = input("Введите другую пременную")
c = ''
c = a
a = b
b = c
print(a," это было b")
print(b," это было a")

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age=int(input("Сколько вам лет? "))
if age >= 18:
    print("Доступ разрешкн")
else:
    print("извените, пользование данным ресурсом только с 18 лет")

