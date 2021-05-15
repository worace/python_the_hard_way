input_file = open("notes.org")

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

print "whole file:"

print_all(input_file)

print "rewind:"

rewind(input_file)

print "print 3 lines:"

current_line = 1
print_a_line(current_line, input_file)

current_line += 1
print_a_line(current_line, input_file)

current_line += 1
print_a_line(current_line, input_file)
