class Family:
    def __init__(self, mood='neutral'): self.mood = mood

class Father(Family):
    def __init__(self, mood='neutral'): Family.__init__(self, mood)
    def be_strict(self): self.mood = 'strict'
    def greet(self): return "Hello!"
class Mother(Family):
    def __init__(self, mood='neutral'): Family.__init__(self, mood)
    def be_kind(self): self.mood = 'kind'
    def greet(self): return 'Hi, honey!'
class Daughter(Mother, Father):
    def __init__(self, mood='neutral'): super().__init__(mood)
class Son(Father, Mother):
    def __init__(self, mood='neutral'): super().__init__(mood)
son = Son()
print(son.greet(), son.mood)