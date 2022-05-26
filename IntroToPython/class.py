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


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_dif(self, other):
        dif = self.age - other.age
        print(abs(dif), "year difference.")

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)


import random


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have hw")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am playing csgo")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)


class Rabbit(Animal):

    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_opposite or parents_same
