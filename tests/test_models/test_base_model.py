"""test module BaseModel"""

import unittest
import models
import datetime


class Test_Base_Model(unittest.TestCase):
    """test for class BaseModel"""

    def test_not_run(self):
        """test for method test_not_run"""
        pass

    def test_doc(self):
        """tests for documentation"""
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance, models.base_model.BaseModel)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_init(self):
        """test type of instance atributes"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_str(self):
        """test __str__ method"""
        instance = models.base_model.BaseModel()
        string = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_save(self):
        """test save method"""
        instance = models.base_model.BaseModel()
        date = instance.updated_at
        instance.save()
        self.assertLess(date, instance.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        instance = models.base_model.BaseModel()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(instance.__class__.__name__, dictionary["__class__"])
        self.assertEqual(instance.id, dictionary["id"])


if __name__ == "__main__":
    unittest.main()
