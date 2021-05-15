## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

print type(Animal())

class Dog(Animal):
    def __init__(self, name):
        self.name = name

d = Dog("fido")
print type(d)
print d.name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

c = Cat("sassy")
print type(c)
print c.name

class Person(object):
    def __init__(self, name):
        print "making a person..."
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

p = Person("horace")
print type(p)
print p.name

p.pet = c
print p.pet.name

class Employee(Person):
    def __init__(self, name, salary):
        print "making an employee..."
        super(Employee, self).__init__(name)
        self.salary = salary

e = Employee("toiler", 50000)
print type(e)
print e.name
print e.salary
print e.pet

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

flipper = Fish()

crouse = Salmon()

harry = Halibut()

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
    def override(self):
        print "PARENT override()"
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"



dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print "--------------"

dad.override()
son.override()

print "--------------"

dad.altered()
son.altered()
