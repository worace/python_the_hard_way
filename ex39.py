# Dictionaries

stuff = {'name': 'Zed',
         'age': 39,
         'height': 6 * 12 + 2}

print stuff
print type(stuff)
print stuff["name"]
print stuff.get("name")
print stuff.get('missing') # gives None

# print stuff['missing'] # errors with KeyError

print stuff.get("pizza", "default...")


states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print states
print "--------------"
print cities


print "michigan:"
print states["Michigan"]

print "enumerating a dict:"

for state, abbrev in states.items():
    print "%s stands for %s" % (abbrev, state)

for state, abbrev in states.items():
    print "%s has city: %s" % (state, cities[abbrev])


print states.keys()
print dict(map(lambda abbrev:
               [abbrev, cities[abbrev]],
               states.values()))
