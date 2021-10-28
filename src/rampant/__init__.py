#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation
"""
from typing import TypeVar, Union, NoReturn
from rampant.main import RampantModules
from rampant.utils.logger import RampantLogger

_T: TypeVar = TypeVar('_T', object, str, Union[tuple, dict])


class Rampant(RampantModules):
    """
    Anything
    """
    def __init__(self, *args, **kwargs):
        # type: (_T, _T) -> NoReturn
        """
        show anything

        :param args:
        :param kwargs:
        """
        super(Rampant).__init__(*args, **kwargs)
        self.__logger = RampantLogger()

    def __del__(self):
        # type: () -> NoReturn
        """
        show anything

        :return: The log message in string format
        """
        self.__logger.warning(f'The object {self.__str__()!s} has been removed ')

    def __str__(self):
        # type: () -> _T
        """
        show anything

        :return:
        """
        return self.__class__.__name__
