import unittest
from finance_tracker.expense import Expense
from finance_tracker import reports
class TestReports(unittest.TestCase):
    def test_stats(self):
        e = [Expense("2024-01-01", 100, "Food", "A")]
        s = reports.stats(e)
        self.assertEqual(s["Total"], 100)
if __name__ == "__main__":
    unittest.main()
