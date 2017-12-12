# coding=utf-8

from __future__ import print_function

import math as m

from gopigo.util.list_util import *


class Point(object):
    __coord = []

    def __init__(self, *coord):
        # type: (*float) -> None
        if coord is None:
            raise
        self.set_coord(coord)

    @staticmethod
    def mid_point_of(*points):
        # type: (*Point) -> Point
        sum_coords = [0.0] * len(max([len(point.coords) for point in points]))
        for point in points:
            dimension = 1
            while dimension <= len(point.coords):
                sum_coords[dimension] += point.coords[dimension]
                dimension += 1
        average_coords = [sum_coord / len(points) for sum_coord in sum_coords]
        return Point(average_coords)

    @staticmethod
    def distance_between(point1, point2):
        # type: (Point, Point) -> float
        return m.sqrt(sum(map(lambda x: x ** 2, diff_two_lists_values(point1.coord, point2.coord))))

    def equals(self, point):
        # type: (Point) -> bool
        if not self.get_dimension() == point.get_dimension():
            return False
        i = 0
        coord1, coord2 = self.get_coord(), point.get_coord()
        while i < len(coord1):
            if not coord1[i] == coord2[i]:
                return False
        return True

    def get_dimension(self):
        # type: () -> int
        return len(remove_zeros_at_end_of_list(self.__coord))

    def get_coord(self):
        # type: () -> list
        return self.__coord

    def set_coord(self, *coord):
        # type: (list) -> None
        self.__coord = remove_zeros_at_end_of_list(list(coord))

    def get_copy(self):
        # type: () -> Point
        return Point(self.get_coord())


p1, p2 = Point(0, 0, 0, 0), Point(1, 1, 1, 1)
print(Point.distance_between(p1, p2))
