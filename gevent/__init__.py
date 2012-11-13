# Copyright (c) 2009-2012 Denis Bilenko. See LICENSE for details.
"""
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libev event loop.

See http://www.gevent.org/ for the documentation.
"""

from __future__ import absolute_import

version_info = (1, 0, 0, 'beta', 4)
__version__ = '1.0b4'
__changeset__ = '2641:a79f019200ac'


__all__ = ['get_hub',
           'Greenlet',
           'GreenletExit',
           'spawn',
           'spawn_later',
           'spawn_raw',
           'joinall',
           'killall',
           'Timeout',
           'with_timeout',
           'getcurrent',
           'sleep',
           'idle',
           'kill',
           'signal',
           'fork',
           'reinit',
           'run']


import sys
if sys.platform == 'win32':
    import socket  # trigger WSAStartup call
del sys


from gevent.hub import get_hub
from gevent.greenlet import Greenlet, joinall, killall
spawn = Greenlet.spawn
spawn_later = Greenlet.spawn_later
from gevent.timeout import Timeout, with_timeout
from gevent.hub import getcurrent, GreenletExit, spawn_raw, sleep, idle, kill, signal, reinit
try:
    from gevent.os import fork
except ImportError:
    __all__.remove('fork')


def run(timeout=None, event=None):
    return get_hub().join(timeout=timeout, event=event)
