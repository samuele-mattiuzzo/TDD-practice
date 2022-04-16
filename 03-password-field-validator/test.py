import unittest

from password_validator import ERROR_MESSAGES, password_validator


class TestPasswordFieldValidator(unittest.TestCase):

    def setUp(self):
        self.valid_password = 'iamvalid'
        self.invalid_password = 'not'

    def test_should_return_true_if_password_is_eight_chars_long(self):

        self.assertTrue(password_validator(self.valid_password)[0])

        self.assertFalse(password_validator(self.invalid_password)[0])
        self.assertEqual(password_validator(self.invalid_password)[
            1], ERROR_MESSAGES['LENGTH'])


if __name__ == '__main__':
    unittest.main()
