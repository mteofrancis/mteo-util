#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# mteo-util.git:/tests/buffer/test_buffer_init.py
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

from mteo_util import (
  Buffer,
  ByteBuffer,
  StringBuffer,
)

class TestBuffer(TestCase):

  def test_init(self):
    buffer = Buffer()
    self.assertTrue(buffer.length() == 0)

class TestByteBuffer(TestCase):

  def test_init(self):
    buffer = ByteBuffer()
    self.assertTrue(buffer.length() == 0)
    self.assertTrue(buffer.value() == b'')

  def test_init_arg(self):
    buf = b'foo'
    buffer = ByteBuffer(buf=buf)
    self.assertTrue(buffer.length() == len(buf))
    self.assertTrue(buffer.value() == buf)

  def test_append(self):
    buffer = ByteBuffer()
    buffer.append(b'foo')
    buffer.append(b'bar')
    self.assertTrue(buffer.value() == b'foobar')
    self.assertTrue(buffer.length() == 6)

  def test_append_invalid_type(self):
    buffer = ByteBuffer()
    with self.assertRaises(TypeError):
      buffer.append(True)

  def test_clear(self):
    buffer = ByteBuffer(buf=b'foo')
    self.assertTrue(buffer.value() == b'foo')
    buffer.clear()
    self.assertTrue(buffer.value() == b'')
    self.assertTrue(buffer.length() == 0)

class TestStringBuffer(TestCase):

  def test_init(self):
    buffer = StringBuffer()
    self.assertTrue(buffer.length() == 0)
    self.assertTrue(buffer.value() == '')

  def test_init_arg(self):
    buf = 'foo'
    buffer = StringBuffer(buf=buf)
    self.assertTrue(buffer.length() == len(buf))
    self.assertTrue(buffer.value() == buf)

  def test_append(self):
    buffer = StringBuffer()
    buffer.append('foo')
    buffer.append('bar')
    self.assertTrue(buffer.value() == 'foobar')
    self.assertTrue(buffer.length() == 6)

  def test_append_invalid_type(self):
    buffer = StringBuffer()
    with self.assertRaises(TypeError):
      buffer.append(True)

  def test_clear(self):
    buffer = StringBuffer(buf='foo')
    self.assertTrue(buffer.value() == 'foo')
    buffer.clear()
    self.assertTrue(buffer.value() == '')
    self.assertTrue(buffer.length() == 0)

##
# vim: ts=2 sw=2 tw=100 et fdm=marker :
##