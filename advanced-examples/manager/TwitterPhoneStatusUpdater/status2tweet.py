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

'''This scripts post a tweet whenever you get a new call or hangup'''

__author__ = 'Tomás Peralta <tomas.peralta(at)t-ip.com.ar'

# GUI imports
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JTextField
from javax.swing import JLabel
from javax.swing import JButton
from javax.swing import WindowConstants
from java.awt import GridLayout
from javax.swing import BorderFactory

# Custom GUI components
import sys
sys.path.append('../../')
from commons.guicomponents import asteriskloginpanel as gui
import commons.guicomponents.enhancedfields as extragui

# Phone status listener imports
from org.asteriskjava.manager import ManagerConnectionFactory
from org.asteriskjava.manager import ManagerEventListener
from org.asteriskjava.manager.event import NewStateEvent
from org.asteriskjava.manager.event import HangupEvent

# Twitter platform
import twitter

class PhoneStatusListener(ManagerEventListener):
    def __init__(self, hostname, username, password, extension):
        factory = ManagerConnectionFactory(hostname, username, password)
        self.managerConnection = factory.createManagerConnection()
        self.extensionToMonitor = extension

    def addStatusUpdater(self, updater):
        self.statusUpdater = updater

    def start(self):
        '''Connect to Asterisk Manager Interface and wait for events'''
        self.managerConnection.addEventListener(self)
        self.managerConnection.login()

    def onManagerEvent(self, event):
        '''Analyze the event type and generate an action according to it's type'''
        if isinstance(event, NewStateEvent) or isinstance(event, HangupEvent):
            (channelName, randomPart) = event.getChannel().split('-')
            if channelName == self.extensionToMonitor:
                if isinstance(event, NewStateEvent) and event.getChannelStateDesc() == 'Up':
                    self.statusUpdater('is now on the phone.')
                elif isinstance(event, HangupEvent):
                    self.statusUpdater('is now available (call ended)')

class GUI():
    def __init__(self):
        self.frame = JFrame('Phone status twitter')
        self.frame.defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE
        self.asteriskLoginPanel = gui.AsteriskLoginPanel(buttonAction=self.loginToAsterisk)
        self.asteriskLoginPanel.render()
        self.frame.add(self.asteriskLoginPanel)
        self.asteriskLoginPanel.getRootPane().setDefaultButton(self.asteriskLoginPanel.asteriskLoginButton)
        self.frame.pack()
        self.frame.visible = True

    def renderTwitterLoginPanel(self):
        '''Render on the frame the login panel with the fields needed to
        authenticate with the Twitter API.'''
        self.twitterLoginPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.twitterLoginPanel)
        
        self.twitterLoginPanel.setBorder(BorderFactory.createTitledBorder('Twitter account information'))

        self.twitterLoginField = extragui.EnhancedTextField('asterisk-jython', 15)
        self.twitterLoginPanel.add(JLabel('Username:'))
        self.twitterLoginPanel.add(self.twitterLoginField)

        self.twitterPasswordField = extragui.EnhancedPasswordField('password', 15)
        self.twitterLoginPanel.add(JLabel('Password:'))
        self.twitterLoginPanel.add(self.twitterPasswordField)

        self.twitterLoginButton = JButton('Log in', actionPerformed=self.loginToTwitter)
        self.twitterLoginPanel.add(self.twitterLoginButton)
        self.twitterLoginPanel.getRootPane().setDefaultButton(self.twitterLoginButton)

        self.twitterLoginStatusLabel = JLabel('Awaiting information...')
        self.twitterLoginPanel.add(self.twitterLoginStatusLabel)

    def renderMainPanel(self):
        '''Render on the frame the main panel with a status label'''
        self.mainPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.mainPanel)

        self.mainPanel.setBorder(BorderFactory.createTitledBorder('Application status'))

        self.mainPanel.add(JLabel('Status:'))
        self.statusLabel = JTextField('Running...', 15)
        self.statusLabel.editable = False
        self.mainPanel.add(self.statusLabel)

    def loginToAsterisk(self, event):
        '''Execute the login procedure to the Asterisk Manager interface'''
        self.manager = PhoneStatusListener(self.asteriskLoginPanel.asteriskHostnameField.text, \
                                            self.asteriskLoginPanel.asteriskLoginField.text, \
                                            self.asteriskLoginPanel.asteriskPasswordField.text, \
                                            self.asteriskLoginPanel.asteriskExtensionField.text)
        try:
            self.manager.addStatusUpdater(self.statusUpdater)
            self.manager.start()
            self.asteriskLoginPanel.visible = False
            self.renderTwitterLoginPanel()
            self.frame.pack()
        except:
            self.asteriskLoginPanel.asteriskLoginStatusLabel.text = "Unable to authenticate"

    def loginToTwitter(self, event):
        '''Execute the login procedure to the Twitter platform'''
        try:
            self.twitter = twitter.Api(username=self.twitterLoginField.text, \
                                        password=self.twitterPasswordField.text)
            self.twitter.GetUser(self.twitterLoginField.text)
            self.twitterLoginPanel.visible = False
            self.renderMainPanel()
            self.frame.pack()
        except:
            self.twitterLoginStatusLabel.text = "Unable to authenticate"

    def statusUpdater(self, update):
        self.statusLabel.text = update
        self.twitter.PostUpdate(update)

if __name__ == "__main__":
    GUI()