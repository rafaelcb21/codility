import unittest
from arrays_lesson_02.odd_occurrences_in_array import solution, solution2

# Command to execute the test:
# python -m unittest -v

class TestOddOccurrencesInArray(unittest.TestCase):

    def test_odd_occurrences_in_array(self):
        self.assertEqual(solution([3]), 3)
        self.assertEqual(solution([2, 2, 2, 2, 2, 2, 3]), 3)
        self.assertEqual(solution([3, 4, 4, 4, 4, 4, 4]), 3)
        self.assertEqual(solution([7, 7, 7, 7, 6, 2, 2, 2, 2, 5, 5]), 6)
        self.assertEqual(solution([7, 7, 7, 7, 7, 2, 2, 2, 2, 5, 5]), 7)

        self.assertEqual(solution2([3]), 3)
        self.assertEqual(solution2([2, 2, 2, 2, 2, 2, 3]), 3)
        self.assertEqual(solution2([3, 4, 4, 4, 4, 4, 4]), 3)
        self.assertEqual(solution2([7, 7, 7, 7, 6, 2, 2, 2, 2, 5, 5]), 6)
        self.assertEqual(solution2([7, 7, 7, 7, 7, 2, 2, 2, 2, 5, 5]), 7)

        # se todos os numeros tiverem um par, o XOR retornará ZERO = false
        self.assertEqual(solution2([3, 3]), 0)
        self.assertEqual(solution2([2, 2, 2, 2, 2, 2, 3, 3]), 0)
        self.assertEqual(solution2([3, 4, 4, 4, 4, 4, 4, 3]), 0)
        self.assertEqual(solution2([7, 7, 7, 7, 6, 2, 2, 2, 2, 5, 5, 6]), 0)

if __name__ == '__main__':
    unittest.main