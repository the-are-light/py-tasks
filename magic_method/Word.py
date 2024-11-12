class Word:
    def __init__(self, word):
        if str(word).isalpha(): self.word = word
        else: raise ValueError("Слово -  любая последовательность из одной или более латинских букв.")

    def __str__(self): return f"<{str(self.word).capitalize()}>"
    def __repr__(self): return f"Word('<{self.word}>')"

    def __eq__(self, other):
        if isinstance(other, Word): return len(self.word) == len(other.word)
        else: return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Word): return len(self.word) != len(other.word)
        else: return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Word): return len(self.word) >= len(other.word)
        else: return NotImplemented

    def __le__(self, other):
        if isinstance(other, Word): return len(self.word) <= len(other.word)
        else: return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word): return len(self.word) > len(other.word)
        else: return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word): return len(self.word) < len(other.word)
        else: return NotImplemented