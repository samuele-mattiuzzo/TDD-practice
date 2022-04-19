import unittest

from search import DATABASE, search


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.invalid_search_term = 'a'  # invalid
        self.exact_search_text = 'Va'  # valencia, vancouver
        self.exact_search_text_mixed_case = 'vA'  # valencia, vancouver
        self.search_text_contained = 'an'  # bangkok, vancouver, istanbul
        self.search_wildcard_all = '*'  # DATABASE
        self.search_no_result = 'tre'  # []

    def test_less_than_two_chars_returns_no_results(self):
        self.assertEqual(search(self.invalid_search_term), [])

    def test_two_or_more_chars_returns_all_matching_cities(self):
        self.assertEqual(search(self.exact_search_text), ["Valencia", "Vancouver"])

    def test_two_or_more_chars_returns_all_matching_cities_case_insensitive(self):
        self.assertEqual(search(self.exact_search_text_mixed_case), ["Valencia", "Vancouver"])

    def test_two_or_more_chars_returns_all_matching_cities_case_insensitive(self):
        self.assertEqual(search(self.search_text_contained), ["Vancouver", "Bangkok", "Istanbul"])

    def test_wildcard_returns_all_all_cities(self):
        self.assertEqual(search(self.search_wildcard_all), DATABASE)

    def test_no_match_returns_empty_array(self):
        self.assertEqual(search(self.search_no_result), [])

if __name__ == '__main__':
    unittest.main()
