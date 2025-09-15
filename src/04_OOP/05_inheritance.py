class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    @property
    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent1:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary
    
    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent2(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def __repr__(self):
        return f'Student: {self.name}, {self.school}, {self.salary}'

    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent2('Rolf', 'MIT', 15.50)
print(rolf)
rolf.marks = [57, 67, 34, 56]
#print(rolf.average())
print(rolf.average)
print(rolf.weekly_salary())
