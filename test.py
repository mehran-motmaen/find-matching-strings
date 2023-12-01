import unittest

from main import StringMatcher


class TestStringMatcher(unittest.TestCase):
    def setUp(self):
        # Initialize the StringMatcher with a sample list of strings
        self.matcher = StringMatcher(["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"])

    def test_matching_strings(self):
        result = self.matcher.find("eos")
        self.assertEqual(result, ["seo", "eso"])

    def test_no_matching_strings(self):
        result = self.matcher.find("xyz")
        self.assertEqual(result, [])

    def test_empty_target_string(self):
        result = self.matcher.find("")
        self.assertEqual(result, [])

    def test_case_insensitive_matching(self):
        result = self.matcher.find("Eos")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()