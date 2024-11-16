class Shape:
    pass

class Cube(Shape):
    def __init__(self, a):
        self.a = a
        self.v = a**3
        self.s = 6 * a**2

    def __str__(self): return f"""
Куб:
Сторона: {self.a}
Площадь: {self.s}
Объём: {self.v}
"""

class Sphere(Shape):
    def __init__(self, r):
        self.r = r
        self.v = (4/3)* r**3 * 3.14
        self.s = 4 * 3.14 * r**2

    def __str__(self): return f"""
Сфера:
Радиус: {self.r}
Площадь: {self.s}
Объём: {self.v}
"""

class Cylinder(Shape):
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.s = 2*3.14*r*h + 2*3.14*r**2
        self.v = 3.14*r**2*h
    def __str__(self): return f"""
Цилиндр:
Радиус: {self.r}
Высота: {self.h}
Площадь: {self.s}
Объём: {self.v}
"""

class Parallelepiped(Shape):
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
        self.v = l*w*h
        self.s = 2* ( l*w + w*h + h*l )
    def __str__(self): return f"""
Параллелепипед: 
Длина: {self.l}
Ширина: {self.w}
Высота: {self.h}
Объем: {self.v}
Площадь: {self.s}"""

class Ellipse(Shape):
    def __init__(self, a ,b, c):
        self.a = a
        self.b = b
        self.c = c
        self.v = (4/3)*3.14*a*b*c
        p = 1.6075
        self.s =  4*3.14 * ( (a*b)**p + (c*b)**p  + (a*c)**p  ) ** (1/p)
    def __str__(self): return f"""
Эллипсоид: 
Полуоси: {self.a, self.b, self.c}
Объем: {self.v}
Площадь: {self.s}"""

def find_large_v(shapes):
    return [ shape for shape in shapes if shape.v >= sum(shape.v for shape in shapes) - shape.v ]


shapes = [
    Cube(3),
    Sphere(4),
    Cylinder(2, 5),
    Parallelepiped(2, 3, 4),
    Ellipse(1, 2, 3)
]

for shape in shapes: print(shape)

large_shapes = find_large_v(shapes)

if large_shapes:
    print("\nФигуры с объемом, равным или превышающим суммарный объем остальных фигур:")
    for shape in large_shapes: print(shape)
else: print("\nНет фигур с объемом, равным или превышающим суммарный объем остальных фигур.")