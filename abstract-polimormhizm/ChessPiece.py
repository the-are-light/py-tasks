from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.c = 'abcdefgh'
        if 1 <= vertical <= 8 and horizontal in self.c:
            self.horizontal =  horizontal
            self.vertical = vertical
        else: return NotImplemented
    @abstractmethod
    def can_move(self): pass

class King(ChessPiece):
    def __init__(self, horizontal, vertical): ChessPiece.__init__(self, horizontal, vertical)
    def can_move(self, h, v): return (self.c.index(h) - self.c.index(self.horizontal) == 1 or self.c.index(self.horizontal) - self.c.index(h) == 1) and (v - self.vertical == 1 or self.vertical - v == 1)

class Knight(ChessPiece):

    def __init__(self, horizontal, vertical): ChessPiece.__init__(self, horizontal, vertical)
    def can_move(self, h, v): return ((self.c.index(h) - self.c.index(self.horizontal) == 2 or self.c.index(self.horizontal) - self.c.index(h) == 2) and (v - self.vertical == 1 or self.vertical -v == 1)) or ( (self.c.index(h) - self.c.index(self.horizontal) == 1 or self.c.index(self.horizontal) - self.c.index(h) == 1) and (v - self.vertical == 2 or self.vertical - v == 2) )

from random import choice, randint

a = [choice([King, Knight])(choice(['a', 'b', 'c', 'd']), randint(1, 8)) for i in range(10)]
for i, item in enumerate(a): print(item.__str__(), item.horizontal, item.vertical, item.can_move('b', 2))