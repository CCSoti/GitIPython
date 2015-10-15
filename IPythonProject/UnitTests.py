import copy

__author__ = 'SilviyaSoti'

import json
from pprint import pprint
import unittest
import githubparsing


# Unit Tests
class TestJSONMethods(unittest.TestCase):
    # read from json file
    with open('data_copy.json') as data_file:
        data = json.load(data_file)
    print "Data is ", data

    def test_file(self):
        self.assertDictEqual(self.data, githubparsing.git_ipython_repos())

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()