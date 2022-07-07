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


if __name__ == "__main__":
    unittest.main()
