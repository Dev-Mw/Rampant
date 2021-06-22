#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation
"""


class Writer(object):
    """
    show anything
    """
    def __init__(self):
        """
        show anything
        """
        self.__write()

    def __call__(self, *args, **kwargs):
        self.__write()

    @staticmethod
    def __write():
        """
        show anything
        """
        print("Writing")
