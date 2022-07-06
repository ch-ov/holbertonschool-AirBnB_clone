#!/usr/bin/python3
"""test Place class"""

import unittest
import models
import datetime


class TestPlace(unittest.TestCase):
    """test Place class"""

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


if __name__ == "__main__":
    unittest.main()
