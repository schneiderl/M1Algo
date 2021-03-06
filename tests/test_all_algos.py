# -*- coding: UTF-8 -*-

import types
import unittest
import algos

class TestAllAlgos(unittest.TestCase):
    def setUp(self):
        self.word = 'foo'
        self.wlist = ['foo', 'zzzz', 'bar', 'qux', 'z']
        def empty_gen():
            if False: yield
        def one_gen(): yield self.word
        self.empty = empty_gen()
        self.one   = one_gen()
    pass

def generate_tests(algo_name, func):
    """
    Add tests for the specified algorithm implementation
    """
    def test_empty(self):
        res = func(self.empty, 42)
        self.assertEqual(list(res), [[]])

    def test_one_word(self):
        res = func(self.one, 42)
        self.assertEqual(list(res), [[self.word]])

    def test_keep_all_words(self):
        res = func(self.wlist, 10)
        words = sorted([w for l in res for w in map(lambda w:w.strip(), l)])
        self.assertEqual(words, sorted(self.wlist))

    def test_keep_words_order(self):
        res = func(self.wlist, 10)
        words = [w for l in res for w in map(lambda w:w.strip(), l)]
        self.assertEqual(words, self.wlist)

    def test_line_length_more_than_0(self):
        width = max(map(len, self.wlist)) + 3
        res = list(func(self.wlist, width))
        self.assertTrue(len(res) > 0)
        self.assertTrue(len(res[0]) > 0)
        firstline = ' '.join(res[0])
        self.assertTrue(len(firstline) > 0)

    def test_line_length_no_more_than_width(self):
        width = 7
        res = list(func(self.wlist, width))
        lres = len(res)
        lres0 = len(res[0])
        self.assertTrue(lres > 0, "expected %d to be > 0" % lres)
        self.assertTrue(lres0 > 0, "expected %d to be > 0" % lres0)
        firstline = ' '.join(res[0])
        lfl = len(firstline)
        self.assertTrue(lfl <= width, 'expected %d to be <= %d' % (lfl, width))

    for attr, val in locals().items():
        if isinstance(val, types.FunctionType):
            name = attr + '_with_' + algo_name
            setattr(TestAllAlgos, name, val)

# Add all tests for each algorithm implementation
for (name, (func, _)) in algos.get_algos().items():
    generate_tests(name, func)
