class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    @property
    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = Student('Rolf', 'MIT')
rolf.marks = [78,99]

print(rolf.average)


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_object = Foo()
my_object.hi()



class Bar: 
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')
    
another_object = Bar()
another_object.hi()

