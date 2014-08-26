#!/usr/bin/env python2
# encoding: utf-8
"""
File: main.py
Author: X4fyr
Email: benedikt_v@web.de
Github: x4fyr
Description: first draft
"""

from genesis.ui import *
from genesis.api import *


class Tor(CategoryPlugin):

    """Tor plugin for Genesis"""
    text = 'Tor'
    iconfont = 'gen-screen'
    folder = 'advanced'

    def on_init(self):
        """plugin init"""
        pass

    def on_session_start(self):
        """session start"""
        pass

    def get_ui(self):
        """create ui"""
        pass
