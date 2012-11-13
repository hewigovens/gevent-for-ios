from gevent import monkey
monkey.patch_all()

import time
assert 'built-in' not in repr(time.sleep), repr(time.sleep)

import thread
import threading
assert 'built-in' not in repr(thread.start_new_thread), repr(thread.start_new_thread)
assert 'built-in' not in repr(threading._start_new_thread), repr(threading._start_new_thread)
assert 'built-in' not in repr(threading._sleep), repr(threading._sleep)

import socket
from gevent import socket as gevent_socket
assert socket.create_connection is gevent_socket.create_connection

import os
assert 'built-in' not in repr(os.read), repr(os.read)
assert 'built-in' not in repr(os.write), repr(os.write)

assert monkey.saved
