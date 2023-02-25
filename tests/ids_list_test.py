import unittest
from dzz import ids_list

class IdsListTest(unittest.TestCase):
    def test_ids_list(self):
        res = ids_list()
        self.assertNotIsInstance(res, str)
        self.assertNotIsInstance(res, dict)
        self.assertIsInstance(res, list)
    
    
    def test_ids_in(self):
        val = ids_list()
        self.assertIn(54, val)
        self.assertNotIn(333, val)



if __name__ == '__main__':
    unittest.main()