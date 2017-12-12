# coding=utf-8



# def merge_2_dict(dict1, dict2):
#     dict3 = dict1.copy()
#     dict3.update(dict2)
#     return dict3

# def merge_dicts(*dicts):
#     return reduce(merge_2_dict, dicts)

# dict1 = {1: 'hehe'}
# dict2 = {2: 'qunimade'}
# dict3 = {3: 'nishuoshijiushi?'}
#
# print merge_dicts(dict1, dict2, dict3)







class Polygon:
    center = None
    vertices = []

    def __init__(self, verties, center=None):
        if center is None:
            center = Point.mid_point_of(verties)
        else:
            self.center = center
        self.vertices = verties


class Distance_Data:
    center = None
    data = {}

    def __init__(self, center, degrees, distances, robot_direction=0.0, direction_offset=0.0):
        self.center = center
        i = 0
        while i < len(degrees):
            self.data.update((degrees[i] + direction_offset + robot_direction), distances[i])
        self.data = sorted(self.data, key=self.data.keys())
