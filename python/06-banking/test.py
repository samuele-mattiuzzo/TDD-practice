import unittest

from banking import Account


class MockAccount():
    def addToBalance(self, amount):
        pass

    def removeFromBalance(self, amount):
        pass

    def addToStatements(self, action):
        pass

    def getStatements(self):
        pass


class TestBanking(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()
