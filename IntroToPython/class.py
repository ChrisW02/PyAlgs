class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distance(self, other):
        x_dif = (self.x - other.x) ** 2
        y_dif = (self.y - other.y) ** 2
        return (x_dif + y_dif) ** 0.5


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

    def set_name(self, new_name=""):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
