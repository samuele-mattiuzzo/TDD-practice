import unittest

from stringcalculator import stringcalculator


class TestStringcalculator(unittest.TestCase):
    
    def test_should_return_zero_if_empty_string(self):
        self.assertEqual(stringcalculator(''), 0)

    def test_should_return_number_if_only_one_present(self):
        self.assertEqual(stringcalculator('1'), 1)

    def test_should_return_sum_of_two_numbers(self):
        self.assertEqual(stringcalculator('1,2'), 3)

    def test_should_return_sum_of_all_numbers(self):
        self.assertEqual(stringcalculator('1,2,3'), 6)

    def test_should_return_sum_of_all_numbers_with_newline_delimiter(self):
        self.assertEqual(stringcalculator('1,2\n3'), 6)

    def test_should_raise_if_input_ends_with_delimiter(self):
        self.assertRaises(Exception, stringcalculator, '1,2,3,' )


if __name__ == '__main__':
	unittest.main()
