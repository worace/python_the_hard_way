from nose.tools import *
import sample
import sample.math

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_square():
    assert(sample.square(2) == 4)

def test_negate():
    print sample.math.negate
    assert_equal( -1, sample.math.negate(1))
