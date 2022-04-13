import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_should_return_number_if_no_conditions_met(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_should_return_fizz_if_multiple_of_three(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_should_return_buzz_if_multiple_of_five(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_should_return_fizzbuzz_if_multiple_of_three_and_five(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')


if __name__ == '__main__':
	unittest.main()
