# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
a=input("Введите число: ")
m = max([int(i) for i in str(a)])
print("самая большая цифра этого числа",m)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные
a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))

a = a + b
b = a - b
a = a - b

print('первое значение =', a)
print('второе значение =', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c;
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    import math

    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")