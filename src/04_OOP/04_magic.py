class Student:
    def __init__(self, name):
        self.name = name
        
movies = ['Matix', 'Finding Nemo', 'Marigold Hotel']

print(movies.__class__)
print('hi'.__class__)


class Garage:
    # Constructor method - called when creating a new instance of the class
    def __init__(self):
        self.cars = []

    # Defines behavior for len() function - returns the length of the object
    def __len__(self):
        return len(self.cars)

    # Defines behavior for indexing - allows using square brackets to access items
    def __getitem__(self, index):
        return self.cars[index]

    # Defines the "official" string representation - used by repr() and in debugging
    def __repr__(self):
        return f'<Garage {self.cars}>'

    # Defines the "informal" string representation - used by str() and print()
    def __str__(self):
        return f'Garage with {len(self.cars)} cars.'

ford = Garage()
print(ford.cars)

ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)
print(len(ford))
print(ford[0])
print(ford)


