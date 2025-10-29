import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    def test_insert_and_search(self):
        self.tree.insert("01/01/2025", 13.2)
        self.assertEqual(self.tree.search("01/01/2025"), 13.2)
        self.tree.insert("02/01/2025", 38.6)
        self.assertEqual(self.tree.search("02/01/2025"), 38.6)

    def test_delete(self):
        self.tree.insert("01/01/2025", 13.2)
        self.tree.insert("02/01/2025", 38.6)
        self.tree.delete("01/01/2025")
        self.assertIsNone(self.tree.search("01/01/2025"))
        self.assertEqual(self.tree.search("02/01/2025"), 38.6)

    def test_balance(self):
        # Insert elements in a way that requires balancing
        for date, temp in [("01/01/2025", 13.2), ("02/01/2025", 38.6), 
                           ("03/01/2025", 25.8), ("04/01/2025", 23.7)]:
            self.tree.insert(date, temp)
        self.assertEqual(self.tree.root.key, "02/01/2025")   # Check root key after balancing
        self.assertEqual(self.tree.root.value, 38.6)         # Check root value after balancing

    def test_multiple_insertions(self):
        dates = [f"{i:02d}/01/2025" for i in range(1, 11)]
        temps = [i * 10 for i in range(1, 11)]
        for date, temp in zip(dates, temps):
            self.tree.insert(date, temp)
        for date, temp in zip(dates, temps):
            self.assertEqual(self.tree.search(date), temp)

if __name__ == '__main__':
    unittest.main()