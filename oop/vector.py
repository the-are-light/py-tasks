
from math import sqrt, acos
class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def cord(self):
        a = (self.x2-self.x1)
        b = (self.y2-self.y1)
        return a, b

    def length(self):
        a = Vector.cord(self)[0]
        b = Vector.cord(self)[1]
        return sqrt(a**2+b**2)

    def arc(self):
        a = (self.x2-self.x1)
        l = Vector.length(self)
        return acos(a/l)

    def sum(self, v2):

        x1, y1 = self.cord()
        x2, y2 = v2.cord()
        x, y = x1+x2, y1+y2
        return x, y

    def substract(self, v2):
        x1, y1 = self.cord()
        x2, y2 = v2.cord()
        x, y = x1-x2, y1-y2
        return x, y

    def scalar(self, v2):
        x1, y1 = self.cord()
        x2, y2 = v2.cord()
        x, y = x1 * x2, y1 * y2
        return x, y

vector1 = Vector(2, 3, 4, 6)
vector2 = Vector(1, 5, 4, 1)

print(rf"""
Vector1 = {vector1.cord()}
Vector2 = {vector2.cord()}

Длина Vector1 = {vector1.length()}
Длина Vector2 = {vector2.length()}

Вычисления угла наклона вектора Vector1 по отношению к положительному направлению оси абсцисс = {vector1.arc()}
Вычисления угла наклона вектора Vector2 по отношению к положительному направлению оси абсцисс = {vector2.arc()}

Сумма векторов = {vector1.sum(vector2)}

Вычитание векторов = {vector2.substract(vector1)}

Скалярное произведение векторов = {vector1.scalar(vector2)}
""")
