class Counter:
    def __init__(self, start=0): self.value = start
    def inc(self, amount=1): self.value = self.value + amount if amount > 0 else self.value
    def dec(self, amount=1): self.value = max([0, self.value-amount])

class NonDeCounter(Counter):
    def __init__(self, start=0): Counter.__init__(self, start)
    def dec(self, amount=1): pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit
    def inc(self, amount=1): self.value = min(self.value + amount, self.limit) if amount >= 0 else self.value

counter = Counter(5)
counter.dec(2)
counter.inc(10)
print(counter.value)

nocounter = NonDeCounter(10)
nocounter.dec(10)
print(nocounter.value)

limitcounter = LimitedCounter(10)
limitcounter.inc(5)
print(limitcounter.value)