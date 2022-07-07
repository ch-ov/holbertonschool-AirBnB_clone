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

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )

    def test_documentation(self):
        """tests documentation"""
        self.assertIsNotNone(models.user.__doc__)
        self.assertIsNotNone(models.user.User.__doc__)


if __name__ == "__main__":
    unittest.main()
