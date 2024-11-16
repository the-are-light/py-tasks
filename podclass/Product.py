class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self): return self.__name
    def get_price(self): return self.__price
    def get_weight(self): return self.__weight

    def set_name(self, v): self.__name = v

    def set_price(self, v): self.__price = v

    def set_weight(self, v): self.__weight = v

class Buy(Product):
    def __init__(self, name, price, weight, count):
        Product.__init__(self, name, price, weight)
        self.__count = count
        self.__totalprice = self.get_price() * self.__count
        self.__totalweight = self.get_weight() * self.__count
    def get_total_price(self): return self.__totalprice
    def get_total_weight(self): return self.__totalweight
    def get_count(self): return self.__count
    def set_coount(self, v): self.__count = v

class Check(Buy):
    def __init__(self, name, price, weight, count): Buy.__init__(self, name, price, weight, count)
    def print_check(self):
        print(f"Товар: {self.get_name()}")
        print(f"Цена за единицу: {self.get_price()}")
        print(f"Вес за единицу: {self.get_weight()}")
        print(f"Количество: {self.get_count()}")
        print(f"Общая цена: {self.get_total_price()}")
        print(f"Общий вес: {self.get_total_weight()}")

product_check = Check("Яблоко", 10, 0.2, 5)
product_check.print_check()