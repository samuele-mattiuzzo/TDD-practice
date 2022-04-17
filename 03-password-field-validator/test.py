import unittest

from password_validator import ERROR_MESSAGES, password_validator


class TestPasswordFieldValidator(unittest.TestCase):

    def setUp(self):
        self.valid_password = '1aMval1d_'
        self.invalid_password = 'not1'

    def test_should_return_true_if_password_matches_conditions(self):
        valid, errors = password_validator(self.valid_password)

        self.assertTrue(valid)
        self.assertFalse(len(errors))

    def test_should_contain_all_error_messages_if_multiple(self):
        valid, errors = password_validator(self.invalid_password)

        self.assertFalse(valid)
        self.assertEqual(len(errors), len(ERROR_MESSAGES))

        joined_errors = '|'.join([err for err in errors])
        self.assertIn(ERROR_MESSAGES['LENGTH'], joined_errors)
        self.assertIn(ERROR_MESSAGES['NUMBERS'], joined_errors)
        self.assertIn(ERROR_MESSAGES['CAPITAL'], joined_errors)
        self.assertIn(ERROR_MESSAGES['SPECIAL'], joined_errors)


if __name__ == '__main__':
    unittest.main()
