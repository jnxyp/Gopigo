# coding=utf-8
from __future__ import print_function
from gopigo.util.list_util import *

class Vector(object):
    magnitude = []

    def __init__(self, *magnitude):
        self.magnitude = remove_zeros_at_end_of_list(list(magnitude))



