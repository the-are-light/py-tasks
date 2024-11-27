from functools import singledispatchmethod
class Negator:
    @singledispatchmethod
    def neg(self, value): raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register(int)
    def int_neg(self, value): return -value

    @neg.register(bool)
    def bool_neg(self, value): return not value

negator = Negator()

print(negator.neg(3))
print(negator.neg(True))