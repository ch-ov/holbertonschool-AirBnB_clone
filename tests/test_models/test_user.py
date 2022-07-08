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

    def test_class(self):
        """test instance class"""
        instance = models.user.User()
        self.assertIsInstance(instance, models.user.User)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.user.User()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)


if __name__ == "__main__":
    unittest.main()
