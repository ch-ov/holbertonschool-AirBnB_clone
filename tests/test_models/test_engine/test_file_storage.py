"""test file storage class"""

import unittest
import models
import datetime
import os


class Test_File_Storage(unittest.TestCase):
    """test for class File Storage"""

    def test_not_run(self):
        """test for method test_not_run"""
        pass

    def test_documentation(self):
        """tests for documentation"""
        pep8_line = models.engine.file_storage.FileStorage
        self.assertIsNotNone(pep8_line.__doc__)
        self.assertIsNotNone(pep8_line.__doc__)
        self.assertIsNotNone(pep8_line.__init__.__doc__)
        self.assertIsNotNone(pep8_line.all.__doc__)
        self.assertIsNotNone(pep8_line.new.__doc__)
        self.assertIsNotNone(pep8_line.save.__doc__)
        self.assertIsNotNone(pep8_line.reload.__doc__)

    def test_class(self):
        """test FileStorage class"""
        instance = models.engine.file_storage.FileStorage()
        self.assertIsInstance(instance, models.engine.file_storage.FileStorage)

    def test_all(self):
        """test all method"""
        instance = models.engine.file_storage.FileStorage()
        dictionary = instance.all()
        self.assertIsNotNone(dictionary)
        self.assertIsInstance(dictionary, dict)
        self.assertIs(dictionary, instance._FileStorage__objects)

    def test_save(self):
        """test save method"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        instance = models.base_model.BaseModel()
        instance.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test reload method"""
        instance = models.engine.file_storage.FileStorage()
        dict1 = models.storage.all().copy()
        models.storage.reload()
        dict2 = models.storage.all().copy()
        self.assertEqual(len(dict1), len(dict2))
        instance.save()
        self.assertIsInstance(instance._FileStorage__file_path, str)
        self.assertIsInstance(instance._FileStorage__objects, dict)
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
