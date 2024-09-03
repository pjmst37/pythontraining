import unittest
import testing_01


class TestTesting(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = testing_01.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'adfaf'
        result = testing_01.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


unittest.main()
