my_name = "Horace"
my_age = 27
my_height = 69 # inches
my_weight = 190 # pounds
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Red"

print "Let's talk about %s" % my_name
print "he's %d inches tall" % my_height
print "he's got %s eyes and %s hair" % (my_eyes, my_hair)

eyes_and_hair = "he's got %s eyes and %s hair" % (my_eyes, my_hair)
print "can assign format string? ...", eyes_and_hair


print "if I add %d and %d I get %d" % (my_age, my_height, my_age + my_height)

print "can I use mixed types: %r and %r" % (my_age, my_eyes)

# format strings seem to typecast (%f will print float even for int)
print "float: %f and rounding... %f" % (1.0, round(1.0))
