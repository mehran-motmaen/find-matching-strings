import unittest
from src.main import StringMatcher


class TestStringListMatcher(unittest.TestCase):
    """
    Test cases for the StringMatcher class.
    """

    def setUp(self):
        """
        Set up the test environment by initializing a StringMatcher object with a sample list of strings.
        """
        self.matcher = StringMatcher(["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"])

    def test_matching_strings(self):
        """
        Test the find method with a target string that has matching strings in the StringMatcher's string_list.
        """
        result = self.matcher.find("eos")
        self.assertEqual(result, ["seo", "eso"])

    def test_no_matching_strings(self):
        """
        Test the find method with a target string that has no matching strings in the StringMatcher's string_list.
        """
        result = self.matcher.find("mehran")
        self.assertEqual(result, [])

    def test_empty_target_string(self):
        """
        Test the find method with an empty target string, expecting an empty list as a result.
        """
        result = self.matcher.find("")
        self.assertEqual(result, [])

    def test_case_insensitive_matching(self):
        """
        Test case-insensitive matching by modifying the setup to include case-insensitive strings.
        """
        self.matcher = StringMatcher(["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso", "EoS"])
        result = self.matcher.find("EoS")
        self.assertEqual(result, ["EoS"])


if __name__ == '__main__':
    unittest.main()
