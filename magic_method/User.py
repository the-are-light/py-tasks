class User:
    def __init__(self, name, age):
        if str(name).isalpha() and str(name) != '' and 0 < age <= 110:
            self.__name = name
            self._age = age
        else: raise ValueError("Некорекктно имя или возраст")

    @property
    def get_name(self): return self.__name
    @get_name.setter
    def set_name(self, v):
        if str(v).isalpha() and str(v) != '': self.__name = v
        else: raise ValueError("Некорректное имя")

    @property
    def get_age(self): return self._age
    @get_age.setter
    def set_age(self, age):
        if 0 < age <= 110: self._age = age
        else: raise ValueError("Некорректный возраст")
