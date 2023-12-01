class StringMatcher:
    def __init__(self, string_list: list):
        """
        Initialize the StringMatcher object.

        Parameters:
        - string_list (list): A list of strings to be used for matching.
        """
        self.string_list = string_list

    def find(self, target_string: str) -> list:
        """
        Find strings in the StringMatcher's string_list that match the given target_string.

        Parameters:
        - target_string (str): The string to find matches for.

        Returns:
        - list: A list of strings from string_list that match the target_string.
        """
        len_target = len(target_string)
        matching_strings = []

        # Count occurrences of each character in the target string
        target_chars_count = {char: target_string.count(char) for char in set(target_string)}

        for string in self.string_list:
            if len_target == len(string):
                # Check if the character counts in the current string match the target string
                if all(string.count(char) == target_chars_count.get(char, 0) for char in set(target_string)):
                    matching_strings.append(string)

        return matching_strings

