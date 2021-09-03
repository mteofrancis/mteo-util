#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# mteo-util.git:/src/mteo_util/tests/test_socket.py
##

## {{{ ---- [ Header ] -----------------------------------------------------------------------------

##
# Copyright (c) 2021 Francis M <francism@destinatech.com>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2.0 as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to:
#
#   Free Software Foundation
#   51 Franklin Street, Fifth Floor
#   Boston, MA 02110
#   USA
##

## }}} ---- [ Header ] -----------------------------------------------------------------------------

from unittest import TestCase

from mteo_util import TcpSocket

import socket

class TestTcpSocket(TestCase):

  def test_init(self):
    sock = TcpSocket()
    sock.close()

  def test_init_arg(self):
    _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd = _sock.fileno()
    sock = TcpSocket(_sock)
    self.assertTrue(sock.fileobj() == _sock)
    self.assertTrue(sock.fileno() == fd)
    sock.close()

  def test_close(self):
    sock = TcpSocket()
    sock.close()
    self.assertTrue(sock.fileobj() == None)
    self.assertTrue(sock.fileno() == None)

  def test_fileobj(self):
    sock = TcpSocket()
    fileobj_type = type(sock.fileobj())
    sock.close()
    self.assertTrue(fileobj_type.__name__ == 'socket')

  def test_fileno(self):
    sock = TcpSocket()
    fd = sock.fileno()
    sock.close()
    self.assertTrue(type(fd).__name__ == 'int')
    self.assertTrue(fd > -1)

  def test_blocking(self):
    sock = TcpSocket()

    sock.blocking(True)
    sock.blocking(False)

    with self.assertRaises(TypeError):
      sock.blocking('foo')

##
# vim: ts=2 sw=2 tw=100 et fdm=marker :
##
