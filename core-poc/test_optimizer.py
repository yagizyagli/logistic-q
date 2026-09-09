"""
LogisticQ Unit Tests
Author: Yağız Yağlı
License: MIT
Description: Functional sanity checks for core quantum logic routing
"""

import unittest
import numpy as np
from optimizer import QuantumRouteOptimizer

class TestQuantumRouteOptimizer(unittest.TestCase):
    
    def setUp(self):
        self.nodes = 3
        self.optimizer = QuantumRouteOptimizer(nodes=self.nodes)
        
        # Matrix values explicitly structured to avoid empty bracket bugs
        r0 = [0, 10, 15]
        r1 = [10, 0, 35]
        r2 = [15, 35, 0]
        self.example_matrix = [r0, r1, r2]

    def test_distance_matrix_loading(self):
        self.optimizer.set_distance_matrix(self.example_matrix)
        self.assertIsNotNone(self.optimizer.distance_matrix)
        self.assertTrue(isinstance(self.optimizer.distance_matrix, np.ndarray))
        self.assertEqual(self.optimizer.distance_matrix.shape, (3, 3))

    def test_qubo_formulation_shape(self):
        self.optimizer.set_distance_matrix(self.example_matrix)
        qubo = self.optimizer.formulate_qubo()
        expected_size = self.nodes * self.nodes
        self.assertEqual(qubo.shape, (expected_size, expected_size))

    def test_classical_fallback_execution(self):
        self.optimizer.set_distance_matrix(self.example_matrix)
        route = self.optimizer.solve_classical_fallback()
        self.assertEqual(len(route), self.nodes + 1)
        self.assertEqual(route[0], 0)
        self.assertEqual(route[-1], 0)

if __name__ == "__main__":
    unittest.main()
