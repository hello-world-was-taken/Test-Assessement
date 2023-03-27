import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    def test_upper(self):
        ''' Test the to_upper function with various inputs and expected outputs '''
        self.assertEqual(to_upper('hello'), 'HELLO')
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("HELLO"), "HELLO")
        self.assertEqual(to_upper("Hello"), "HELLO")
        self.assertEqual(to_upper(""), "")
        self.assertEqual(to_upper(" "), " ")
        self.assertEqual(to_upper("123"), "123")
        self.assertEqual(to_upper("hello world"), "HELLO WORLD")


class TestToLower(unittest.TestCase):
    def test_lower(self):
        ''' Test the to_lower function with various inputs and expected outputs '''
        self.assertEqual(to_lower('HELLO'), 'hello')
        self.assertEqual(to_lower("HELLO"), "hello")
        self.assertEqual(to_lower("hello"), "hello")
        self.assertEqual(to_lower("Hello"), "hello")
        self.assertEqual(to_lower(""), "")
        self.assertEqual(to_lower(" "), " ")
        self.assertEqual(to_lower("123"), "123")
        self.assertEqual(to_lower("Hello World"), "hello world")


class TestCapitalize(unittest.TestCase):
    def test_upper(self):
        ''' Test the capitalize function with various inputs and expected outputs '''
        self.assertEqual(capitalize('hello'), 'Hello')
        self.assertEqual(capitalize("hello"), "Hello")
        self.assertEqual(capitalize("HELLO"), "Hello")
        self.assertEqual(capitalize("Hello"), "Hello")
        self.assertEqual(capitalize(""), "")
        self.assertEqual(capitalize(" "), " ")
        self.assertEqual(capitalize("123"), "123")
        self.assertEqual(capitalize("hello world"), "Hello world")

if __name__ == '__main__':
    unittest.main()
