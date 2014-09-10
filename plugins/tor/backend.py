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


class Get(object):
    """Collecting and formatting status-data of tor"""

    try:
        _controller = Controller.from_port(port=9051)
    except:
        pass

    def __init__(self, debug):  # TODO: figure out what debug is and where it come from
        """initiate connection"""
        try:
            self._controller.authenticate()     # TODO: Needs pre config
        except Exception, authentication:
            raise authentication
        else:
            self.version = self._controller.get_version()

    def __del__(self):
        """close connection to socket"""
        try:
            self._controller.close()
        except:
            pass

    def status(self):
        """print status (for debbuging)"""
        _GETINFO = {
            'config-file': 'config-file',
            'address-mapping': 'address-mappings/all',
            'ext_ip': 'address',
            'read': 'traffic/read',
            'written': 'traffic/written',
            'circ_est': 'status/circuit-established',
            'enough': 'status/enough-dir-info',
            'good': 'status/good-server-descriptor',
            'accepted': 'status/accepted-server-descriptor'
            }
        if self._controller.get_info(_GETINFO["circ_est"]):
            _circ_est = "Running"
        else:
            _circ_est = "Not Running. Check logs."
        try:
            _ext_ip = self._controller.get_info(_GETINFO["ext_ip"])
        except:
            _ext_ip = "Unable to fetch IP."
        _status_package = {
            'version': self._controller.get_version(),
            'status': _circ_est,
            'ext_ip': _ext_ip,
            'read': self._controller.get_info(_GETINFO["read"]) + " B",
            'written': self._controller.get_info(_GETINFO["written"]) + " B"
            }
        return _status_package
# 
# 
# class Configuration(object):
#     """Get and set Configuration"""
#     controller = Controller.from_port(port=9051)    # TODO: change to _controller
# 
#     def __init__(self):
#         """Initialte socket connection """
#         self.controller.authenticate()
# 
#     def __del__(self):
#         """close connection to socket"""
#         self.controller.close()
# 
#     def hidden_service(self):
#         """get and format config
#         :returns: dict with HiddenService keys
#         """
#         conf = self.controller.get_conf_map('HiddenServiceOptions')
#         # TODO: waiting for stem patch
#         #       https://trac.torproject.org/projects/tor/ticket/12533
#         #       Support only one Hidden Service till patch
#         return conf
# 
#     def general(self):
#         """get general config
#         :returns: TODO
#         """
#         KEYS = ['SocksPort',
#                 'DataDirectory',
#                 'ControlPort',
#                 'ControlListenAddress',
#                 'ControlSocket',
#                 'CookieAuthFileGroupReadable',
#                 'HTTPProxy',
#                 'HTTPProxyAuthenticator',
#                 'HTTPSProxy',
#                 'HTTPSProxyAuthenticator',
#                 'Socks4Proxy',
#                 'Socks5Proxy',
#                 'Socks5ProxyPassword',
#                 'SOCKSListenAddress']
#         conf = self.controller.get_conf_map(KEYS)
#         return conf
