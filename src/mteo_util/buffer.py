#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# mteo-util.git:/src/mteo_util/buffer.py
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

## {{{ class Buffer

class Buffer:

  _buf = None

  def __init__(self):
    self._buf = []

  def append(self, buf):
    self._buf.append(buf)

  def size(self):
    size = 0
    for buf in self._buf:
      size += len(buf)
    return size

  def get_bytes(self):
    return b''.join(self._buf)

  def get_str(self):
    return self.get_bytes().decode('utf-8')

## class Buffer }}}

##
# vim: ts=2 sw=2 tw=100 et fdm=marker :
##
