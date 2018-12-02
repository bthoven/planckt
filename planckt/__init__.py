# -*- coding: utf-8 -*-

from __future__ import absolute_import
import sys

__version__ = "0.0.1"


# Get the Python version
pyversion = sys.version_info[0]

try:
    __PLANCKT_SETUP__
except NameError:
    __PLANCKT_SETUP__ = False

if not __PLANCKT_SETUP__:
    from .utils import Param

    if pyversion < 3:
        from . import lcdm
    else:
        import planckt.lcdm as lcdm

    __all__ = ["Param", "lcdm"]
