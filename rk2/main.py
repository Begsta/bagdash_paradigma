import unittest
from functions import *
from data import *

class TestOperatorFunctions(unittest.TestCase):
    def setUp(self):
        self.languages = langs
        self.operators = ops
        self.ops_langs = ops_langs
        self.one_to_many = get_one_to_many(langs, ops)
        self.many_to_many = get_many_to_many(ops, langs, ops_langs)

    def test_func1(self):
        res_b1 = func1(self.one_to_many)
        self.assertEqual(res_b1[0], ('breakov', 'C++'))

    def test_func2(self):
        res_b2 = func2(self.one_to_many, self.languages)
        self.assertIn(('Python', 2), res_b2)
        self.assertIn(('C++', 2), res_b2)
        self.assertIn(('Java', 1), res_b2)

    def test_func3(self):
        res_b3 = func3(self.many_to_many, "ov")
        self.assertTrue(('breakov', 'C++') in res_b3)
        self.assertTrue(('breakov', 'Java') in res_b3)

if __name__ == '__main__':
    unittest.main()
