import unittest
from arrays_lesson_02.cyclic_rotation import solution

# Command to execute the test:
# python -m unittest -v

class TestCyclicRotation(unittest.TestCase):
    
    def test_cyclic_rotation(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 1), [6, 3, 8, 9, 7])
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
        self.assertEqual(solution([], 8), [])
        self.assertEqual(solution([3], 4), [3])
        self.assertEqual(solution([3, 8, 9, 7, 6], 999), [8, 9, 7, 6, 3])

if __name__ == '__main__':
    unittest.main
