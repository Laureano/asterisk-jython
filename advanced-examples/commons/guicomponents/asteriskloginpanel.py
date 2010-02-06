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

'''TODO'''

__author__ = 'Tomás Peralta <tomas.peralta(at)t-ip.com.ar'

from javax.swing import JPanel
from enhancedfields import EnhancedTextField, EnhancedPasswordField
from javax.swing import JLabel
from javax.swing import JButton
from java.awt import GridLayout

class AsteriskLoginPanel(JPanel):
    def render(self):
        '''Render on the frame the login panel with the fields needed to
        authenticate with the Asterisk manager.'''
        self.layout = GridLayout(0,2)

        self.asteriskHostnameField = EnhancedTextField('localhost', 15)
        self.add(JLabel('Hostname:'))
        self.add(self.asteriskHostnameField)

        self.asteriskLoginField = EnhancedTextField('manager', 15)
        self.add(JLabel('Username:'))
        self.add(self.asteriskLoginField)

        self.asteriskPasswordField = EnhancedPasswordField('pa55word', 15)
        self.add(JLabel('Password:'))
        self.add(self.asteriskPasswordField)

        self.asteriskExtensionField = EnhancedTextField('SIP/John', 15)
        self.add(JLabel('Extension:'))
        self.add(self.asteriskExtensionField)

        self.asteriskLoginButton = JButton('Log in', actionPerformed=self.buttonAction)
        self.add(self.asteriskLoginButton)

        self.asteriskLoginStatusLabel = JLabel('Awaiting information...')
        self.add(self.asteriskLoginStatusLabel)