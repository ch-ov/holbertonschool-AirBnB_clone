#!/usr/bin/python3
"""test Amenity class"""

import unittest
import models
import datetime


class TestAmenity(unittest.TestCase):
    """test Amenity class"""

    def test_not_run(self):
        """test for method test_not_run"""
        pass

    def test_documentation(self):
        """tests module and class docstring"""
        self.assertIsNotNone(models.amenity.__doc__)
        self.assertIsNotNone(models.amenity.Amenity.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.amenity.Amenity()
        self.assertIsInstance(instance, models.amenity.Amenity)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.amenity.Amenity()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
