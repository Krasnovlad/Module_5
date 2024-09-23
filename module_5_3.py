class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


def __eq__(self, other):
    if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
        return self.number_of_floors == other


def __lt__(self, other):
    if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
        return self.number_of_floors < other.number_of_floors

def __add__(self, value):
    if isinstance(self.number_of_floors, int) and isinstance(value, int):
        self.number_of_floors += value
        return self.number_of_floors

def __radd__(self, value):
    if isinstance(self.number_of_floors, int) and isinstance(value, int):
        self.number_of_floors += value
        return self.number_of_floors
def __iadd__(self, value):
    if isinstance(self.number_of_floors, int) and isinstance(value, int):
        self.number_of_floors += value
        return self.number_of_floors
def __le__(self, other):
    if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
        return self.number_of_floors <= other.number_of_floors

def __gt__(self, other):
    if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
        return self.number_of_floors > other.number_of_floors

def __ge__(self, other):
    if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
        return self.number_of_floors >= other.number_of_floors

def __ne__(self, other):
    if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
        return self.number_of_floors != other.number_of_floors

print(f'Название: {h1.name}, количество этажей: {h1.number_of_floors}')
print(f'Название: {h2.name}, количество этажей: {h2.number_of_floors}')

eq = __eq__(h1, h2)
print(eq)

add = __add__(h1, 10)
print(f'Название: {h1.name}, кол-во этажей: {add}')

print(h1.number_of_floors == h2.number_of_floors)

iadd = __iadd__(h1, 10)
print(f'Название: {h1.name}, кол-во этажей: {iadd}')

radd = __radd__(h2, 10)
print(f'Название: {h2.name}, кол-во этажей: {radd}')

gt = __gt__(h1, h2)
print(gt)

ge = __ge__(h1, h2)
print(ge)

lt = __lt__(h1, h2)
print(lt)

le = __le__(h1, h2)
print(le)

ne = __gt__(h1, h2)
print(ne)







