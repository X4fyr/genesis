#!/usr/bin/env python2
# encoding: utf-8
"""
File: backend.py
Author: X4fyr
Email: benedikt_v@web.de
Github: X4fyr
Description: backend oparations
"""

from stem.control import Controller


class Status(object):
    """Collecting and formatting status-data of tor"""
    GETINFO = {'config-file': 'config-file',
               'address-mapping': 'address-mappings/all',
               'ext-ip': 'address',
               'circ-stat': 'circuit-status',
               'read': 'traffic/read',
               'written': 'traffic/written',
               'uid': 'process/uid',
               'circ_est': 'status/circuit-established',
               'enough': 'status/enough-dir-info',
               'good': 'status/good-server-descriptor',
               'accepted': 'status/accepted-server-descriptor'}
    controller = Controller.from_port(port=9051)    # TODO: fetch from settings

    def __init__(self):
        """initiate connection"""
        self.controller.authenticate()  # TODO: fix permissions in torrc

    def __del__(self):
        """close connection to socket"""
        self.controller.close()

    def print_status(self):
        """print status (for debbuging)"""
        print("Version: %s" % self.controller.get_version())
        print("Process: pid:%s user:%s" % (self.controller.get_pid(),
                                           self.controller.get_user()))
        print("Read: %s bytes Written: %s bytes" % (
            self.controller.get_info(self.GETINFO['read']),
            self.controller.get_info(self.GETINFO['written'])))
        print("Current exit policy: %s" %
              self.controller.get_exit_policy().summary())
#        print("External IP: %s" %
#              self.controller.get_info(self.GETINFO['ext-ip']))
#        print("Circuit Status: %s" %
#              self.controller.get_info(self.GETINFO['circ-stat']))
        if self.controller.get_info(self.GETINFO['circ_est']):
            print("Circuit established!")
        elif self.controller.get_info(self.GETINFO['accepted']):
            print("Descriptor accepted")
        elif self.controller.get_info(self.GETINFO['good']):
            print("Good Descriptor")
        elif self.controller.get_info(self.GETINFO['enough']):
            print("Enough Dir Information")
        else:
            print("Something is going wrong.")


class Configuration(object):
    """Get and set Configuration"""
    controller = Controller.from_port(port=9051)

    def __init__(self):
        """Initialte socket connection """
        self.controller.authenticate()

    def __del__(self):
        """close connection to socket"""
        self.controller.close()

    def hidden_service(self):
        """get and format config
        :returns: dict with HiddenService keys
        """
        conf = self.controller.get_conf_map('HiddenServiceOptions')
        # TODO: waiting for stem patch
        #       https://trac.torproject.org/projects/tor/ticket/12533
        #       Support only one Hidden Service till patch
        return conf

    def general(self):
        """get general config
        :returns: TODO
        """
        KEYS = ['SocksPort',
                'DataDirectory',
                'ControlPort',
                'ControlListenAddress',
                'ControlSocket',
                'CookieAuthFileGroupReadable',
                'HTTPProxy',
                'HTTPProxyAuthenticator',
                'HTTPSProxy',
                'HTTPSProxyAuthenticator',
                'Socks4Proxy',
                'Socks5Proxy',
                'Socks5ProxyPassword',
                'SOCKSListenAddress']
        conf = self.controller.get_conf_map(KEYS)
        return conf
