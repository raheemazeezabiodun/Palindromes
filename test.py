import unittest
from palindrome import reverse_string, is_palindrome, is_palindrome_v2, is_palindrome_v3


class TestReverseString(unittest.TestCase):
    def test_string(self):
        self.assertEqual(reverse_string('boy'), 'yob')
        self.assertEqual(reverse_string('niggas'), 'saggin')
        self.assertNotEqual(reverse_string('btoa'), 'atob')  # btoa == aotb


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('hannah'), True)
        self.assertEqual(is_palindrome('mallam'), True)
        self.assertEqual(is_palindrome('boom'), False)


class TestPalindromeV2(unittest.TestCase):
    def test_strings(self):
        self.assertEqual(is_palindrome_v2('racecar'), True)
        self.assertEqual(is_palindrome_v2('deed'), True)
        self.assertEqual(is_palindrome_v2('python'), False)
        self.assertTrue(is_palindrome_v2('hannah'))
