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


if __name__ == "__main__":
    unittest.main()
