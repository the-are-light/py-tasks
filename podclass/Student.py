class Student:
    def __init__(self, first_name, last_name, group, averageMark):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.aMark = averageMark

class Bachelor(Student):
    def __init__(self, first_name, last_name, group, averageMark): Student.__init__(self, first_name, last_name, group, averageMark)

    def getScholarship(self):
        if self.aMark == 5: return 10000
        elif self.aMark > 3: return 5000
        else: return 0

class Undergraduate(Student):
    def __init__(self, first_name, last_name, group, averageMark, researchWork):
        Student.__init__(self, first_name, last_name, group, averageMark)
        self.researchWork = researchWork
    def getScholarship(self):
        if self.aMark == 5: return 15000
        elif self.aMark > 3: return 7500
        else: return 0

students = [
    Bachelor('Илья', 'Пряников', 14222, 5),
    Undergraduate('Артем', 'Корытов', 14234, 5,'Research AI')
]

for student in students: print(student.first_name, student.getScholarship())