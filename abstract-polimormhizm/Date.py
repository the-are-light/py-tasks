class Date:
    def __init__(self, yyyy, mm, dd):
        self.yyyy = yyyy
        self.mm = mm
        self.dd = dd

    def iso_format(self): return f"{self.yyyy}-{self.mm}-{self.dd}"


class USADate(Date):
    def __init__(self, yyyy, mm, dd): Date.__init__(self, yyyy, mm, dd)
    def format(self): return f"{self.mm}-{self.dd}-{self.yyyy}"

class ItalianDate(Date):
    def __init__(self, yyyy, mm, dd): Date.__init__(self, yyyy, mm, dd)
    def format(self): return f"{self.dd}/{self.mm}/{self.yyyy}"
usa_date = USADate(2023, 10, 5)
italian_date = ItalianDate(2023, 10, 5)

print(usa_date.format())
print(usa_date.iso_format())
print(italian_date.format())
print(italian_date.iso_format())