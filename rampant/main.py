#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation
"""
from typing import TypeVar, Union, NoReturn
from rampant.constant import ConstantGlobal, \
    ConstantScanner
from rampant import core, \
    net, \
    io, \
    malware, \
    phishing

_T: TypeVar = TypeVar('_T', object, Union[tuple, dict])


class Main(
    ConstantGlobal,
    ConstantScanner
):
    """
    show anything
    """
    @property
    def core(self):
        # type: () -> _T
        """
        show anything

        :return:
        """
        return core

    @property
    def malware(self):
        # type: () -> _T
        """
        show anything

        :return:
        """
        return malware

    @property
    def net(self):
        # type: () -> _T
        """
        show anything

        :return:
        """
        return net

    @property
    def phishing(self):
        # type: () -> _T
        """
        show anything

        :return:
        """
        return phishing

    @property
    def inout(self):
        # type: () -> _T
        """
        show anything

        :return:
        """
        return io


class RampantModules(Main):
    """
    show anything
    """
    def __init__(self, *args, **kwargs):
        # type: (_T, _T) -> NoReturn
        """
        show anything

        :param args:
        :param kwargs:
        """
        super(RampantModules).__init__(*args, **kwargs)
