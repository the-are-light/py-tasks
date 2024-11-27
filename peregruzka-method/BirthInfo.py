from functools import singledispatchmethod

from datetime import date
class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date): raise TypeError("Аргумент переданного типа не поддерживается")
    @__init__.register(date)
    def date_init(self, birth_date):
        if birth_date.year < date.today().year: self.birth_date = birth_date
        else: raise ValueError("Ты не родился ещё?")
    @__init__.register(tuple|list)
    def tuple_init(self, birth_date):
        if date(*birth_date).year < date.today().year: self.birth_date = date( *birth_date )
        else: raise ValueError("Ты не родился ещё?")
    @__init__.register(str)
    def str_init(self, birth_date):
        if date( *list(map(int, birth_date.split("-"))) ).year < date.today().year: self.birth_date = date( *list(map(int, birth_date.split("-"))) )
        else: raise ValueError("Ты не родился ещё?")
    def current_age(self):
        return f"""Current age: {
                date.today().year - self.birth_date.year,
                date.today().month - self.birth_date.month,
                date.today().day - self.birth_date.day
        } - format(YYYY-MM-DD)"""
    def age(self): return date.today().year - self.birth_date.year

birth = BirthInfo( "2006-02-19" )
print(birth.birth_date)
print(birth.current_age())
print(birth.age())
