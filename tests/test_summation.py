import unittest

from solver.utils import solve


class SolverTestCase(unittest.TestCase):

    def test_calculations(self):
        self.assertEqual(solve(1, 3), 4)
        self.assertIsInstance(solve(1, 2), int)
