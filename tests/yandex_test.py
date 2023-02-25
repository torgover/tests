import unittest
from yandex import get_headers



class YandexTest(unittest.TestCase):
    def response_test(self):
        res = get_headers()
        self.assertIsInstance(res, str)



if __name__ == '__main__':
    unittest.main()