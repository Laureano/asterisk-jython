from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JTextField
from javax.swing import JPasswordField
from javax.swing import JLabel
from javax.swing import JButton
from javax.swing import WindowConstants
from javax.swing import ImageIcon
from java.awt import GridLayout

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

        self.asteriskHostnameField = JTextField('localhost', 15)
        self.asteriskLoginPanel.add(JLabel('Hostname:'))
        self.asteriskLoginPanel.add(self.asteriskHostnameField)

        self.asteriskLoginField = JTextField('manager', 15)
        self.asteriskLoginPanel.add(JLabel('Username:'))
        self.asteriskLoginPanel.add(self.asteriskLoginField)

        self.asteriskPasswordField = JPasswordField('pa55word', 15)
        self.asteriskLoginPanel.add(JLabel('Password:'))
        self.asteriskLoginPanel.add(self.asteriskPasswordField)

        self.asteriskLoginButton = JButton('Log in', actionPerformed=self.loginToAsterisk)
        self.asteriskLoginPanel.add(self.asteriskLoginButton)

        self.asteriskLoginStatusLabel = JLabel('Awaiting information...')
        self.asteriskLoginPanel.add(self.asteriskLoginStatusLabel)

    def renderTwitterLoginPanel(self):
        '''Render on the frame the login panel with the fields needed to
        authenticate with the Twitter API.'''
        self.twitterLoginPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.twitterLoginPanel)

        self.twitterLoginField = JTextField('asterisk-jython', 15)
        self.twitterLoginPanel.add(JLabel('Username:'))
        self.twitterLoginPanel.add(self.twitterLoginField)

        self.twitterPasswordField = JPasswordField('pa55word', 15)
        self.twitterLoginPanel.add(JLabel('Password:'))
        self.twitterLoginPanel.add(self.twitterPasswordField)

        self.twitterLoginButton = JButton('Log in', actionPerformed=self.loginToTwitter)
        self.twitterLoginPanel.add(self.twitterLoginButton)

        self.twitterLoginStatusLabel = JLabel('Awaiting information...')
        self.twitterLoginPanel.add(self.twitterLoginStatusLabel)

    def loginToAsterisk(self, event):
        '''Execute the login procedure to the Asterisk Manager interface'''
        self.asteriskLoginPanel.visible = False
        self.renderTwitterLoginPanel()
        self.frame.pack()

    def loginToTwitter(self, event):
        '''Execute the login procedure to the Twitter platform'''
        pass

if __name__ == "__main__":
    GUI()