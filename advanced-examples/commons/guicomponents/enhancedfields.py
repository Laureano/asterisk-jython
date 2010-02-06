#!/usr/bin/jython
# -*- coding: iso-8859-15 -*-
#
# Copyright 2010 t-ip: IP Development
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''A module that adds additional funcionalities to JTextField and JPasswordField'''

__author__ = 'Tomás Peralta <tomas.peralta(at)t-ip.com.ar'

from javax.swing import JTextField
from javax.swing import JPasswordField

class EnhancedTextField(JTextField):
    '''A JTextField that selects and unselects the text according to the focus'''
    def __init__(self, text, columns):
        '''Constructor'''
        JTextField.__init__(self, text, columns)
        self.focusGained=lambda e: e.getSource().selectAll()
        self.focusLost=lambda e: e.getSource().select(0,0)

class EnhancedPasswordField(JPasswordField):
    '''A JPasswordField that selects and unselects the text according to the focus'''
    def __init__(self, text, columns):
        '''Constructor'''
        JPasswordField.__init__(self, text, columns)
        self.focusGained=lambda e: e.getSource().selectAll()
        self.focusLost=lambda e: e.getSource().select(0,0)