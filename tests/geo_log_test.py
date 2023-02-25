import unittest
from dzz import *

class GeoLogTest(unittest.TestCase):
    def test_geo_log(self):
        ge_log = geo_log(listvalue=geo_logs, param='Россия')
        self.assertNotIsInstance(ge_log, dict)
        self.assertIsInstance(ge_log, list)
    
    
    @unittest.expectedFailure
    def test_len_geo_log(self):
        res = geo_log(listvalue=geo_logs, param="Россия")
        self.assertLess(len(res), 4)


if __name__ == '__main__':
    unittest.main()