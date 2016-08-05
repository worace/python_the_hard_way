def print_multi_args(*args):
    print args

def print_two_args(arg1, arg2):
    print arg1
    print arg2


def print_none():
    print "HI"


print_multi_args(1,2,3,4)

print_two_args("left", "right")

print_none()


def another_func():
    print "...four spaces indented"
