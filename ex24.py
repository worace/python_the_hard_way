print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(jelly_beans):
    jelly_beans = jelly_beans * 500
    jars = jelly_beans / 500
    crates = jars / 100
    return jelly_beans, jars, crates

start = 1000
list_return = secret_formula(start)
print "list return:", list_return
beans, jars, crates = secret_formula(start)

print "starting at %d" % start
print "now have %d beans, %d jars, and %d crates" % (beans, jars, crates)
