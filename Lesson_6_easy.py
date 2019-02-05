# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, A, B, C):

        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C

        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CA = side_len(self.C, self.A)

    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    # По формуле Герона расчитываем площадь треугольника
    def areaTriangle(self):
        semi_perimetr = self.perimeterTriangle() / 2
        return math.sqrt(semi_perimetr * (semi_perimetr - self.AB)
                         * (semi_perimetr - self.BC)
                         * (semi_perimetr - self.CA))

    def heightTriangle(self):
        return self.areaTriangle() * 2 / self.AB


treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))

print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())
print("-----------------------------")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Equ_Trapeze:
    def __init__(self, A, B, C, D):
        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CD = side_len(self.C, self.D)
        self.DA = side_len(self.D, self.A)

    def chec(self):
        if self.AB == self.CD:
            return "Данная трапеция является равнобокой"
        else:
            return "Данная трапеция НЕ является равнобокой"

    def SideLen(self):
        return "AB = {}, BC = {}, CD = {}, DA = {}"\
            .format(self.AB, self.BC, self.CD, self.DA)

    def PerimeterTrapeze(self):
        return self.AB + self.BC + self.CD + self.DA

    def AreaTrapeze(self):
        return (self.BC + self.DA) / 2\
               * math.sqrt(self.AB ** 2 - (self.BC - self.DA) ** 2 / 4)

trapeze1 = Equ_Trapeze((2, 2), (3, 5), (6, 5), (7, 2))

print(trapeze1.chec())
print(trapeze1.SideLen())
print(trapeze1.PerimeterTrapeze())
print(trapeze1.AreaTrapeze())
