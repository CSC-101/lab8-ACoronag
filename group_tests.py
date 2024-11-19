import group
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    def test_groups_of_three_1(self):
        result = group.groups_of_three([1,2,3,4,5,6,7,8,9,10,11])
        expected = [[1,2,3],[4,5,6],[7,8,9],[10,11]]
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()
