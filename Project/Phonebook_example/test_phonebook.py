# This contains test cases for the phonebook.py

import unittest
from phonebook import Phonebook

# A testcase is created by subclassing unittest.TestCase
class PhonebookTest(unittest.TestCase):

# The setUp() and tearDown() methods allow you to define instructions that will
# be executed before and after each test method.
    def setUp(self):
        self.phonebook = Phonebook()

    def tearDown(self):
        pass

    def test_create_phonebook(self):
        pass

    def test_lookup_entry_by_name(self):
        # phonebook = Phonebook()
        self.phonebook.add('bob', '12345')
        self.assertEqual('12345', self.phonebook.lookup("bob"))

    def test_missing_entry_raises_KeyError(self):
        # phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # @unittest.skip("not complete")
    def test_empty_phonebook_is_consistent(self):
        # phonebook = Phonebook()
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("poor example")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("sue", "12345") #identical to bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("bob", "12345")
        self.phonebook.add("mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("bob", "12345")
        self.phonebook.add("mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.skip("not ready")
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("bob", "12345")
        self.phonebook.add("mary", "123")
        self.assertFalse(self.phonebook.is_consistent())

    # @unittest.skip("not ready")
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("sue", "12345")
        self.assertIn("sue", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())

# This block shows a simple way to run the tests. unittest.main() provides
# a command-line interface to the test script. Without this blcok, the test can
# be executed by the command -  "python3 -m unittest" and with this -
# python3 test_phonebook.py
if __name__ == "__main__":
    unittest.main()
