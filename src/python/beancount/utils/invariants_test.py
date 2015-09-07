__author__ = "Martin Blais <blais@furius.ca>"

import itertools
import unittest
from beancount.utils import invariants


class Dummy:
    """Just a dummy class as a target to instrument."""
    counter = 0
    def foo(self):
        pass

class TestInvariants(unittest.TestCase):

    def setUp(self):
        incr = lambda obj: setattr(obj, 'counter', obj.counter + 1)
        invariants.instrument_invariants(Dummy, incr, incr)

    def tearDown(self):
        invariants.uninstrument_invariants(Dummy)

    def test_invariants_on_dummy(self):
        dummy = Dummy()
        dummy.foo()
        self.assertEqual(2, dummy.counter)
