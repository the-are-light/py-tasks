from functools import singledispatchmethod

from datetime import date
class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date): raise TypeError("Аргумент переданного типа не поддерживается")
    @__init__.register(date)
    def date_init(self, birth_date): self.birth_date = birth_date
    @__init__.register(tuple)
    def tuple_init(self, birth_date): self.birth_date = date( *birth_date )
    @__init__.register(list)
    def list_init(self, birth_date): self.birth_date = date(*birth_date)
    @__init__.register(str)
    def str_init(self, birth_date): self.birth_date = date( *list(map(int, birth_date.split("-"))) )
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