import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class Test_File_Storage(unittest.TestCase):
    """test for class File Storage"""

    def test_not_run(self):
        """test for method test_not_run"""
        pass


if __name__ == "__main__":
    unittest.main()
