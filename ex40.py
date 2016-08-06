# modules classes and objects

def apple(): print "APLE FUNC"

top_var = "top level var"

class MyStuff(object):
    def __init__(self, tangerine):
        print "initing new obj"
        self.tangerine = tangerine

    def apple(self):
        print "instance method apple %s" % self.tangerine

an_object = MyStuff("lolol")
an_object.apple()



class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

