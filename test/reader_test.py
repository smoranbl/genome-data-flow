
import unittest


class TestReader(unittest.TestCase):

    def test_load_sheet(self):
        self.assertCountEqual(3, 3, 'Should be 3')


if __name__ == '__main__':
    unittest.main()
