import copy
import unittest
import utils

class ObjectifyTestCase(unittest.TestCase):

    def setUp(self):
        self.o = utils.Objectify()

    def test_bool_empty(self):
        self.assertFalse(self.o)

    def test_bool_not_empty(self):
        self.o['hello'] = 'world'
        self.assertTrue(self.o)

    def test_bool_false(self):
        self.o['hello'] = 'world'
        self.o['_bool'] = False
        self.assertFalse(self.o)

    def test_bool_true(self):
        self.o['_bool'] = True
        self.assertTrue(self.o)

    def test_dict(self):
        d = {'hello': 'world', 'thanks': 'mom'}
        o = utils.Objectify(copy.deepcopy(d))
        self.assertEqual(len(o), len(d))
        for key, value in d.items():
            self.assertEqual(o[key], value)
            self.assertEqual(getattr(o, key), value)
        self.assertEqual(unicode(o), unicode(d))
        self.assertEqual(str(o), str(d))

if __name__ == '__main__':
    unittest.main()