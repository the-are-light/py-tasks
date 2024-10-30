
from math import acos
class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = x2 - x1
        self.y = y2 - y1

    def length(self): return (self.x**2+self.y**2) ** 0.5
    def arc(self): return acos(self.x / Vector.length(self))
    def summa(self, v2): return Vector( self.x1, self.y1, self.x2+v2.x, self.y2 + v2.y )
    def diff(self, v2): return Vector(self.x1, self.y1, self.x1 - v2.x, self.y1 - v2.y)
    def scalar(self, v2): return self.x * v2.x + self.y * v2.y

vector1 = Vector(2, 3, 4, 6)
vector2 = Vector(1, 5, 4, 1)

print(rf"""
Vector1 = {vector1.x, vector2.y}
Vector2 = {vector2.x, vector2.y}

Длина Vector1 = {vector1.length()}
Длина Vector2 = {vector2.length()}

Вычисления угла наклона вектора Vector1 по отношению к положительному направлению оси абсцисс = {vector1.arc()}
Вычисления угла наклона вектора Vector2 по отношению к положительному направлению оси абсцисс = {vector2.arc()}

Сумма векторов = {vector1.summa(vector2).x, vector1.summa(vector2).y}

Вычитание векторов = {vector2.diff(vector1).x, vector2.diff(vector1).y}

Скалярное произведение векторов = {vector1.scalar(vector2)}
""")
