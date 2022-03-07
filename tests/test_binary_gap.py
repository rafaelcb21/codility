import unittest
from iterations_lesson_01.binary_gap import solution

# Command to execute the test:
# python -m unittest -v

class TestBinaryGap(unittest.TestCase):

    def test_binary_gap(self):
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(2), 0)
        self.assertEqual(solution(147), 2)
        self.assertEqual(solution(483), 3)
        self.assertEqual(solution(647), 4)

if __name__ == '__main__':
    unittest.main()
