#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation
"""
import logging
from typing import Optional, TypeVar, NoReturn

_T: TypeVar = TypeVar('_T', object, Optional[str])


class RampantLogger:
    """
    show anything
    """
    __logger = logging.getLogger()
    __handler = logging.StreamHandler()
    __handler.setLevel(logging.WARNING)
    __logger.setLevel(logging.INFO)
    __logger.addHandler(__handler)

    def info(self, message, /):
        # type: (_T, ...) -> NoReturn
        """
        show anything

        :param message: message to show
        :return: nothing
        """
        self.__logger.info(message)

    def warning(self, message, /):
        # type: (_T, ...) -> NoReturn
        """
        show anything

        :param message: message to show
        :return: nothing
        """
        self.__logger.warning(message)

    def critical(self, message, /):
        # type: (_T, ...) -> NoReturn
        """
        show anything

        :param message: message to show
        :return: nothing
        """
        self.__logger.critical(message)
