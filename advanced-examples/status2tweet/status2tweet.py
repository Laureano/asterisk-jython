# GUI imports
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JTextField
from javax.swing import JPasswordField
from javax.swing import JLabel
from javax.swing import JButton
from javax.swing import WindowConstants
from java.awt import GridLayout

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
                    self.statusUpdater('On the phone')
                elif isinstance(event, HangupEvent):
                    self.statusUpdater('Available')

class GUI():
    def __init__(self):
        self.frame = JFrame('Phone status twitter')
        self.frame.defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE
        self.renderAsteriskLoginPanel()
        self.frame.pack()
        self.frame.visible = True

    def renderAsteriskLoginPanel(self):
        '''Render on the frame the login panel with the fields needed to
        authenticate with the Asterisk manager.'''
        self.asteriskLoginPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.asteriskLoginPanel)

        self.asteriskHostnameField = JTextField('pbx', 15)
        self.asteriskLoginPanel.add(JLabel('Hostname:'))
        self.asteriskLoginPanel.add(self.asteriskHostnameField)

        self.asteriskLoginField = JTextField('asterisk-java', 15)
        self.asteriskLoginPanel.add(JLabel('Username:'))
        self.asteriskLoginPanel.add(self.asteriskLoginField)

        self.asteriskPasswordField = JPasswordField('AsteriskJava', 15)
        self.asteriskLoginPanel.add(JLabel('Password:'))
        self.asteriskLoginPanel.add(self.asteriskPasswordField)

        self.asteriskExtensionField = JTextField('SIP/8011', 15)
        self.asteriskLoginPanel.add(JLabel('Extension:'))
        self.asteriskLoginPanel.add(self.asteriskExtensionField)

        self.asteriskLoginButton = JButton('Log in', actionPerformed=self.loginToAsterisk)
        self.asteriskLoginPanel.add(self.asteriskLoginButton)

        self.asteriskLoginStatusLabel = JLabel('Awaiting information...')
        self.asteriskLoginPanel.add(self.asteriskLoginStatusLabel)

    def renderTwitterLoginPanel(self):
        '''Render on the frame the login panel with the fields needed to
        authenticate with the Twitter API.'''
        self.twitterLoginPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.twitterLoginPanel)

        self.twitterLoginField = JTextField('TomasLaureano', 15)
        self.twitterLoginPanel.add(JLabel('Username:'))
        self.twitterLoginPanel.add(self.twitterLoginField)

        self.twitterPasswordField = JPasswordField('', 15)
        self.twitterLoginPanel.add(JLabel('Password:'))
        self.twitterLoginPanel.add(self.twitterPasswordField)

        self.twitterLoginButton = JButton('Log in', actionPerformed=self.loginToTwitter)
        self.twitterLoginPanel.add(self.twitterLoginButton)

        self.twitterLoginStatusLabel = JLabel('Awaiting information...')
        self.twitterLoginPanel.add(self.twitterLoginStatusLabel)

    def renderMainPanel(self):
        '''Render on the frame the main panel with a status label'''
        self.mainPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.mainPanel)

        self.mainPanel.add(JLabel('Status:'))
        self.statusLabel = JTextField('Running...', 15)
        self.statusLabel.editable = False
        self.mainPanel.add(self.statusLabel)

    def loginToAsterisk(self, event):
        '''Execute the login procedure to the Asterisk Manager interface'''
        self.manager = PhoneStatusListener(self.asteriskHostnameField.text, \
                                            self.asteriskLoginField.text, \
                                            self.asteriskPasswordField.text, \
                                            self.asteriskExtensionField.text)
        try:
            self.manager.addStatusUpdater(self.statusUpdater)
            self.manager.start()
            self.asteriskLoginPanel.visible = False
            self.renderTwitterLoginPanel()
            self.frame.pack()
        except:
            self.asteriskLoginStatusLabel.text = "Unable to authenticate"

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

if __name__ == "__main__":
    GUI()