import unittest
from finance_tracker.expense import Expense
class TestExpense(unittest.TestCase):
    def test_valid(self):
        e = Expense("2024-01-01", 100, "Food", "Lunch")
        self.assertEqual(e.amount, 100)
    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            Expense("2024-01-01", -10, "Food", "Test")
if __name__ == "__main__":
    unittest.main()
