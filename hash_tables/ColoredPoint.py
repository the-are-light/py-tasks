class ColoredPoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def __repr__(self):
        return f"ColoredPoint(<{self.x}>, <{self.y}>, '<{self.color}>')"
    def __eq__(self, other):
        if isinstance(other, ColoredPoint): return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return not (other == self)
        return NotImplemented

    def __hash__(self): return hash((self.x, self.y, self.color))

colorpoint = ColoredPoint(10, 10, 'red')
colorpoint2 = ColoredPoint(10, 10, 'red')
colorpoint3 = ColoredPoint(12, 14, 'green')
point = '10 10 red'
print(colorpoint == colorpoint2)
print(colorpoint3 != colorpoint)
print(colorpoint == point)
print(hash(colorpoint))
a = {colorpoint: 'hi', colorpoint2:'hello', colorpoint3:'hey'}
print(a)

