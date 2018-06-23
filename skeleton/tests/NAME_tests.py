from nose.tools import *
import NAME
def setup():
    print("SETUP!")
def teadown():
    print("TEAR DOWN!")
def test_basic():
    print("I RAN!:", end='')
