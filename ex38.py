# doing things to lists and class basics

a = [1,2,3]
a.append(4)
print a


class Thing(object):
    # takes self as first param
    def a_func(self, arg): print "arg in func: %s" % arg

a = Thing # reference the class
print a

a = Thing() # instantiate one
print a

a.a_func("pizza")

class Pizza:
    def hi(self, arg): print arg

Pizza().hi("lol")

ten_things = "Apples Oranges Crows Telephone Light Sugar"

ten_things = ten_things.split()

more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana",
              "Girl", "Boy"]

while len(ten_things) != 10:
    ten_things.append(more_stuff.pop(0))

print ten_things

print ten_things[1]
print ten_things[-1]

print ten_things.pop()

print " ".join(ten_things)

print ten_things[1:4]
print "#".join(ten_things[1:4])

