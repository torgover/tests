import unittest
from unittest import TestCase, main
from dzz import max_value, ids_list


class MaxValueTest(unittest.TestCase):
    def test_get_max_value(self):
        max_vall = max_value()
        self.assertIn('yandex', max_vall)


    def test_type_maxvalue(self):
        max_val = max_value()
        self.assertNotIsInstance(max_val, list)
        self.assertIsInstance(max_val, str)


    @unittest.expectedFailure
    def test_len(self):
        res = max_value()
        self.assertLess(len(res), 4)


class ids_list_test(TestCase):
    def test_number_in(self):
        result = ids_list()
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, dict)


if __name__ == '__main__':
    main()
