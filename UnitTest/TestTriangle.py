#!/usr/bin/env python
import unittest
import sys
sys.path.append('../')
from Triangle import Triangle


class TestTriangule(unittest.TestCase):

    def test_no_es_triangulo(self):
        param = [201, 0, 201]
        trian = Triangle(param)
        self.assertEqual('NotATriangle', trian.istriangle())

    def test_no_es_triangulo2(self):
        param = [8, 1, 3]
        trian = Triangle(param)
        self.assertEqual('NotATriangle', trian.istriangle())

    def test_triangle_equilateral(self):
        parametro = [4, 4, 4]
        trian = Triangle(parametro)
        self.assertEqual('Equilateral', trian.istriangle())

    def test_triangle_isosceles1(self):
        parametro = [3, 2, 2]
        trian = Triangle(parametro)
        self.assertEqual('Isosceles', trian.istriangle())

    def test_triangle_isosceles2(self):
        parametro = [8, 15, 8]
        trian = Triangle(parametro)
        self.assertEqual('Isosceles', trian.istriangle())

    def test_triangle_isosceles3(self):
        parametro = [5, 5, 8]
        trian = Triangle(parametro)
        self.assertEqual('Isosceles', trian.istriangle())

    def test_triangle_scalene(self):
        parametro = [7, 3, 4]
        trian = Triangle(parametro)
        self.assertEqual('Scalene', trian.istriangle())

if __name__ == "__main__":
    unittest.main()
