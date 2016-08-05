from os.path import exists
from time import time

from_file = "notes.org"

print "copy notes.org to /tmp"

in_file = open(from_file)
indata = in_file.read()

print "file length: %d bytes" % len(indata)

out_file = "/tmp/notes_%d.org" % int(time())

print "already exists? %r" % exists(out_file)

writer = open(out_file, "w")
writer.write(indata)

writer.close()
in_file.close()
