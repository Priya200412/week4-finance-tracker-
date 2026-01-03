import unittest, os
from finance_tracker.expense import Expense
from finance_tracker import file_handler
class TestFileHandler(unittest.TestCase):
    def test_save_load(self):
        e = [Expense("2024-01-01", 100, "Food", "Test")]
        file_handler.save(e)
        data = file_handler.load()
        self.assertEqual(len(data), 1)
if __name__ == "__main__":
    unittest.main()
