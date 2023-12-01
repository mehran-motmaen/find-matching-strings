class StringMatcher:
    def __init__(self, string_list:list):
        self.string_list = string_list

    def find(self, target_string):
        len_target = len(target_string)
        matching_strings = []
        target_chars_count = {char: target_string.count(char) for char in set(target_string)}

        for string in self.string_list:
            if len_target == len(string):
                if all(string.count(char) == target_chars_count.get(char, 0) for char in set(target_string)):
                    matching_strings.append(string)

        return matching_strings

# Example usage:
string_list = ["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"]
matcher = StringMatcher(string_list)

target_string = "eos"
result = matcher.find(target_string)

print(result)