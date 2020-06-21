class Table:
    def __init__(self, l, w, h):
        self.lenght = l
        self.width = w
        self.height = h

class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p

    def square(self):
        return self.width * self.lenght

t1 = KitchenTable(3, 4, 1)

print(t1.square())