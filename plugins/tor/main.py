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
from backend import Get


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
        ui = self.app.inflate('tor:main')
        try:
            get = Get(self)
        except:
            ui.remove("main")
            ui.remove("dlgClientConf")
            ui.remove("dlgRelayConf")
            ui.remove("dlgProxyFw")
        else:
            ui.remove("fault")
            status = get.status()
            ui.find("version").set("text", status["version"])
            ui.find("status").set("text", status["status"])
            ui.find("ext_ip").set("text", status["ext_ip"])
            ui.find("read").set("text", status["read"])
            ui.find("written").set("text", status["written"])

            # Dialog control
            if self._clientconfig is None:
                ui.remove("dlgClientConf")

            if self._relayconfig is None:
                ui.remove("dlgRelayConf")

            if self._proxyfw is None:
                ui.remove("dlgProxyFw")
            del get
        finally:
            return ui

    @event('button/click')
    def on_click(self, event, params, vars=None):
        """Allocate buttons"""
        if params[0] == 'btnClientConf':
            self._clientconfig = 1
        elif params[0] == 'btnRelayConf':
            self._relayconfig = 1
        elif params[0] == 'btnProxyFw':
            self._proxyfw = 1

    @event('dialog/submit')
    @event('form/submit')
    def on_submit(self, event, params, vars=None):
        """Handle form submits"""
        if params[0] == 'dlgClientConf':
            self._clientconfig = None
        elif params[0] == 'dlgRelayConf':
            self._relayconfig = None
        elif params[0] == 'dlgProxyFw':
            self._proxyfw = None
