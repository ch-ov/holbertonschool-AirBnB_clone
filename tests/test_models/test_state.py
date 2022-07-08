#!/usr/bin/python3
"""test State class"""

import unittest
import models
import datetime


class TestState(unittest.TestCase):
    """test State class"""

    def test_not_run(self):
        """test for method test_not_run"""
        pass

    def test_documentation(self):
        """tests documentation"""
        self.assertIsNotNone(models.state.__doc__)
        self.assertIsNotNone(models.state.State.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.state.State()
        self.assertIsInstance(instance, models.state.State)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.state.State()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
