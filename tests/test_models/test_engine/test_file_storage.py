"""test file storage class"""

import unittest
import models
import datetime


class Test_File_Storage(unittest.TestCase):
    """test for class File Storage"""

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


if __name__ == "__main__":
    unittest.main()
