#!/usr/bin/python3
"""test User class"""

import unittest
import models
import datetime


class TestUser(unittest.TestCase):
    """test User class"""

    def test_not_run(self):
        """test for method test_not_run"""
        pass

    def test_documentation(self):
        """tests documentation"""
        self.assertIsNotNone(models.user.__doc__)
        self.assertIsNotNone(models.user.User.__doc__)


if __name__ == "__main__":
    unittest.main()
