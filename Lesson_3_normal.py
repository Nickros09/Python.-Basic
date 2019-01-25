# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math

def fibonacci(n, m):
    first = 0
    second = 1
    res = []

    for i in range(m):
        if i >= n - 1:
            res.append(second)
        first, second = second, first + second
    return res


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    res = origin_list[:]
    for i in range(1, len(origin_list)):
        j = i
        while (res[j] < res[j - 1]) and (j > 0):
            res[j], res[j - 1] = res[j - 1], res[j]
            j -= 1
    return res
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(fun, lst):
    return [x for x in lst if fun(x)]
print(my_filter(lambda x: x > 0, [1, 2, 0, -2, 3, 0, 2]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a = (10, 10)
b = (6, 0)
c = (20, 0)
d = (24, 10)


def distance(n, m):
    x1, y1 = n
    x2, y2 = m
    return math.hypot(x2 - x1, y2 - y1)

if distance(a, b) == distance(c, d) and distance(b, c) == distance(a, d) and (a[0] + c[0])/2 == (b[0] + d[0])/2 and (a[1] + c[1])/2 == (b[1] + d[1])/2:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки НЕ являются вершинами параллелограмма')