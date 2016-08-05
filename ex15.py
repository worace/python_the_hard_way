filename = "notes.org"

txt = open(filename)

print "here's your file: %r" % filename
print txt.read()

txt.close()

print "type open another file:"
second_file_name = raw_input("> ")

second_file = open(second_file_name)

second_file_contents = second_file.read()
second_file.close()
print second_file_contents
