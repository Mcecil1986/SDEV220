# test_tasks.py

import unittest
import tasks

class TestTasks(unittest.TestCase):

    def test_add_task(self):
        todo = []
        updated = tasks.add_task(todo, "Buy groceries")
        self.assertIn("Buy groceries", updated)
        self.assertEqual(len(updated), 1)

    def test_count_tasks(self):
        todo = ["Laundry", "Pay bills", "Call mom"]
        count = tasks.count_tasks(todo)
        self.assertEqual(count, 3)

if __name__ == "__main__":
    unittest.main()


"""
TEST RESULTS SUMMARY (in my own words):

The test runner executed both test methods inside the TestTasks class.
Each dot (.) in the output represents a passing test. Since both tests passed,
the final output shows "OK". This means the add_task() and count_tasks()
functions behaved exactly as expected for the inputs provided. If either
function returned an incorrect value, the test runner would show a failure
instead of "OK".
"""
