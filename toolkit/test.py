import unittest2 as unittest
import numpy as np

import formulas


class Formulas(unittest.TestCase):

    def test_euclidean_dist(self):
        x = np.array([2, -1])
        y = np.array([-2, 2])
        self.assertAlmostEqual(5.0, formulas.euclidean_distance(x, y))

    def test_cosine_dist(self):
        x = np.array([1, 1, 0, 1])
        y = np.array([2, 0, 1, 1])

        expected = 0.707107
        result = formulas.cosine_distance(x, y)

        self.assertAlmostEqual(expected, result, places=4)
